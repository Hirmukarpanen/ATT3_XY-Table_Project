# Ryhma
Timi & Sebastian 👍

XY-pöydän datan vastaanottaminen ja lähettäminen MQTT brokerin kautta, sekä mahdollinen visualisointi.


Proof of Concept: XY-Pöydän Datan Vastaanottaminen ja Lähettäminen MQTT Brokerin Kautta


Projektin tavoitteena on osoittaa, että XY-pöydän ohjaus ja datan hallinta MQTT-protokollan avulla on teknisesti toteutettavissa ja että nykyinen laitteisto (XY-pöytä ja Beckhoffin PLC CX9020) tukee suunniteltua toteutusta.
Ratkaisun on tarkoitus täyttää kaikki asetetut vaatimukset ja suorittaa tarvittavat toiminnot, kuten datan käsittely ja ohjaus.


Tekninen toteutettavuus:
Varmistetaan, että MQTT-protokolla voidaan integroida PLC-järjestelmään ja että datan käsittely toimii luotettavasti.
Toiminnallisuuden täyttyminen: Ratkaisun on pystyttävä toteuttamaan ohjausliikkeet ja simuloimaan kuormalavan siirtämistä paikasta A paikkaan B.
Riskien arviointi: Ohjelmiston käytön kokemattomuus ja mahdolliset fyysisen laitteiston ongelmat voivat vaikuttaa projektiin, mutta näitä riskejä voidaan lieventää koulutuksella ja laitteiston kokoonpanomuutoksilla.


Ratkaisun Kuvaus:
XY-pöydässä on kaksi lineaarijohdetta, joita ohjataan servomoottoreilla. Toisen johteen päässä on pneumatiikkasylinteri, ja järjestelmään kuuluu kaksi anturia, jotka mittaavat servoakseleiden kotiasemat. 
Projektin perusidea on simuloida kuormalavan siirtämistä paikasta A paikkaan B.


Komponentit:
Beckhoffin PLC CX9020 ja Twincat 3 -ohjelmisto.
Ohjelmistointegraatio: MQTT-viestinvälitysjärjestelmä mahdollistaa XY-pöydän liikkeiden ja anturidatan hallinnan, sekä käskyjen välittämisen ja käsittelyn reaaliaikaisesti.


Keskeiset Toiminnot:
Datan vastaanotto ja käsittely: XY-pöytä vastaanottaa ohjauskäskyjä MQTT-brokerilta ja käsittelee ne toteuttaakseen tarvittavat liikkeet.
Datan lähetys ja tilapäivitykset: XY-pöytä lähettää sensoridataa ja tilapäivityksiä takaisin MQTT-brokerille reaaliajassa.
Liikkeiden simulointi: XY-pöytä simuloi kuormalavan siirtoa käskystä ja varmistaa oikean liikeradan.


Testiskenaariot ja Käyttötapaukset:

Testiskenaario 1: Testaa, että XY-pöytä voi vastaanottaa liikkumiskäskyjä MQTT:n kautta ja että liikkeet suoritetaan täsmällisesti.
Menestyskriteeri: XY-pöytä liikkuu annettujen koordinaattien mukaisesti ilman virheitä.

Testiskenaario 2: Testaa, että anturitiedot lähetetään MQTT-brokerille ja että ne ovat synkronissa liikkeiden kanssa.
Menestyskriteeri: Datan lähetys toimii ilman viivettä, ja vastaanottava järjestelmä pystyy käsittelemään tietoa.

Testiskenaario 3: Testaa integraatio Twincat IoT -sovelluksen kanssa, jos modeemi ja ethernetkytkin saadaan käyttöön.
Menestyskriteeri: Etäohjaus toimii ilman häiriöitä ja mahdollistaa reaaliaikaisen ohjauksen.


Tekniset Vaatimukset ja Resurssit:
Laitteet: XY-pöytä, servomoottorit, pneumatiikkasylinteri, anturit, Beckhoffin PLC CX9020.
Ohjelmistot: Twincat 3 ja MQTT-broker.
Verkko: Modeemi ja ethernetkytkin (tarvittaessa etäohjaukseen Twincat IoT -sovelluksella).


Rajoitteet ja Haasteet:
Fyysiset asennukset: Lineaarijohteiden asennustapa voi rajoittaa toimintoja; johteet voi olla tarpeen asentaa uudelleen optimaalisen toiminnan saavuttamiseksi.
Ohjelmistohaasteet: PLC:n ongelmat voivat aiheuttaa viivästyksiä; odotetaan, että tekniset ongelmat voidaan ratkaista projektin aikana.


Demo ja Arviointimenetelmät:
Demotilaisuus: Suoritetaan live-esittely, jossa näytetään MQTT-datan vastaanotto ja lähetys sekä XY-pöydän liikkeet.
Arviointi: Arvioidaan liikkeiden täsmällisyyttä, MQTT-datan käsittelynopeutta ja järjestelmän luotettavuutta.



Dokumentointi ja Raportointi:
Viikko 1: Aloitus, laitteiston tarkistus ja PLC:n herättely. PLC saatiin palautettua vanhaan ohjelmaan, mutta online-tila ei toiminut.
Viikko 2: Yhteyden muodatamisen yrittäminen MQTT kansssa. PLC jouduttiin vaihtamaan tuntemattomasta syystä. Muodostimme projektille yhteden GitHub:in kanssa. Sekä visuaalista siistimistä sähkökeskuksella.



Aikataulu ja Seuranta:
Viikko 1-2: Laitteiston tarkistus, vanhan ohjelman palautus ja PLC:n alustaminen.
Viikko 3-4: MQTT-protokollan käyttöönotto ja ensimmäiset testit.
Viikko 5-6: Testiskenaarioiden suoritus ja Twincat IoT -integraation testaaminen (tarvittaessa).
Viikko 7-8: Demotilaisuus ja projektin tulosten arviointi.

Projektin seuranta: Viikottaiset raportit edistymisestä ja ongelmista, sekä lopullinen yhteenveto PoC:n onnistumisesta.


![Nimetön kaavio drawio](https://github.com/user-attachments/assets/71bc1fd0-c497-4ee0-97ba-6e4a73698bd3)

MVP- on muodostaa edes jonkunlainen yhteys twincatin ja brokerin välillä.

Stretch goal-
