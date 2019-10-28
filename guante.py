import serial
import time
import pyttsx3

helena = 'voces/MSSpeech_TTS_es-ES_Helena.msi'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i in range(len(voices)):
    print('voice ', voices[i].id, ' id: ', i)
    #speech_engine.setProperty('voice', voice.id)
    #speech_engine.say('The quick brown fox')

print(engine.getProperty('voice'))
engine.setProperty('voice', 'spanish')
print(engine.getProperty('voice'))

while (False):
    #try:
    # Inicializamos el canal de lectura
    #arduino = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
    while True:
    # Leemos mensaje mandado desde arduino
        #val = arduino.readline()
        val = '10000'

        # Si flexionamos solo pulgar
        if val == '10000':
            # TODO:
            #engine.say('Esto es una prueba')
            print(engine.getProperty('voices')[0])
            engine.runAndWait()
        # Si flexionamos solo índice
        """
        elif val == '01000':
            # TODO:
            0
        # Si flexionamos solo corazón
        elif val == '00100':
            # TODO:
            0
        # Si flexionamos solo anular
        elif val == '00010':
            # TODO:
            0
        # Si flexionamos solo meñique
        elif val == '00001':
            # TODO:
            0
        # Si flexionamos pulgar e índice
        elif val == '11000':
            # TODO:
            0 
        # Si flexionamos pulgar y corazón
        elif val == '10100':
            # TODO:
            0 
        # Si flexionamos pulgar y anular
        elif val == '10010':
            # TODO:
            0 
        # Si flexionamos pulgar y meñique
        elif val == '10001':
            # TODO:
            0 
        # Si flexionamos índice y corazón
        elif val == '01100':
            # TODO:
            0 
        # Si flexionamos índice y anular
        elif val == '01010':
            # TODO:
            0 
        # Si flexionamos índice y meñique
        elif val == '01001':
            # TODO:
            0 
        # Si flexionamos corazón y anular
        elif val == '00110':
            # TODO:
            0 
        # Si flexionamos corazón y meñique
        elif val == '00101':
            # TODO:
            0 
        # Si flexionamos anular y meñique
        elif val == '00011':
            # TODO:
            0 
        # Si flexionamos pulgar, índice y corazón
        elif val == '11100':
            # TODO:
            0 
        # Si flexionamos pulgar, índice y anular
        elif val == '11010':
            # TODO:
            0 
        # Si flexionamos pulgar, índice y meñique
        elif val == '11001':
            # TODO:
            0 
        # Si flexionamos pulgar, corazón y anular
        elif val == '10110':
            # TODO:
            0 
        # Si flexionamos pulgar, corazón y meñique
        elif val == '10101':
            # TODO:
            0 
        # Si flexionamos pulgar, anular y meñique
        elif val == '10011':
            # TODO:
            0 
        # Si flexionamos índice, corazón y anular
        elif val == '01110':
            # TODO:
            0 
        # Si flexionamos índice, corazón y meñique
        elif val == '01101':
            # TODO:
            0 
        # Si flexionamos corazón, anular y meñique
        elif val == '00111':
            # TODO:
            0 
        # Si flexionamos pulgar, índice, corazón y anular
        elif val == '11110':
            # TODO:
            0 
        # Si flexionamos pulgar, índice, corazón y meñique
        elif val == '11101':
            # TODO:
            0 
        # Si flexionamos pulgar, índice, anular y meñique
        elif val == '11011':
            # TODO:
            0 
        # Si flexionamos pulgar, corazón, anular y meñique
        elif val == '10111':
            # TODO:
            0 
        # Si flexionamos índice, corazón, anular y meñique
        elif val == '01111':
            # TODO:
            0 
        # Si flexionamos todos los dedos
        elif val == '11111':
            # TODO:
            0 
        """

    #except:
     #   print('No se ha podido acceder al puerto serie.')
      #  time.sleep(1.5)

arduino.close()