import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def resetAll(root,frame1):
    #df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    dmkLogo = ImageTk.PhotoImage((Image.open("img/dmk.png")).resize((35,35),Image.ANTIALIAS))
    dmkImg = Label(frame1, image=dmkLogo).grid(row = 2,column = 0)

    aiadmkLogo = ImageTk.PhotoImage((Image.open("img/aiadmk.png")).resize((25,38),Image.ANTIALIAS))
    aiadmkImg = Label(frame1, image=aiadmkLogo).grid(row = 3,column = 0)

    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((45,30),Image.ANTIALIAS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 4,column = 0)

    congLogo = ImageTk.PhotoImage((Image.open("img/cong.png")).resize((40,35),Image.ANTIALIAS))
    congImg = Label(frame1, image=congLogo).grid(row = 5,column = 0)

    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.png")).resize((35,25),Image.ANTIALIAS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)


    a=Label(frame1, text=" DMK             :          ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    b=Label(frame1, text=result['dmk'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    c=Label(frame1, text=" AIADMK          :          ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    d=Label(frame1, text=result['aiadmk'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    e=Label(frame1, text=" BJP             :          ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    f=Label(frame1, text=result['bjp'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    g=Label(frame1, text=" CONG            :          ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    h=Label(frame1, text=result['cong'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    i=Label(frame1, text=" NOTA            :          ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    j=Label(frame1, text=result['nota'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         showVotes(root,frame1)
