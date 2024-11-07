
1. JSON-määrittely
   
Suunnitellaan ensin JSON-viesti, jolla voit lähettää XY-pöydän koordinaatit ja muut tarvittavat komennot

command: Voidaan käyttää ohjaamaan erilaisia toimintoja, kuten "move", "stop", tai "status".

x_position ja y_position: Määrittävät XY-pöydän tavoitekoordinaatit.

speed: Liikkumisnopeus.

2. TwinCATin PLC-koodi
   
TwinCATissa määritellään MQTT-viestin vastaanotto ja sen käsittely. vastaanotetaan JSON-viesti ja parsitaan koordinaatit sekä nopeus komentoja

3. JSON-viestin parsinta
 
Seuraavaksi luodaan funktio (tai etsitän valmis koodi) joka parsii JSON-viestin ja poimii siitä halutut tiedot.

4. Toimintojen määrittely

MoveXYTable ja StopXYTable ovat funktioita, jotka sisältävät XY-pöydän ohjauslogiikan, kuten moottorien käynnistämisen tai pysäyttämisen, sekä nopeuden asettamisen.

5. Palautteen lähetys
   
Kun XY-pöytä on saavuttanut tavoitepaikan tai kun komento on vastaanotettu, tai joku virhetilanne on mennyt päälle voidaan lähettää palautteena tilatieto.
![Untitled Diagram drawio](https://github.com/user-attachments/assets/afda05a4-785d-4125-ba84-e7163f23f83c)
