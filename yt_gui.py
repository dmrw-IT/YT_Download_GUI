import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import os

def dir_search(set_dir):
    cur_dir = os.getcwd()
    ask_dir = filedialog.askdirectory(parent=root, initialdir=cur_dir)
    return set_dir.set(ask_dir)
    

### initialize the app:
root = tk.Tk()

### set the title: 
root.title("YT_Download_GUI")

### set app height and width:
app_w, app_h = 500, 700
fg_color = "#494949" # dark grey
accent_color = "#e11b1b" # custom red/orange
bg_color = "white"
#root.geometry(f"{app_w}x{app_h}")
# center the app on the screen:
root.eval("tk::PlaceWindow . center")

### create main_frame:
main_frame = tk.Frame(root, width=app_w, height=app_h, bg=bg_color )
main_frame.grid(row=0, column=0)
main_frame.pack_propagate(False)

### main_frame widgets:

# load logo image:
logo_img = ImageTk.PhotoImage(file="assets/logo.png")
# create logo widget:
logo_widget = tk.Label(main_frame, image=logo_img, bg=bg_color)
logo_widget.image = logo_img # necessary despite being redundant...
logo_widget.pack()

# first text prompt: 'Choose type of download: Select 1:'
dl_prompt = tk.Label(
    main_frame,
    text="Choose download type (Select One):",
    bg=bg_color,
    fg=fg_color,
    font=("TkMenuFont, 12")
)

### radio buttons for above text:

# video radio button:
video_rb = tk.Radiobutton(
    main_frame,
    text="Video",
    bg=bg_color,
    fg=fg_color
)

# playlist radio button:
playlist_rb = tk.Radiobutton(
    main_frame,
    text="Playlist",
    bg=bg_color,
    fg=fg_color
)

# second text prompt: 'Enter YouTube URL:'
url_prompt = tk.Label(
    main_frame,
    text="Enter YouTube URL:",
    bg=bg_color,
    fg=fg_color,
    font=("TkMenuFont, 12")
)

# Entry widget for text above:
url_entry = tk.Entry(
    main_frame,
    bg=bg_color,
    fg=fg_color

)

# second text prompt: 'Enter YouTube URL:'
outputdir_prompt = tk.Label(
    main_frame,
    text="Select a directory for downloads:",
    bg=bg_color,
    fg=fg_color,
    font=("TkMenuFont, 12")
)

# Entry widget for text above:
dir_sv = tk.StringVar()
dir_entry = tk.Entry(
    main_frame,
    textvariable=dir_sv,
    bg=bg_color,
    fg=fg_color,
    width=40,
    bd=2
)

browse_btn = tk.Button(
    main_frame,
    text="Browse",
    width=6,
    command=lambda:dir_search(dir_sv)
)

dl_prompt.pack()
video_rb.pack()
playlist_rb.pack()
url_prompt.pack()
url_entry.pack()
outputdir_prompt.pack()
dir_entry.pack(side=tk.LEFT, padx=2)
browse_btn.pack(side=tk.LEFT)

### run the app:
root.mainloop()

