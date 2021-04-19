from Zoom import MainWindow
from ZoomAlt import Zoom
from ROI import getRoi
import easygui
import unicodedata
import tkinter as tk

uni_img = easygui.fileopenbox()
filepath = unicodedata.normalize('NFKD', uni_img).encode('ascii','ignore')
filepath = filepath.decode('utf-8')

app = Zoom(tk.Tk(), filepath)
app.mainloop()

