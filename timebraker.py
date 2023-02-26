from tkinter import messagebox, Label, Button, FALSE, Tk, Entry, filedialog, Canvas, Checkbutton
import tkinter as tk
import time
import os

doAgain = False
adv_sett = False


app = tk.Tk()
app.title("runtimeBreaker")
app.geometry("150x260")
app.resizable(False	, False)

def changecode():
	global doAgain
	if doAgain == False:
		doAgain = True
	elif doAgain == True:
		doAgain = False
	else:
		print("Bu işte bir sıkıntı var usta")

def show_advanced():
	global adv_sett
	if adv_sett == False:
		app.geometry("400x260")
		adv_sett = True
		sett['text'] = 'Ekstra ayarları   gizle '
	elif adv_sett == True:
		app.geometry("150x260")
		adv_sett = False
		sett['text'] = 'Ekstra ayarları göster'

def developer_info():
	try:
		messagebox.showinfo("Yapımcı bilgileri","yapımcı = r00t025 \nDiscord: 𝕾𝖔𝖚𝖑𝖋𝖑𝖞 ♡#8509")
	except:
		pass


text = Label(app,text="uygulama hata verse \n de merak etmeyin \n KOD ÇALIŞIYOR")
warntxt = Label(app,text="SADECE sayı giriniz! (saniye olarak)", fg="Red")
endtext = Label(app, text="           Uyarı gelmasi için gereken süre: \n \n \n \n \nUyarının bekleme süresi:")
timeend = Entry()
waitend = Entry()
sett = Button(app,text="Ekstra ayarları göster", command=show_advanced)
by = Label(app, text="RUNTIME \n       BREAKER",font=('Helvetica 10 bold', 18), fg="Blue")
wanex = Button(app, text="yapımcı bilgileri", font=(5,7), command=developer_info)

button_chck = Checkbutton(app, text="Tekrarla", command=changecode)


button_chck.place(x=222,y=170)
warntxt.place(x=177, y=3)
endtext.place(x=150, y=30)
timeend.place(x=200, y=50)
waitend.place(x=200, y=130)
sett.place(x=17, y=220)
text.place(x=12)
by.place(x=-20,y=100)
wanex.place(x=320, y=230)

def empty():
	time.sleep(2)
	

def mloop():
	try:
		sleeptime = int(timeend.get())
		waittime = int(waitend.get())
	except:
		sleeptime = 600
		waittime  = 900
	for kalanzaman in range(sleeptime):
		time.sleep(1)		
	os.system("shutdown -s -t " + str(waittime))
	if messagebox.askyesno("Dikkat", "Bilgisayar " + str(waittime/60) + " dakika (" + str(waittime) + " saniye) sonra kapanacak (evet' basarsanız ve tekrarlama açık ise takrar baştan başlayacak)"):
		if doAgain == True:
			os.system("shutdown -a")
			if messagebox.askyesno("Tamam", "Kapatma iptal edildi, başa sarmak için evet'e tıklayın"):	
				mloop()
			empty()
		elif doAgain == False:
			os.system("shutdown -a")	
			empty()
	os.system("shutdown -a")
	empty()


başlat = Button(app,text="Başlat",command=mloop)



başlat.place(x=50, y=50)



app.mainloop()
