from argparse import FileType
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from numpy import size
from stegano import lsb 

root=Tk()
root.title("Steganography - Kelas Teori dan Praktikum D")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#5eb8db")

def showimage():
	global filename
	global img
	global cek
	filename=filedialog.askopenfilename(initialdir=os.getcwd(),
							title='Select Image File',
							filetype=(("PNG file","*.png"),
									("JPG File","*.jpg"),("All file","*.txt")))
	img=Image.open(filename)
	img=ImageTk.PhotoImage(img)
	lbl.configure(image=img,width=250,height=250)
	lbl.image=img
	cek = os.stat(filename).st_size
def Hide():
	global secret
	massage=text1.get(1.0,END)
	secret = lsb.hide(str(filename), massage)


def Show():
	clear_massage = lsb.reveal(filename)
	text1.delete(1.0, END)
	text1.insert(END, clear_massage)

def save():
	secret.save("hidden.png")

def onClick():
    tk.messagebox.showinfo("Info Gambar.", f'Ukuran Gambar : {cek} byte')

def onClick2():
    tk.messagebox.showinfo("Anggota Kelompok.", """
	Anggota Kelompok : 

	Dikri Hidayat                   1197050030
	Reyhan Fauzy Dahlan      1197050113
	Milda Maulida Fauziah    1197050068
	Sultan Al                1197050128 """)

def onClick3():
    tk.messagebox.showinfo("Panduan Pengguna", """
	Panduan Penggunaan: 

	1. Pertama buka gambar terlebih dahulu
	2. Selanjutnya Masukan pesan tersembunyi
	3. Lalu tekan sembunyikan
	4. Maka gambar dengan file tersembunyi
	    berhasil dibuat dengan nama hidden.png
	5. Selanjutnya buka gambar ulang, buka
	    gambar dengan nama hidden.png
	6. Lalu klik tampil, maka pesan tersembunyi akan 
	    keluar
	""")


#icon
image_icon=PhotoImage(file="logo.jpg")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="logo.png")
Label(root,image=logo,bg="#5eb8db").place(x=10,y=0)

Label(root,text="Kelompok 4 Sistem Multimedia",bg="white",fg="#2d4155",font="arial 25 bold").place(x=20,y=20)
Button(text="kelompok", width=7,height=1,font="arial 14 bold",command=onClick2).place(x=600,y=2)
Button(text="Panduan", width=7,height=1,font="arial 14 bold",command=onClick3).place(x=600,y=40)


#first Frame
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

#Second Frame
frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame
frame3=Frame(root,bd=3,bg="#5eb8db", width=330,height=100,relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3,text="Buka Gambar", width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=17)
Button(frame3,text="Save Gambar", width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=17)
Label(frame3,text="Picture, Image, Photo File", bg="#5eb8db", fg="yellow").place

#fourth frame
frame4=Frame(root,bd=3,bg="#2f4115", width=330,height=100,relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4,text="Sembunyikan", width=11,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="Tampil", width=7,height=1,font="arial 14 bold",command=Show).place(x=200,y=50)
Button(frame4,text="Info", width=7,height=1,font="arial 14 bold",command=onClick).place(x=200,y=13)
Label(frame4,text="Picture, Image, Photo File",bg="#2f4115",fg="yellow").place(x=20,y=5)








root.mainloop()