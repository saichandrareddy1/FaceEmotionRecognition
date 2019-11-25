from tkinter import *
from value_count import value_count
from tkinter import messagebox

def GUI_Confidence(result):
    window = Tk()
    window.geometry("500x60")
    window.title("Confidence_checker")
    def exited():
        
        messagebox.showinfo("EXIT", "Thanks Sir, Have a Great Day")
        exit()

    label = Label(window, text = result, bg="white", relief = 'solid',
                  width=90, font=("arial", 12, "bold")).pack()

    b1 = Button(window, text="exit", width=12, bg="brown", fg="white", command=exited).pack()

    
    window.mainloop()
