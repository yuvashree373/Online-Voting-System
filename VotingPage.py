import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "DMK\n\nStalin", variable = vote, value = "dmk", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"dmk",client_socket)).grid(row = 2,column = 1)
    dmkLogo = ImageTk.PhotoImage((Image.open("img/dmk.png")).resize((45,45),Image.ANTIALIAS))
    dmkImg = Label(frame1, image=dmkLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "AIADMK\n\nPalaniswamy", variable = vote, value = "aiadmk", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"aiadmk",client_socket)).grid(row = 3,column = 1)
    aiadmkLogo = ImageTk.PhotoImage((Image.open("img/aiadmk.png")).resize((35,48),Image.ANTIALIAS))
    aiadmkImg = Label(frame1, image=aiadmkLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "BJP\n\nAnnamalai", variable = vote, value = "bjp", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"bjp",client_socket) ).grid(row = 4,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((55,40),Image.ANTIALIAS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "CONG\n\nAlagiri", variable = vote, value = "cong", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"cong",client_socket)).grid(row = 5,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/cong.png")).resize((50,45),Image.ANTIALIAS))
    congImg = Label(frame1, image=congLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nNOTA    \n  ", variable = vote, value = "nota", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"nota",client_socket)).grid(row = 6,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.png")).resize((45,35),Image.ANTIALIAS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
