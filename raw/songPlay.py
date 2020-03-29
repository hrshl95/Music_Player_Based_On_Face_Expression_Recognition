
import sys

# from tkinter import *

from pydub import AudioSegment
from pydub.playback import play
from tkinter import *


def play_song():
    song = AudioSegment.from_wav("audio.wav")
    play(song)

def open_player():

    window = Tk()

    window.title("Expression Player")

    width = (window.winfo_screenwidth()//2)-(400//2);
    height = (window.winfo_screenheight()//2)-(200//2);

    window.geometry("{}x{}+{}+{}".format(400,200,width,height))
    window.config(bg="#CCCCCC")


    photo = PhotoImage(file="music.gif")
    lbl = Label(window,text="Playing Song...",borderwidth=2, relief="raised",image=photo,bg="#000000")
    lbl.place(relx=0.05,rely=0.06,relheight=0.6,relwidth=0.9)

    emo = Label(window,text='emotion',borderwidth=2, relief="raised", bg="#CCCCCC",fg="#CB7234")
    emo.configure(font=("bitstream charter",24,"bold"))
    emo.place(relx=0.25,rely=0.72,relheight=0.2,relwidth=0.5)


    play_btn = Button(window, text='Play',relief="raised",bg="#CCCCCC",font=("bitstream charter",13,"bold"))
    play_btn.configure(command=play_song)
    play_btn.place(relx=0.05, rely=0.77, relwidth=0.1, relheight=0.1)

    stop = Button(window, text='Close',relief="raised",command=window.destroy,bg="#CCCCCC")
    stop.configure(font=("bitstream charter",13,"bold"))
    stop.place(relx=0.85, rely=0.77, relwidth=0.1, relheight=0.1)

    window.mainloop()

open_player()    
