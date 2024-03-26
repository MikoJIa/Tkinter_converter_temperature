import tkinter as tk


window = tk.Tk()
window.title('Converter F to C')
window.geometry('350x100')
window.resizable(False, False)


def converter():
    foreng = int(ent.get())
    c = 5 / 9 * (foreng - 32)
    lbl_res['text'] = str(c)


frame = tk.Frame(borderwidth=5, relief=tk.SUNKEN)
frame.pack(fill=tk.BOTH)


ent = tk.Entry(master=frame, width=8, font=('Arial', 20, 'bold'))
ent.grid(row=0, column=0)

lbl_f = tk.Label(master=frame, text='\N{DEGREE FAHRENHEIT}', font='Arial 20')
lbl_f.grid(row=0, column=1)

btn = tk.Button(master=frame, text='\N{RIGHTWARDS BLACK ARROW}', width=4, height=2, font=('Arial', 15, 'bold'), command=converter)
btn.grid(row=0, column=2, pady=10)

lbl_res = tk.Label(master=frame, text='0', font='Arial 20')
lbl_res.grid(row=0, column=3, padx=10)

lbl_c = tk.Label(master=frame, text='\N{DEGREE CELSIUS}', font='Arial 20')
lbl_c.grid(row=0, column=4, sticky='en')

window.mainloop()