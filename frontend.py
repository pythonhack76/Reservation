from tkinter import *

window=Tk()

label1=Label(window,text="Hotel")
label1.grid(row=0, column=0)

label2=Label(window,text="Nome")
label2.grid(row=1, column=0)

label3=Label(window,text="indirizzo")
label3.grid(row=2, column=0)

label4=Label(window,text="Telefono")
label4.grid(row=3, column=0)

label5=Label(window,text="Giorni soggiorno:")
label5.grid(row=4, column=0)

label1=Label(window,text="Tipo Stanza(Normale, King, Deluxe) :")
label1.grid(row=5, column=0)

label1=Label(window,text="Totale Spesa")
label1.grid(row=6, column=0)






window.mainloop()
