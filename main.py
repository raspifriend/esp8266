import machine
import socket
import ssd1306
import bme280

i2c = machine.I2C(scl = machine.Pin(4), sda = machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
bme = bme280.BME280(i2c = i2c)

oled.fill(0)
oled.text('Temperatur:', 0,0)
oled.text(bme.values[0],0,10)
oled.text('Druck:',0,20)
oled.text(bme.values[1],0,30)
oled.text('Sensor von',0,45)
oled.text('Felix',0,55)
oled.show()

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

html = """<!DOCTYPE html>
<html>
    <head> <title>IoT Sensor</title> </head>
    <body><h3>ESP8266 Temperatur-/Drucksensor</h3>
    <table border="1"> <tr><th>Temperatur</th><th>Druck</th></tr> %s </table></body> <br>
    TecDay, 19. Oktober 2017
</html>
"""

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    a = bme.values[0]
    b = bme.values[1]
    oled.fill(0)
    oled.text('Temperatur:', 0,0)
    oled.text(a,0,10)
    oled.text('Druck:',0,20)
    oled.text(b,0,30)
    oled.text('Sensor von',0,45)
    oled.text('Felix',0,55)
    oled.show()
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    row = ['<tr><td>%s</td><td>%s</td></tr>' % (a, b)]
    response = html % '\n'.join(row)
    cl.send(response)
    cl.close()



