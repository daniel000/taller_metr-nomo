
from Tkinter import *
from Tkinter import Tk
import tkMessageBox
from a import Grabar
import pyaudio
import Tkinter
import tkSnack
import time
import sys





def main():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    # metrónomo
    def playNote(freq, duration):

     snd = tkSnack.Sound()
     filt = tkSnack.Filter('generator', freq, 30000, 0.0, 'sine', int(11500*duration))
     snd.stop()
     snd.play(filter=filt, blocking=1)


def soundStop():

    try:
        root = root.destroy()
        filt = None
    except:
        pass


if len(sys.argv) == 1:
    ubpm = raw_input('ingresar tempo: ')
else:
    ubpm = sys.argv[1]





Ubpm = int(ubpm)
if Ubpm > 300:
    BPM = 300
else :
    BPM = ubpm



if BPM == 300:
    print "The maximum BPM is 300, using 300 BPM"
else:
    pass


bpm = 60.0 / int(BPM)

delay = bpm - 0.1


root = Tkinter.Tk()
tkSnack.initializeSnack(root)

tkSnack.audio.play_gain(80)


while True:
    playNote(880, 0.1)
    soundStop()
    time.sleep(delay)


root.withdraw()
     # Creacion de la ventana

    ventana = Tk()

    ventana.title("Ventana Principal")

    audio1 = Grabar(CHUNK, FORMAT, CHANNELS, RATE)


    d = BooleanVar(ventana)
    e = BooleanVar(ventana)
    e.set(False)
    f = BooleanVar(ventana)
    f.set(False)

    global arreglo1

    arreglo1 = []


    # Uso de frames para organizar la ventana.
    frame1 = Frame(ventana)
    frame1.pack(side=TOP)
    frame2 = Frame(ventana)
    frame2.pack(side=TOP)


    # Creacion e insercion del cuadro de texto 1.
    cuadro= Label(frame1, fg="black", padx=15, pady=10, text="Digite el nombre del archivo 1:")
    cuadro.pack(side=LEFT)

    # Creacion e insercion de cuadro de entrada 1.
    e1 = Entry(frame1, bd=5, insertwidth=1)
    e1.pack(side=LEFT, padx=15, pady=10)

    # Mensajes de grabacion activada.
    mensaje1 = Label(frame1, fg='red', padx=15, pady=10, text='Grabando...')

    # Funcion activa mensaje y grabar

    def activasms1():
        if e1.get() == '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso nombre del audio.')
        else:
            d.set(True)
            e1.configure(state='disabled')
            audio1.inicio()
            mensaje1.pack(side=LEFT)
            while d.get():
                audio1.grabacion()
                ventana.update()
                if d.get() is False:
                    break



    # Funcion desactiva mensaje y para de grabar.
    def desactivasms1():
        d.set(False)
        e.set(True)
        mensaje1.pack_forget()
        global  arreglo1
        arreglo1 = audio1.parar()

        audio1.creaAudio(e1.get())
        grabarButton1.pack_forget()
        pararButton1.pack_forget()





    def reproduccion1():
        audio1.reproduce(e1.get())



    # Creacion de botones.
    grabarButton1 = Button(frame2, padx=30, pady=2, text="Grabar", command=activasms1)
    grabarButton1.pack(side=LEFT)

    pararButton1 = Button(frame2, padx=30, pady=2, text="Parar", command=desactivasms1)
    pararButton1.pack(side=LEFT)

    reproducirButton1 = Button(frame2, padx=20,pady=2, text="Reproducir", command=reproduccion1)
    reproducirButton1.pack(side=RIGHT)



ventana.mainloop()

if __name__ == "__main__":
    main()