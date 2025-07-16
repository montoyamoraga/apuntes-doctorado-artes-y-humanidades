# importar modulos
from tkinter import Tk
from tkinter import ttk

# constantes
PADDING = 10
TITULO = "administrador de traiciones"

# crear ventana
root = Tk()

# crear frame
frame = ttk.Frame(root, padding=PADDING)

# hacer grilla
frame.grid()

root.title(TITULO)

ttk.Label(frame,
          text="Hello World!",
          padding=PADDING).grid(
    column=0,
    row=0)

ttk.Button(
    frame,
    text="Inicio",
    command=root.destroy,
    padding=PADDING).grid(
        column=1, row=0)

ttk.Button(
    frame,
    text="Navegar",
    command=root.destroy,
    padding=PADDING).grid(
    column=2, row=0)

ttk.Button(
    frame,
    text="Editar",
    command=root.destroy,
    padding=PADDING).grid(
    column=3, row=0)

ttk.Button(
    frame,
    text="Ayuda",
    command=root.destroy,
    padding=PADDING).grid(
    column=4, row=0)

ttk.Button(
    frame,
    text="Salir",
    command=root.destroy,
    padding=PADDING
    ).grid(
        column=5, row=0
)

ttk.Entry(
    frame,
    text="Escribe algo"
    ).grid(
    column=0,
    row=1,
    columnspan=6
)

root.mainloop()
