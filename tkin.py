from tkinter import Tk, filedialog

def direccion() -> str:
    ventana = Tk()
    ventana.withdraw()

    ruta = filedialog.askdirectory(title="Selleciona la carpeta que desea ordenar.")

    return ruta