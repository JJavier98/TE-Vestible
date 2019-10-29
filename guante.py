import serial
import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'spanish')

alexa_activa = False
fin_time = 0
ini_time = 0

while (True):
    try:
        # Inicializamos el canal de lectura
        arduino = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=3.0)
        while True:
        # Leemos mensaje mandado desde arduino
            val = str(arduino.readline())
            val = val[2:7]

            if alexa_activa:
                # Si flexionamos solo pulgar
                if val == '10000':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos solo índice
                elif val == '01000':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos solo corazón
                elif val == '00100':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos solo anular
                elif val == '00010':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos solo meñique
                elif val == '00001':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar e índice
                elif val == '11000':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar y corazón
                elif val == '10100':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar y anular
                elif val == '10010':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar y meñique
                elif val == '10001':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos índice y corazón
                elif val == '01100':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos índice y anular
                elif val == '01010':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos índice y meñique
                elif val == '01001':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos corazón y anular
                elif val == '00110':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos corazón y meñique
                elif val == '00101':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos anular y meñique
                elif val == '00011':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar, índice y corazón
                elif val == '11100':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar, índice y anular
                elif val == '11010':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar, índice y meñique
                elif val == '11001':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar, corazón y anular
                elif val == '10110':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar, corazón y meñique
                elif val == '10101':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar, anular y meñique
                elif val == '10011':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos índice, corazón y anular
                elif val == '01110':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos índice, corazón y meñique
                elif val == '01101':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos corazón, anular y meñique
                elif val == '00111':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar, índice, corazón y anular
                elif val == '11110':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar, índice, corazón y meñique
                elif val == '11101':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar, índice, anular y meñique
                elif val == '11011':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos pulgar, corazón, anular y meñique
                elif val == '10111':
                    # TODO:
                    engine.say('')
                    alexa_activa = False
                # Si flexionamos índice, corazón, anular y meñique
                elif val == '01111':
                    # TODO:
                    engine.say('')
                    alexa_activa = False

                engine.runAndWait()
                fin_time = time.localtime(time.time())[5]
                if fin_time - ini_time > 3:
                    alexa_activa = False
                    ini_time = 99
            # Si flexionamos todos los dedos
            elif val == '11111':
                engine.say('Alexa')
                engine.runAndWait()
                alexa_activa = True
                ini_time = time.localtime(time.time())[5]

    except:
        print('No se ha podido acceder al puerto serie.')
        time.sleep(1.5)