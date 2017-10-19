# IoT-Sensor mit ESP8266
Dies ist eine Anleitung zum Bau eines Temperatur-/Druck-Sensors mit dem ESP8266-Microcontroller.
## Bauteile
1 Microcontroller [NodeMCU, ESP8266](https://www.ebay.com/itm/NodeMcu-Lua-WIFI-Internet-Things-development-board-based-ESP8266-CP2102-module-/201542946669?hash=item2eece54f6d:g:EOIAAOSw4q9XT5mo)

1 Temperatur- & Drucksensor [BMP280](https://www.ebay.com/itm/1x-GY-BMP280-3-3-BMP280-3-3V-High-Precision-Atmospheric-Pressure-Sensor-BMP180/281983204149?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D41375%26meid%3Df0f0ae46083c44c6a18684659016f1bb%26pid%3D100033%26rk%3D2%26rkt%3D2%26sd%3D201542946669&_trksid=p2045573.c100033.m2042)

1 OLED-Display (128 x 64 Pixel) [SSD1306](https://www.ebay.com/itm/0-96-I2C-IIC-SPI-Serial-128X64-OLED-LCD-Display-SSD1306-for-51-STM32-Arduino-/201688735605?var=&hash=item2ef595df75:m:m1O7zNonCe3M8LIIgLYvBPw) (white + IIC)

1 [Breadboard](https://www.ebay.com/itm/Mini-Prototype-Solderless-self-adhensive-Breadboard-400-Contacts-Best-/222062903350?epid=1045888288&hash=item33b3fb0036:g:4A0AAOSwnONZB-Kj)

1 [Batterie-Gehäuse](https://www.ebay.com/itm/3-Pcs-Wired-ON-OFF-Switch-3-x-AA-4-5V-Batteries-Battery-Holder-Case-LW-/182387276678?epid=1149395326&hash=item2a7720fb86:g:yS0AAOSw-0xYT1iu) mit [MicroUSB-Stecker](https://www.ebay.com/itm/10PCS-5-Pin-Micro-USB-Type-B-Male-Plug-Connector-Plastic-Cover-/182523146896?epid=2113648798&hash=item2a7f3a3290:g:w1YAAOSw03lY6h57) oder MicroUSB-Ladegerät

12 Verbindungskabel (6 [male-male](https://www.ebay.com/itm/40pcs-10cm-Male-to-Male-DuPont-Wire-Jumper-Color-Cable-Arduino-Breadboard-DIY/142518863204?_trkparms=aid%3D555019%26algo%3DPL.BANDIT%26ao%3D1%26asc%3D41375%26meid%3Db9822c424ed7453d9e5c9388b65f351a%26pid%3D100506%26rk%3D1%26rkt%3D1%26&_trksid=p2045573.c100506.m3226), 6 [female-male](https://www.ebay.com/itm/40PCS-Dupont-10CM-Male-To-Female-Jumper-Wire-Ribbon-Color-Cable-for-Arduino-NEW-/142513849970?epid=523678718&hash=item212e7cc672:g:qE8AAOSwX0NZwzdI))

Totale Kosten: 10-15 $
## Zusammenbau
Bei der Verkabelung muss darauf geachtet werden, dass gleich markierte Pins miteinander verbunden werden:

- VCC/3V3 --> VCC/3V3
- GND --> GND
- SCL --> SCL
- SDA --> SDA

Zudem gehören folgende Pins zu den jeweiligen Bezeichnungen:

- Pin 2 [D2] = SDA
- Pin 3 [D2] = SCL
- CSB = VCC/3V3
- SD0 = GND

## Verbinden mit dem ESP8266 & Laden der Treiber
1. Lade die Nötigen Dateien an deinem PC/Laptop herunter. Entweder von hier oder von diesem [Link](https://tinyurl.com/iotTecDay). Die heruntergeladene Zip-Datei muss nun entpackt/extrahiert werden. Nun sollte ein extrahierter Ordner "Sensor" vorhanden sein.
2. Verbinde dein PC/Laptop mit dem WLAN des ESP8266. Der WLAN-Name lautet "Sensor_xx", wobei `xx` der grünen Zahl auf dem ESP8266-Microcontroller entspricht. Das Passwort ist: `iotsensxx`. Hier ist `xx` ebenfalls die grüne Nummer auf dem Chip.
3. Öffne die Datei `webrepl.html` aus dem Ordner `Sensor/WebREPL`. 
4. Falls du dich nicht mit dem WLAN des ESP8266 verbinden kannst, überprüfe die Verkabelung oder betätige den on/off-Schalter am Batteriengehäuse. Beim Einschalten sollte die blaue LED auf dem Microcontroller kurz aufleuchten.
5. Bist du mit dem WLAN des ESP8266 verbunden, klicke im geöffneten Browser (WebREPL.html) auf den Button `Connect`. Nun wirst du aufgefordert ein Passwort einzugeben. Dieses lautet: `iot1`.
6. Sende nun die Dateien `ssd1306.py` und `bme280.py` an den Microcontroller. Dazu klickst du auf den Button `Durchsuchen` und wählst zuerst die Datei `ssd1306.py`aus. Nun auf den Button `Send to device` klicken. Wiederhole den Vorgang für die Datei `bme280.py`.
