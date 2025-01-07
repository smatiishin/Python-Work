# Sam Matiishin
# CPT 101
# MP3 Player Program
# Description: This is a GUI program that allows for a user to play music using mp3 files from a computer


import tkinter # Import for environment
import tkinter.filedialog # Import for file parsing

import pygame # Import for mixer
from pygame import mixer # Import mixer for music

import os # Import for file parsing

# Secondary function called by the main function that loads and plays the song
def play():
    try:
        mixer.music.load(play_list.get(tkinter.ACTIVE))
        mixer.music.play()
    except:
        #Display error message
        tkinter.messagebox.showinfo('Error','No songs in queue!')

# Secondary function called by the main function that stops the music
def stop():
    mixer.music.stop()

# Secondary function called by the main function that pauses the music
def pause():
    mixer.music.pause()

# Secondary function called by the main function that resumes the music
def unpause():
    mixer.music.unpause()

# Secondary function called by the main function that allows for the user to select a
# folder in which to play mp3 files from, and appends these files and their names to the program
def loadfile():
    # Set variable to the function that opens the file directory and allow
    # for the user to select a folder containing mp3 files
    some_folder_name = tkinter.filedialog.askdirectory()
    os.chdir(some_folder_name)
    song_choices = os.listdir(some_folder_name)

    # Append the file names ending in .mp3 to the song list
    for file in song_choices:
        if file.endswith(".mp3"):
            song_list.append(file)

    # Add the song names to be displayed on the screen
    for song in song_list:
        play_list.insert(0, song)

# Secondary function called by the main function that modifies the volume of the music
def volume(position):
    volume_percent = 100
    mixer.music.set_volume(volume_adjuster.get()/volume_percent)

# Secondary function called by the main function that displays help directions
def help_user():
    tkinter.messagebox.showinfo("Directions","This program is an MP3 player: \nStep 1: Press open and select a folder containg .mp3 files\nStep 2: Click one .mp3 song from the display list\nStep 3: Use controls, as well as the volume knob on the right to listen to music. Enjoy!")



# Global values used to pass data to functions
main_window = tkinter.Tk() # Create environment for the program
song_list = [] # Initialize list for songs to be placed into
play_list = tkinter.Listbox(main_window, selectmode = tkinter.SINGLE, bg="black", fg="white", width=30) # Initialize window for songs to be displayed into
volume_adjuster = tkinter.Scale(main_window, command=volume, fg='red') # Initialize volume adjustment knob

# Primary function that executes the program
def main():
    # Rename the file
    main_window.title("myplayer")
    # Inititalize music player
    mixer.init()

    # Initalize frames to be used in the window
    top_frame = tkinter.LabelFrame(main_window, text="File Selection")
    control_frame = tkinter.LabelFrame(main_window, text="Controls")

    # Initialize label for the file selection frame
    welcome_label = tkinter.Label(top_frame, width=20, height=3, text="Select a folder:", fg="IndianRed2")
    # Initialize button that allows for the user to open a folder containing .mp3 files
    file_selector_button = tkinter.Button(top_frame, text="Open", command=loadfile, width=20)

    # Initialize play button
    play_button = tkinter.Button(control_frame, text="Play", command=play, width=5, height=1, bg='lime green', fg='plum4')
    # Initialize stop button
    stop_button = tkinter.Button(control_frame, text="Stop", command=stop, width=5, height=1, bg='IndianRed1', fg='white')
    # Initialize pause button
    pause_button = tkinter.Button(control_frame, text="Pause", command=pause, width=5, height=1, bg='aquamarine')
    # Initialize resume button
    resume_button = tkinter.Button(control_frame, text="Resume", command=unpause, width=5, height=1, bg='violet')
    # Initialize quit button
    quit_button = tkinter.Button(control_frame, text="Exit", command=main_window.destroy, width=5, height=1, bg='orange')

    # Initialize help button in the menu
    help_button = tkinter.Button(control_frame, text="Help?", command=help_user, width=5, height=1, bg='gray50')

    # Pack corresponding labels and buttons into their respective frames
    volume_adjuster.pack(side='right')
    welcome_label.pack(side='top')
    file_selector_button.pack(side='top') 
    play_button.pack(side='left', ipadx=5)
    stop_button.pack(side='left',ipadx=5)
    pause_button.pack(side='left', ipadx=5)
    resume_button.pack(side='left', ipadx=5)
    quit_button.pack(side='left', ipadx=5)
    help_button.pack(side='bottom', ipadx=5)

    # Pack each corresponding frame into the program
    top_frame.pack(side='top')
    control_frame.pack(side='left')

    # Pack the file displayer into the program
    play_list.pack()

    # Command that keeps the program running
    main_window.mainloop()
    
# Command that executes the main function
main()

    
