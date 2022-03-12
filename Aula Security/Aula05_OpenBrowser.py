import webbrowser
from tkinter import * # * = importar tudo

root = Tk( )# é p dizer q é NONE, não tem nada na tela
root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
root.mainloop() #abrir o programa