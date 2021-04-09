from tkinter import *
from tkinter import ttk
import os
import wmi, time

def narakam():
    window.destroy()
    def guilt():
        GB = 100
        download = 0
        speed = 1
        while(download<GB):
            time.sleep(0.09)
            bar2['value']+=(speed/GB)*100
            download+=speed
            text3 = Label(window3, text="You are not forgiven\nErasing all Random files...........\nDeleting all files permanently", bg="#2A2A29", fg="red", font=('Arial 9 bold')).place(x=185,y=220)
            window3.update_idletasks()
        Label(window3, text="Era?? Bhayapaddava?? Idi Prank ey ra, ee sari evadaina\nfree ga emaina istey, install cheyaka ila pappa aipotav,\n this is just an awareness, share this to your friends", font=('Helvetica',15)).pack()

    window3 = Tk()
    window3.geometry("510x350")
    window3.title("YOUTUBE.EXE")
    window3.configure(bg="#2A2A29")

    text1 = Label(window3, text="Endi bey Extraalu chestunav??\nnenu antey bhayam leda?", font=('Helvetica 15 bold'), bg="#2A2A29", fg="gold").pack()
    text2 = Label(window3, text="Uppudu nee computer lo random locations lo data, files,\nimages, documents ni erase chestunna\nthis process is final and cannot be stopped", bg="#2A2A29", fg="red", font=('Arial 11 bold')).pack()
    button1 = Button(window3, text="Please forgive me", command=guilt, bg="red", fg='white').pack(pady=10)
    bar2 = ttk.Progressbar(window3, orient=HORIZONTAL, length=300, mode="determinate")
    bar2.pack(pady=10)

    window2.mainloop()

def vadhiley():
    window.destroy()
    def start():
        GB = 100
        download = 0
        speed = 1
        while(download<GB):
            time.sleep(0.05)
            bar1['value']+=(speed/GB)*100
            download+=speed
            text3 = Label(window2, text="Commiting suicide..........\nerasing all my files", font=('Helvetica 9 bold'), bg="#2A2A29",fg="red").place(x=185,y=260)
            window2.update_idletasks()

        Label(window2, text="Era?? Bhayapaddava?? Idi Prank ey ra, ee sari evadaina\nfree ga emaina istey, install cheyaka ila pappa aipotav,\n this is just an awareness, share this to your friends", font=('Helvetica',15)).pack()

    window2 = Tk()
    window2.geometry("510x350")
    window2.title("YOUTUBE.EXE")
    window2.configure(bg="#2A2A29")
    text1 = Label(window2, text="Nuvvu nannu request chesav, ok nee meeda jaali kalikindi,\nSarle, let me activate the antivirus ra macha", font=('Helvetica 14'), bg="#2A2A29", fg="gold").pack()
    text2 = Label(window2, text="Antivirus process initiated, please koncham tulasi neelu untey \nmee computer meeda poyandi appudu virus jil jil jiga jiga", font=('Helvetica 11 bold'), bg="#2A2A29", fg="green").pack(pady=20)
    text4 = Label(window2, text="Thanks cheppu bey mundu, attitude a?", font=('Helvetica 11 bold'), bg="#2A2A29", fg="red").pack()
    
    button3 = Button(window2, text="Thanks Virus Macha", bg="red", fg="white",command=start).pack(pady=10)
    bar1 = ttk.Progressbar(window2, orient=HORIZONTAL,length=300, mode="determinate")
    bar1.pack(pady=10)

    window2.mainloop()

def first():
    global window
    window = Tk()
    window.geometry("600x450")
    window.title("YOUTUBE.EXE")
    window.configure(bg="#2A2A29")

    c = wmi.WMI()
    my_system = c.Win32_ComputerSystem()[0]

    name = str(os.getlogin())

    text_label1 = Label(window, text = "***Successfully installed a TROJAN.ini FILE***\n***Root Access Gained***\n***All your files are in my control***", font=('Helvetica 15 bold'), bg="#2A2A29", fg="red").pack()
    text_label2 = Label(window, text="Mee computer ki virus pattindi, if you don't believe me, i can prove it\ncurrent username is '"+name+"' right?", font=('Helvetica 13 bold'), bg="#2A2A29", fg="white").pack()
    text_label3 = Label(window, text="Nee computer details kuda telusu ra naaku, let me prove it,\n you use Manufacturer: "+my_system.Manufacturer+"\nModel: "+my_system.Model+"\nName: "+my_system.Name+"\nSystemFamily: "+my_system.SystemFamily, font=('Helvetica 15 bold'),bg="#2A2A29",fg="gold").pack()
    text_label4 = Label(window, text="Nee system neeku kaavalante ee window nee close cheyaku,\n close chesina next second every file will\n be deleted I repeat again do not close this window, \nlisten to the instructions carefully",font=('Helvetica 13 bold'),bg="#2A2A29",fg="red").pack()
    text_label5 = Label(window, text="Don't worry, I'M a virus with a built-in antivirus, do you want to activate the antivirus??\nnee manasalo em feeling undo aa button meeda nokku bey", bg="#2A2A29", fg="gold").pack()
    button1 = Button(window, text="vadhiley ra macha, please ra", borderwidth=5, bg="red", fg="white", font=('arial',13),command=vadhiley).place(x=350, y=390)
    button2 = Button(window, text="nenu evariki bhayapadanu", borderwidth=5, bg="red", fg="white", font=('arial',13), command=narakam).place(x=25, y=390)
    window.mainloop()

first()