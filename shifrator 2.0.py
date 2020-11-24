from tkinter import scrolledtext
from tkinter import ttk
import tkinter as tk
import webbrowser
import random

def seed(nseed='4826493'):
    if nseed.isnumeric() == False:
        nseed = 4826493
    random.seed(int(nseed)) 
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
               'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '!', '?', '-', '(', ')',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '/', '[', ']', '']
    while letters[0] != '':
        random.shuffle(letters)
    d = {i : letters[i] for i in range(len(letters))}
    items = d.items()
    return items

def zashifr(text, items):
    shifr = ''
    for letter in text:
        for j in items:
            if letter.lower() == j[1]:
                kod = ''
                a = j[0]
                
                for i in range(10):
                    c = a/(10-i)
                    if a > 9:
                        b = round(c)
                    else: b = a
                    
                    if letter.isupper() and i==0:
                        if b%2 != 0:
                            b -= 1
                    elif letter.islower() and i==0:
                        if a > 9:
                            if b%2 == 0:
                                b +=1
                        else:
                            b=(a//2)
                            if b%2==0:
                                b+=1
                    a -= b
                    kod += str(b)

                kodrand = list(kod)[1::]
                random.shuffle(kodrand)
                
                shifr += kod[0]
                shifr += ''.join(kodrand)
                break
    return shifr

def razshifr(shifr, items):
    text = ''
    kods = []
    kod = []
    for i in range(len(shifr)):
        number = shifr[i]
        kod += [number]
        if len(kod) == 10:
            kods += [kod]
            kod = []

    for kod in kods:
        a = 0
        for i in kod:
            a += int(i)
            
        for i in items:
            if a == i[0]:
                if int(kod[0])%2 == 0:
                    text += i[1].upper()
                else:
                    text += i[1]
                break
    return text


#root

root = tk.Tk()
root["bg"] = "#fffaf2"
root.title("Шифратор")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2 
w = w - 300 - 30
h = h - 250 - 20
root.geometry('600x500+{}+{}'.format(w, h))
root.resizable(False, False)

style = ttk.Style()

style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": '#ffe0f9' },
            "map":       {"background": [("selected", '#f5ceed')],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("yummy")

tab_control = tk.ttk.Notebook(root)
ttk.Style().configure("TNotebook", background= '#f7feff')
tab1 = tk.ttk.Frame(tab_control)
tab2 = tk.ttk.Frame(tab_control)
ttk.Style().configure("TFrame", background= '#fffaf2')
tab_control.add(tab1, text='  Зашифровать  ')  
tab_control.add(tab2, text='  Расшифровать  ')

#ssilka

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

lb = tk.Label(root, text = 'Связь:', bg = "#f7feff")
lb.place(x = 400, y = 3)

lbl = tk.Label(root, text=r"https://vk.com/griffin_john", bg = "#f7feff", fg="#d05f8b", cursor="hand2")
lbl.place(x = 440, y = 3)
lbl.bind("<Button-1>", callback)

#seed

def clicked_seed():
    lb_seed.configure(text = vvod_seed.get())
    if lb_seed['text'].isnumeric():
        if len(lb_seed['text']) > 9:
            lb_seed['text'] = '999999999'
        elif lb_seed['text'] == '666':
            lb_seed.configure(bg='Black', fg='red')
        else:
            lb_seed.configure(bg='#f7feff', fg='black')
    else:
        clicked_seed_umolch()

def clicked_seed_umolch():
    lb_seed.configure(text = "???")
    lb_seed.configure(bg='#f7feff', fg='black')
    vvod_seed.delete(0, tk.END)
        
lb_seed = tk.Label(root, font=("Arial bold", 15), text="???", bg='#f7feff', fg='black')
lb_seed.place(x = 478, y = 34, width = 110, height = 40)

btn_seed = tk.Button(root, font=("Arial bold", 15), text="Установить сид", bg="black", fg="#b1f2f2", cursor="hand2",
                     activebackground = 'black', activeforeground = '#83ebeb', command=clicked_seed)
btn_seed.place(x = 128, y = 34, width = 170, height = 40)

btn_seed_umolch = tk.Button(root, font=("Arial bold", 15), text="По умолчанию", bg="black", fg="#b1f2f2", cursor="hand2",
                            activebackground = 'black', activeforeground = '#83ebeb', command=clicked_seed_umolch)
btn_seed_umolch.place(x = 308, y = 34, width = 160, height = 40)

vvod_seed = tk.Entry(root, font=("Arial bold", 15), justify = tk.CENTER, bg = '#f7feff', fg = 'black')
vvod_seed.place(x = 8, y = 34, width = 110, height = 40)

#zashifr

def clicked_zashifr():
    nseed = lb_seed['text']
    text = zashifr(txt_zashifr.get(1.0, tk.END), seed(nseed))
    txt_zashifr.delete(1.0, tk.END)
    text = razshifr(text, seed(nseed*10))
    root.clipboard_clear()
    root.clipboard_append(text)

txt_zashifr = scrolledtext.ScrolledText(tab1, font=("Arial Bold", 14), bg = '#f7ffff', fg = 'black', selectbackground = '#ffc080', selectforeground = 'black', wrap = tk.WORD)  
txt_zashifr.place(x = 7, y = 130, width = 590, height = 325)
txt_zashifr.focus()

btn_zashifr = tk.Button(tab1, font=("Arial bold", 15), text="Зашифровать и скопировать в буфер обмена", bg="black", fg="#f5a2e4", cursor="hand2",
                        activebackground = 'black', activeforeground = '#e87bd2', command=clicked_zashifr)
btn_zashifr.place(x = 77, y = 80, width = 440, height = 40)

#razshifr

def clicked_razshifr():
    nseed = lb_seed['text']
    text = zashifr(root.clipboard_get(), seed(nseed*10))
    text = razshifr(text, seed(nseed))
    txt_razshifr.delete(1.0, tk.END)
    txt_razshifr.insert(tk.INSERT, text)

txt_razshifr = scrolledtext.ScrolledText(tab2, font=("Arial Bold", 14), bg = '#f7ffff', fg = 'black', selectbackground = '#ffc080', selectforeground = 'black', wrap = tk.WORD)   
txt_razshifr.place(x = 7, y = 130, width = 590, height = 325)
txt_razshifr.focus()

btn_razshifr = tk.Button(tab2, font=("Arial bold", 15), text="Расшифровать текст из буфера обмена", bg="black", fg="#f5a2e4", cursor="hand2",
                        activebackground = 'black', activeforeground = '#e87bd2', command=clicked_razshifr)
btn_razshifr.place(x = 77, y = 80, width = 440, height = 40)

#The end

tab_control.pack(expand=1, fill='both')
root.mainloop()





