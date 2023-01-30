from customtkinter_import import Frame, Button, Label, Entry, CheckBox, ComboBox, Slider, TabView, Switch, ScrollBar, customtk, InputDialog
from time import sleep
from datetime import datetime
from threading import Thread
from win10toast import ToastNotifier
from tkinter import messagebox

#customtk.set_appearance_mode("Dark")
class Reloj(customtk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Reloj")
        #self.geometry("570x200")
        
        self.notificacion = ToastNotifier()
        self.aparicion = 0
        self.check = 0
        def aparicion():
            if self.aparicion == 0:
                self.hour = 1
                self.mins = 1
                self.sec = 59
                self.notificacion.show_toast("Tiempo finalizado.", f"El tiempo ha finalizado.\nAparicion de la mina en {self.hour}Hora {self.mins}Minutos con {self.sec}Segundos", duration=10, threaded=True)
                while self.check == 2:
                    if self.sec == 0:
                        if self.sec == 0 and self.hour or self.mins != 0:
                            self.sec = 60
                        if self.mins != 0:
                            self.mins -= 1
                        if self.mins == 0 and self.hour >= 1:
                            self.hour -= 1
                            self.mins = 59
                        if self.mins == 0 and self.hour == 1:
                            self.hour = 0
                            self.mins = 59
                    if self.sec == 0 and self.mins == 0 and self.hour == 0:
                        self.check = 0
                        self.notificacion.show_toast("Aparición de mina", f"Tu mina ha aparecido en el:\n{self.piso.get()}\nColor: {self.color.get()}\nUbicación: {self.ubicacion.get()}", duration=10, threaded=True)
                        print(f"Tu mina ha aparecido en el:\n{self.piso.get()}\nColor: {self.color.get()}\nUbicación: {self.ubicacion.get()}")
                        enable()
                        break
                    self.sec -= 1
                    self.aparicionLabel.configure(text=f"Aparicion\n{self.hour}h:{self.mins}m:{self.sec}s")
                    sleep(1)
        def realTime():
            self.actualTime = datetime.now().strftime("%H:%M:%S")
            self.actualSec = str(self.actualTime)[6:]
            self.actualMin = str(self.actualTime)[3:-3]
            self.actualHour = str(self.actualTime)[:-6]
            #self.timeLabel.after(1, time)
        def time():
            if self.hourEntry.get() == "":
                self.hourEntry.delete(0, "end")
                self.hourEntry.insert(0, 00)
            if self.minsEntry.get() == "":
                self.minsEntry.delete(0, "end")
                self.minsEntry.insert(0, 00)
            if self.secEntry.get() == "":
                self.secEntry.delete(0, "end")
                self.secEntry.insert(0, 00)
            if self.hourEntry.get() != "" or self.minsEntry.get() != "" or self.secEntry.get() != "":
                if self.piso.get() != "" and self.color.get() != "" and self.ubicacion.get() != "":
                    self.check = 1
                    self.hour = int(self.hourEntry.get())
                    self.mins = int(self.minsEntry.get())
                    self.sec = int(self.secEntry.get())
            #if self.hourEntry.get() == "" and self.minsEntry.get() == "" and self.secEntry.get() == "":
            #    messagebox.showinfo(title="Vacio", message="Los espacios 'Piso', 'Color: Mina' y 'Ubicacion'\nNo pueden estar Vacios.")
            if self.check == 2: pass
            elif self.check == 1:
                self.aparicion = 1
                disable()
                while self.check == 1:
                    if self.hour == 0:
                        if self.mins == 0:
                            if self.sec == 0:
                                self.check = 2
                                self.aparicion -= 1
                                self.timeLabel.configure(text="00h:00m:00s")
                                aparicion()
                                break
                    if self.sec == 0:
                        if self.sec == 0 and self.hour or self.mins != 0:
                            self.sec = 60
                        if self.mins != 0:
                            self.mins -= 1
                        if self.mins == 0 and self.hour >= 1:
                            self.hour -= 1
                            self.mins = 59
                        if self.mins == 0 and self.hour == 1:
                            self.hour = 0
                            self.mins = 59
                    self.sec -= 1
                    if self.hour < 10 and self.mins < 10 and self.sec < 10:
                        self.timeLabel.configure(text=f"0{self.hour}h:0{self.mins}m:0{self.sec}s")
                        print("Hora Actual:", self.actualTime, " | ", f"Cronometro: 0{self.hour}h:0{self.mins}m:0{self.sec}s", " | ", f"Aparicion: 0{self.aparicion + self.hour}h:0{self.mins}m", end="\r")
                    elif self.hour < 10 and self.mins < 10 and self.sec > 9:
                        self.timeLabel.configure(text=f"0{self.hour}h:0{self.mins}m:{self.sec}s")
                        print("Hora Actual:", self.actualTime, " | ", f"Cronometro: 0{self.hour}h:0{self.mins}m:{self.sec}s", " | ", f"Aparicion: 0{self.aparicion + self.hour}h:0{self.mins}m", end="\r")
                    elif self.hour < 10 and self.mins > 9 and self.sec > 9:
                        self.timeLabel.configure(text=f"0{self.hour}h:{self.mins}m:{self.sec}s")
                        print("Hora Actual:", self.actualTime, " | ", f"Cronometro: 0{self.hour}h:{self.mins}m:{self.sec}s", " | ", f"Aparicion: 0{self.aparicion + self.hour}h:{self.mins}m", end="\r")
                    elif self.hour < 10 and self.mins > 9 and self.sec < 10:
                        self.timeLabel.configure(text=f"0{self.hour}h:{self.mins}m:0{self.sec}s")
                        print("Hora Actual:", self.actualTime, " | ", f"Cronometro: 0{self.hour}h:{self.mins}m:0{self.sec}s", " | ", f"Aparicion: 0{self.aparicion + self.hour}h:{self.mins}m", end="\r")
                    elif self.hour > 9 and self.mins < 10 and self.sec > 9:
                        self.timeLabel.configure(text=f"{self.hour}h:0{self.mins}m:{self.sec}s")
                        print("Hora Actual:", self.actualTime, " | ", f"Cronometro: {self.hour}h:0{self.mins}m:{self.sec}s", " | ", f"Aparicion: {self.aparicion + self.hour}h:0{self.mins}m", end="\r")
                    elif self.hour > 9 and self.mins < 10 and self.sec < 10:
                        self.timeLabel.configure(text=f"{self.hour}h:0{self.mins}m:0{self.sec}s")
                        print("Hora Actual:", self.actualTime, " | ", f"Cronometro: {self.hour}h:0{self.mins}m:0{self.sec}s", " | ", f"Aparicion: {self.aparicion + self.hour}h:0{self.mins}m", end="\r")
                    else:
                        self.timeLabel.configure(text=f"{self.hour}h:{self.mins}m:{self.sec}s")
                        print("Hora Actual:", self.actualTime, " | ", f"Cronometro: {self.hour}h:{self.mins}m:{self.sec}s", " | ", f"Aparicion: {self.aparicion + self.hour}h:{self.mins}m", end="\r")
                    sleep(1)
                    continue
        def stop():
            self.check = 0
            print("Pausado...")
            enable()
        def clear():
            print("Clear Time")
            self.check = 0
            self.hour = 0
            self.mins = 0
            self.sec = 0
            self.aparicionLabel.configure(text="Aparicion")
            self.hourEntry.delete(0, "end")
            self.hourEntry.configure(placeholder_text="Hour")
            self.minsEntry.delete(0, "end")
            self.minsEntry.configure(placeholder_text="Mins")
            self.secEntry.delete(0, "end")
            self.secEntry.configure(placeholder_text="Sec")
        def exit():
            clear()
            self.destroy()
        def enable():
            self.hourEntry.configure(state="normal")
            self.minsEntry.configure(state="normal")
            self.secEntry.configure(state="normal")
        def disable():
            self.hourEntry.configure(state="disable")
            self.minsEntry.configure(state="disable")
            self.secEntry.configure(state="disable")
            
        self.frame = Frame(self, bg_color="transparent")
        self.hora = Label(self.frame, text="Hora")
        self.minuto = Label(self.frame, text="Minuto")
        self.segundos = Label(self.frame, text="Segundos")
        self.piso = ComboBox(self.frame, state="readonly", values=["Piso 1", "Piso 2", "Piso 3", "Piso 4"], width=80)
        self.color = ComboBox(self.frame, state="readonly", values=["Roja", "Amarilla"], width=90)
        self.ubicacion = ComboBox(self.frame, state="readonly", values=["Cantera", "Borde"], width=90)
        
        self.hourEntry = Entry(self.frame, justify="center", width=50)
        self.minsEntry = Entry(self.frame, justify="center", width=50)
        self.secEntry = Entry(self.frame, justify="center", width=50)
        self.timeLabel = Label(self.frame, text="00h:00m:00s", font=("calibri", 40, "bold"))
        self.aparicionLabel = Label(self.frame, text=f"Aparicion")
        
        self.startButton = Button(self.frame, text="Iniciar", width=50, command=lambda: Thread(target=time).start())
        self.stopButton = Button(self.frame, text="Stop", width=50, command=stop)
        self.clearButton = Button(self.frame, text="Clear", width=50, command=clear)
        self.exitButton = Button(self.frame, text="EXIT", fg_color="red", text_color="White", hover_color="Gray", width=50, command=exit)
        
        self.frame.pack(fill="both", expand=True)
        self.hora.grid(row=0, column=0, padx=(20, 0))
        self.minuto.grid(row=0, column=1)
        self.segundos.grid(row=0, column=2)
        self.piso.grid(row=0, column=3)
        self.color.grid(row=0, column=4)
        self.ubicacion.grid(row=0, column=5)
        self.aparicionLabel.grid(row=0, column=6)
        self.piso.place_configure(x=185)
        self.color.place_configure(x=270)
        self.ubicacion.place_configure(x=365)
        self.aparicionLabel.place_configure(x=490)
        
        self.hourEntry.grid(row=1, column=0, padx=(20, 3), pady=5)
        self.minsEntry.grid(row=1, column=1, pady=5)
        self.secEntry.grid(row=1, column=2, pady=5)
        self.timeLabel.grid(row=1, column=3, padx=(5, 5))
        
        self.startButton.grid(row=1, column=4, padx=(0, 5))
        self.stopButton.grid(row=1, column=5, padx=(0, 5))
        self.clearButton.grid(row=1, column=6)
        self.exitButton.grid(row=2, column=3)

if __name__ == "__main__":
    rj = Reloj()
    rj.mainloop()