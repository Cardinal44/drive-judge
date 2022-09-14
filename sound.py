import math        
import pyaudio
import time   
def alarm():
   
    PyAudio = pyaudio.PyAudio     

    BITRATE =   2000   #number of frames per second/frameset.
    FREQUENCY = 5000  
    LENGTH = 0.4 #seconds to play sound


    NUMBEROFFRAMES = int(BITRATE * LENGTH)


    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''
    #generating waves
    for x in range(NUMBEROFFRAMES):
        WAVEDATA =WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
    for x in range(RESTFRAMES):
        WAVEDATA = WAVEDATA+chr(128)


    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(1),channels =2,rate = BITRATE,output = True)


    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()

    p.terminate()

alarm()