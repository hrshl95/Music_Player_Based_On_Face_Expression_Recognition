
import sys
import os

from tkinter import *
from PIL import ImageTk,Image,ImageSequence

import simpleaudio as sa

from os import listdir
from os.path import isfile, join

import random

import webbrowser

id = None

BACKGND_COLOR = '#0048AC'
BUTTON_COLOR = '#014bb0'


def open_player(expression):

    play_obj = None

    BASE_DIR = os.path.abspath('songs')
    path = BASE_DIR+'/{}/'.format(expression)

    songfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(songfiles)

    def play_song(song, stat):
        global play_obj

        if stat:
            wave_obj = sa.WaveObject.from_wave_file("songs/{}/{}".format(expression,song))

            play_obj = wave_obj.play()

        else:

            play_obj.stop()


    def animate(counter):
        global id
        canvas.itemconfig(image,image=sequence[counter])
        if not animating:
            return
        id = player_base.after(100, lambda: animate((counter+1)%len(sequence)))

    def play_game():
        animate(0)
        play_song(songfiles[0], True)


    global id

    player_base = Tk()
    player_base.title('Expression Music Player')
    player_base.geometry("700x500")
    player_base.config(bg=BACKGND_COLOR)

    canvas = Canvas(player_base)
    canvas.place(relx=0,rely=0,relwidth=0.7,relheight=0.8)

    sequence = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                        Image.open("anim_2.gif")
                        )]

    image = canvas.create_image(270,200,image=sequence[0]) #270,200
    animating = True


    control_panel = Frame(player_base,bg=BACKGND_COLOR,bd=1,relief='groove')
    control_panel.place(relx=0,rely=0.8,relheight=0.2,relwidth=0.7)

    play_btn = Button(control_panel, text='Play',relief="raised",bg=BUTTON_COLOR,font=("bitstream charter",13,"bold"))
    play_btn.configure(command=play_game)
    play_btn.place(relx=0.05, rely=0.3, relwidth=0.15, relheight=0.4)

    stop = Button(control_panel, text='Close',relief="raised",bg=BUTTON_COLOR)
    stop.configure(font=("bitstream charter",13,"bold"))
    stop.place(relx=0.80, rely=0.3, relwidth=0.15, relheight=0.4)
    stop.configure(command = lambda : [play_song(songfiles[0], False), player_base.destroy()] ) #player_base.after_cancel(id),


    # -------------------------
    #
    path_ = "C:\\Users\\admin\\Desktop\\Face_Recognition v2\\src\\emojis\\{}.gif".format(expression)

    emoji_frame= Frame(player_base,bg=BACKGND_COLOR,bd=1,relief='groove')
    emoji_frame.place(relx=0.7,rely=0,relheight=0.4,relwidth=0.3)

    create_image = Image.open(path_)
    back_image = ImageTk.PhotoImage(create_image)

    expression_emoji = Label(emoji_frame, image=back_image)
    expression_emoji.place(relx=0,rely=0,relheight=1,relwidth=1)

    songlist_panel = Frame(player_base,bg=BACKGND_COLOR,bd=1,relief='groove')
    songlist_panel.place(relx=0.7,rely=0.4,relheight=0.5,relwidth=0.3)


    list_title = Label(songlist_panel,text='Playlist',bg='black',fg='white',relief='raised')
    list_title.place(relx=0,rely=0,relwidth=1,relheight=0.15)


    y = 0.15

    for i in songfiles:

        song = Label(songlist_panel,text=i,bg=BACKGND_COLOR,fg='black',bd=1,relief='groove',anchor='w',padx=10)
        song.place(relx=0,rely=y,relwidth=1,relheight=0.1)
        y+=0.1


    def open_link(expression):

        url = " "

        if expression == 'Happy':
            url = 'https://9gag.com/funny'

        if expression == 'Sad':
            url = "https://9gag.com/savage"

        if expression == 'Surprise':
            url = "https://9gag.com/wtf"

        if expression == 'Angry':
            url = "https://9gag.com/satisfying"

        webbrowser.open_new(url)



    web_btn = Button(player_base, text='Try this!',relief="raised",bg=BUTTON_COLOR,font=("bitstream charter",13,"bold"))
    web_btn.configure(command= lambda: open_link(expression))
    web_btn.place(relx=0.7, rely=0.9, relwidth=0.3, relheight=0.1)


    player_base.mainloop()


# open_player('Happy')
