import os
import sys
import ctypes
import flet as ft
from interfaz import construir_interfaz

# Uso de icono personalizado en la barra de tareas:
myappid = 'lanumero1.reporteswhatsapp.generador.1.4'
try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass

if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

icons_dir = os.path.join(base_dir, "icons")

if __name__ == "__main__":
    ft.app(target=construir_interfaz, assets_dir=icons_dir)