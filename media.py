from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('Media Player Ramji ka')
#root.iconbitmap('c:/gui/codemy.ico')

#root.geometry("500*300")

pygame.mixer.init()

def add_song():
  song = filedialog.askopenfilename(initialdir='/home/cavisson/Desktop/R_python/media/pic/', title="Choose a Song",filetypes=(("mp3 Files", "*.mp3"),))
  song = song.replace("/home/cavisson/Desktop/R_python/media/pic/","")
  song = song.replace(".mp3","")
  song_box.insert(END, song)

def add_many_songs():
  songs = filedialog.askopenfilenames(initialdir='/home/cavisson/Desktop/R_python/media/pic/', title="Choose Multiple songs",filetypes=(("mp3 Files", "*.mp3"),))
 
  print("songs........................")
  for song in songs:
    song = song.replace("/home/cavisson/Desktop/R_python/media/pic/","")
    song = song.replace(".mp3","")
    song_box.insert(END, song)
  

def play():
  song = song_box.get(ACTIVE)
  song = "/home/cavisson/Desktop/R_python/media/pic/"+song+".mp3"
  #song = f"/home/cavisson/Desktop/R_python/media/pic/"{song}".mp3")
  
  pygame.mixer.music.load(song)
  pygame.mixer.music.play(loops=0)

def stop():
  pygame.mixer.music.stop()
  song_box.selection_clear(ACTIVE)

global paused
paused = False


def pause(is_paused):
  global paused
  paused = is_paused
  
  if paused:
    pygame.mixer.music.unpause()
    paused = False
  else:
    pygame.mixer.music.pause()
    paused = True

def next_song():
  print("Nice working")
  #next_one = song_box.curselection()
  print(type(song_box.curselection()))
  print(song_box[0])


  """next_one = next_one[0]+1
  song = song_box.get(next_one)
  song = "/home/cavisson/Desktop/R_python/media/pic/"+song+".mp3"
  pygame.mixer.music.load(song)
  pygame.mixer.music.play(loops=0)
  print("End")
  """ 







song_box = Listbox(root, bg="black",fg="yellow", width=160)
song_box.pack(pady=10)


back_btn_img = PhotoImage(file='/home/cavisson/Desktop/R_python/media/pic/backward.png')
forward_btn_img = PhotoImage(file='/home/cavisson/Desktop/R_python/media/pic/forward.png')
play_btn_img = PhotoImage(file='/home/cavisson/Desktop/R_python/media/pic/play50.png')
pause_btn_img = PhotoImage(file='/home/cavisson/Desktop/R_python/media/pic/stop50.png')
stop_btn_img = PhotoImage(file='/home/cavisson/Desktop/R_python/media/pic/stoopp1.png')

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command= next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command= lambda:pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0,column=0)
forward_button.grid(row=0,column=1)
play_button.grid(row=0,column=2)
pause_button.grid(row=0,column=3)
stop_button.grid(row=0,column=4)



my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song to Playlist",command=add_song)
add_song_menu.add_command(label="Add Many Song to Playlist",command=add_many_songs)

	


root.mainloop()
