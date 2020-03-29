
import final
import songPlay

while True:
    emotion = final.try_main()
    songPlay.open_player(songPlay.window,emotion)
