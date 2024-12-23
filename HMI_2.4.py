import tkinter as tk
import json
import paho.mqtt.client as mqtt

# MQTT Configuration
BROKER = "127.0.0.1"  # Mosquitto broker's hostname
PORT = 1884           # Custom port
USERNAME = "admin"    # MQTT username
PASSWORD = "1234"     # MQTT password
CLIENT_ID = "HMI"     # Unique client ID
SUB_TOPIC = "plc2pc"  # Subscription topic
PUB_TOPIC = "pc2plc"  # Publish topic

class XYTableHMI:
    def __init__(self, root):
        self.root = root
        self.root.title("XY Table HMI")

        # Initialize MQTT Client
        self.client = mqtt.Client(client_id=CLIENT_ID)
        self.client.username_pw_set(USERNAME, PASSWORD)  # Set username and password
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(BROKER, PORT, 60)
        self.client.loop_start()

        # Variables for MQTT data
        self.x_coord = tk.StringVar(value="0")
        self.y_coord = tk.StringVar(value="0")
        self.power_on = tk.StringVar(value="OFF")
        self.homed = tk.StringVar(value="No")
        self.reset_state = False  # Initial state for the reset toggle
        self.piston_state = False  # Initial state for the piston (False = Down, True = Up)
        self.power_state = False  # Initial state for power toggle (False = OFF, True = ON)

        # UI Layout
        self.create_widgets()

    def create_widgets(self):
        # Status Section
        tk.Label(self.root, text="Status", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="X Coordinate:").grid(row=1, column=0, sticky="e")
        tk.Label(self.root, textvariable=self.x_coord).grid(row=1, column=1, sticky="w")

        tk.Label(self.root, text="Y Coordinate:").grid(row=2, column=0, sticky="e")
        tk.Label(self.root, textvariable=self.y_coord).grid(row=2, column=1, sticky="w")

        tk.Label(self.root, text="Power On:").grid(row=3, column=0, sticky="e")
        tk.Label(self.root, textvariable=self.power_on).grid(row=3, column=1, sticky="w")

        tk.Label(self.root, text="Homed:").grid(row=4, column=0, sticky="e")
        tk.Label(self.root, textvariable=self.homed).grid(row=4, column=1, sticky="w")

        # Control Section
        tk.Label(self.root, text="Control", font=("Arial", 14)).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="X Coordinate:").grid(row=6, column=0, sticky="e")
        self.x_entry = tk.Entry(self.root)
        self.x_entry.grid(row=6, column=1)

        tk.Label(self.root, text="Y Coordinate:").grid(row=7, column=0, sticky="e")
        self.y_entry = tk.Entry(self.root)
        self.y_entry.grid(row=7, column=1)

        self.power_button = tk.Button(self.root, text="Power OFF", command=self.toggle_power, bg="gray")
        self.power_button.grid(row=8, column=0, columnspan=2, pady=5)

        tk.Button(self.root, text="Home", command=self.send_home).grid(row=9, column=0, pady=5)
        tk.Button(self.root, text="Send Coordinates", command=self.send_coordinates).grid(row=9, column=1, pady=5)

        self.reset_button = tk.Button(self.root, text="Reset: OFF", command=self.toggle_reset, bg="gray")
        self.reset_button.grid(row=10, column=0, columnspan=2, pady=5)

        # Piston control (Toggle)
        self.piston_button = tk.Button(self.root, text="Piston Down", command=self.toggle_piston)
        self.piston_button.grid(row=11, column=0, columnspan=2, pady=10)

    def send_home(self):
        self.publish_message({"Home": True})

    def toggle_reset(self):
        self.reset_state = not self.reset_state
        state_text = "ON" if self.reset_state else "OFF"
        self.reset_button.config(text=f"Reset: {state_text}", bg="green" if self.reset_state else "gray")
        self.publish_message({"Reset": self.reset_state})

    def send_coordinates(self):
        try:
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())

            # Validate that the coordinates are within the allowed range
            if x < 0 or x > 250 or y < 0 or y > 250:
                # No popup, just print to console if coordinates are invalid
                print("Coordinates must be between 0 and 250.")
            else:
                # Publish message if coordinates are valid
                self.publish_message({"X": x, "Y": y})
        except ValueError:
            # If the coordinates are invalid
            print("Invalid coordinates. Please enter integers.")

    def publish_message(self, message):
        self.client.publish(PUB_TOPIC, json.dumps(message))

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected successfully!")
            self.client.subscribe(SUB_TOPIC)
        else:
            print(f"Failed to connect to MQTT broker. Code: {rc}")

    def on_message(self, client, userdata, msg):
        try:
            # Decode the message payload
            payload = msg.payload.decode()

            # Print the raw payload for debugging
            print(f"Received message: {repr(payload)}")  # Using repr() to show invisible characters
            print(f"Message length: {len(payload)}")  # Print the message length

            # Strip any trailing characters, including null bytes
            payload = payload.strip().replace("FALSE", "false").replace("TRUE", "true").replace("\x00", "")

            # Debugging step: Ensure the payload is correct
            print(f"Processed payload: {repr(payload)}")  # Using repr() to show invisible characters

            # Try to parse the JSON string
            data = json.loads(payload)

            # Update UI elements with the received data
            self.x_coord.set(data.get("x", "N/A"))
            self.y_coord.set(data.get("y", "N/A"))
            self.power_on.set("ON" if data.get("power") else "OFF")
            self.homed.set("Yes" if data.get("homed") else "No")

        except json.JSONDecodeError as e:
            # If there is a JSON decode error, print it
            print(f"JSON decode error: {str(e)}")
        except Exception as e:
            # Catch other unexpected errors and print them
            print(f"Unexpected error: {str(e)}")

    def toggle_piston(self):
        """Toggle the piston state between up (True) and down (False)."""
        self.piston_state = not self.piston_state  # Toggle the piston state
        state_text = "Piston Up" if self.piston_state else "Piston Down"  # Determine the state text

        # Update the button text to reflect the current state
        self.piston_button.config(text=state_text)

        # Publish message to control the piston state (True = Up, False = Down)
        self.publish_message({"Piston": self.piston_state})
        print(f"Piston command: {state_text}")

    def toggle_power(self):
        """Toggle the power state between on (True) and off (False)."""
        self.power_state = not self.power_state  # Toggle the power state
        state_text = "Power ON" if self.power_state else "Power OFF"  # Determine the state text

        # Update the button text to reflect the current state
        self.power_button.config(text=state_text, bg="green" if self.power_state else "gray")

        # Publish message to control the power state (True = ON, False = OFF)
        self.publish_message({"PowerOn": self.power_state})
        print(f"Power command: {state_text}")

# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = XYTableHMI(root)
    root.mainloop()
