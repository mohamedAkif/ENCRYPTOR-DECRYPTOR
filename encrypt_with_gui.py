import tkinter
from tkinter import *
import random

def choose_en_method():                                       #to choose the encryption method

    if var.get()==1:

        encrypt_single_key()

    elif var.get()==2:
        encrypt_poly_key()
    elif var.get()==3:
        encrypt_random_key()

def choose_de_method():
    if var.get()==1:
        decrypt_single_key()
    elif var.get()==2:
        decrypt_poly_key()
    elif var.get()==3:
        decrypt_random_key()


def encrypt_single_key():
    msg= str(en_msg.get())
    msg=msg.upper()
    key=int(en_key.get())
    cipher=""

    for x in range(len(msg)):
        if msg[x] not in [" ",":",",",".","'","!","@","#","$","%","&","*","(",")"]:
            n=ord(msg[x])+key
            if n>90:                               # A is 65 and Z is 90 for calulations
                n=n-26

            cipher+=chr(n)
        else:
            cipher+=msg[x]

    result_text.delete('1.0',END)
    result_text.insert(INSERT,cipher)


def decrypt_single_key():
    msg=str(de_msg.get())

    key=int(de_key.get())
    decipher=""
    for x in range(len(msg)):
        if msg[x] not in [" ",":",",",".","'","!","@","#","$","%","&","*","(",")"]:
            n=ord(msg[x])-key
            if n<65 and n>57:
                n+=26

            decipher+=chr(n)


        else:
            decipher+=msg[x]
    result_text.delete('1.0',END)
    result_text.insert(INSERT,decipher)



def encrypt_poly_key():
    msg=str(en_msg.get())
    msg=msg.upper()
    key=str(en_key.get())
    key=key.upper()
    cipher=""
    y=0
    for x in range(len(msg)):
        if msg[x] not in [" ",":",",",".","'","!","@","#","$","%","&","*","(",")"]:
            if y>(len(key)-1):
                y=0
            n=ord(msg[x])+ord(key[y])-64


            if n>90:
                n-=26
            cipher+=chr(n)
            y+=1
        else:
            cipher+=msg[x]
    result_text.delete('1.0',END)
    result_text.insert(INSERT,cipher)



def decrypt_poly_key():
    msg=str(de_msg.get())
    key=str(de_key.get())
    key=key.upper()
    decipher=" "
    y=0
    for x in range(len(msg)):
        if msg[x] not in [" ",":",",",".","'","!","@","#","$","%","&","*","(",")"]:
            if y>(len(key)-1):
                y=0
            n=ord(msg[x])-ord(key[y])+64

            if n<65:
                n+=26

            decipher+=chr(n)
            y+=1
        else:
            decipher+=msg[x]

    result_text.delete('1.0',END)
    result_text.insert(INSERT,decipher)



def encrypt_random_key():
    msg = str(en_msg.get())
    msg = msg.upper()
    key=[]
    rand_key=0
    cipher = ""

    for x in range(len(msg)):
        if msg[x] not in [" ", ":", ",", ".", "'", "!", "@", "#", "$", "%", "&", "*", "(", ")"]:
            rand_key=random.randint(1,26)
            n=ord(msg[x])+rand_key

            if n>90:
                n-=26
            cipher+=chr(n)
            key.append(str(rand_key))
        else:
            cipher+=msg[x]
    result_text.delete('1.0',END)
    result_text.insert(INSERT,cipher)
    en_key.set(key)




def decrypt_random_key():
    msg = str(de_msg.get())
    key = str(de_key.get())
    key_list=list(key.split(" "))
    decipher = " "
    y=0

    for x in range(len(msg)):
        if msg[x] not in [" ", ":", ",", ".", "'", "!", "@", "#", "$", "%", "&", "*", "(", ")"]:

            n=ord(msg[x])-int(key_list[y])
            y+=1
            if n<65:
                n+=26
            decipher+=chr(n)
        else:
            decipher+=msg[x]
    result_text.delete('1.0',END)
    result_text.insert(INSERT,decipher)




window=tkinter.Tk()
window.resizable(0,0)
window.title("shift encryptor : by mohamed akif")

var=IntVar()
en_key=StringVar()
en_msg=StringVar()
de_key=StringVar()
de_msg=StringVar()

en_key.set("")
en_msg.set("")
de_key.set("")
de_msg.set("")


en_label=Label(window,text="Enter the message to encrypt : ").grid(row=0, column=0)
en_entry=Entry(window,textvariable=en_msg,font=('ariel',10)).grid(row=1,column=0)
key_label=Label(window,text="Key :").grid(row=2,column=0)
key_entry=Entry(window,textvariable=en_key,width=15,font=('ariel',10)).grid(row=3,column=0,)

en_button=Button(window,text="ENCRYPT", bd=1,command=lambda :choose_en_method()).grid(row=4,column=0)


de_label=Label(window,text="Enter the cipher :").grid(row=0,column=1,ipadx=10)
de_entry=Entry(window,textvariable=de_msg,width=25,font=('ariel',10)).grid(row=1,column=1)
de_key_label=Label(window,text="Key :").grid(row=2,column=1)
de_key_entry=Entry(window,textvariable=de_key,width=15,font=('ariel',10)).grid(row=3,column=1)
de_button=Button(window,text="DECRYPT",bd=1,command=lambda:choose_de_method()).grid(row=4,column=1)

R1=Radiobutton(window,text="MONO SHIFT (Enter a num btw 1-26 for key)",variable=var,value=1).grid(row=5)
var.set(1)
R2=Radiobutton(window,text="POLYALPHA SHIFT (Enter a word for key)",variable=var,value=2).grid(row=6)
R3=Radiobutton(window,text="RANDOM SHIFT (key is randomly generated)",variable=var,value=3).grid(row=5,column=1)

result_text=Text(window,width=45,height=10,font=('ariel',12))
result_text.grid(row=7,column=0,columnspan=2)



window.mainloop()
