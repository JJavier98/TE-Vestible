import serial
import time

conectado = False

while (not conectado):
    try:
        arduino = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
        while True:
            val = arduino.readline()
            print(val)
    except:
        print('No se ha podido acceder al puerto serie.')
        time.sleep(1.5)

arduino.close()