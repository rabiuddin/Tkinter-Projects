from tkinter import *
from PIL import ImageTk, Image
from pytube import YouTube
from tkinter import filedialog
from tkinter import messagebox


def download():
    try:
        folder_path = filedialog.askdirectory(initialdir="~/Desktop", title="Select a folder")
        yd = yt.streams.get_highest_resolution()
        yd.download(folder_path)
        my_label = Label(root, text="Done!!", pady=15, background="#FFFFFF", font=(20))
        my_label.grid(row=6, column=0, columnspan=2)       

    except Exception as e:
        message_box = messagebox.ERROR

def click():
    link = link_e.get()

    global yt 
    yt = YouTube(link)

    name = Label(root, text="Name: " + yt.title, background="#FFFFFF")
    name.grid(row=3, column=0, columnspan=2)
    view = Label(root, text="Views: " + str(yt.views), background="#FFFFFF")
    view.grid(row=4, column=0, columnspan=2)
    download_btn = Button(root, text="Download", command=download)
    download_btn.grid(row=5, column=0, columnspan=2, pady=20)
    


root = Tk()
root.title("Frame")
root.iconbitmap("1.jpg")
root.geometry("450x500")
root.configure(background="#FFFFFF")

YT_image = ImageTk.PhotoImage(Image.open("download.png"))
YT_label = Label(root, image=YT_image, anchor="center", justify="center")
YT_label.grid(row= 0, column=0, columnspan=2)

link_label = Label(root, text="Link: ", background="#FFFFFF")
link_label.grid(row=1, column=0)

link_e = Entry(root, width=65, border=5)
link_e.grid(row=1,column=1)

link_btn = Button(root, text="Check", command=click)
link_btn.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()
