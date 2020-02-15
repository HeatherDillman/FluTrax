from map_view import show_graph
import pandas as pd
from tkinter import *
from PIL import Image, ImageTk
from show_trend import show_trend
from update_info import update_info


class Window(Frame):
    def nationwide_map(self):
        show_graph(pd.read_csv('data.csv'))

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.configure(background='white')

        load = Image.open("FluTrax Logo - Small.png")
        load = load.resize((300, 350))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.configure(borderwidth=0, highlightthickness=0)
        img.place(x=150, y=30)

        button_background_color = '#5867B0'

        map_button = Button(self, text="Show Nationwide", command=self.nationwide_map)
        map_button.configure(background=button_background_color, foreground='white')
        map_button.place(x=60, y=400, width=120, height=50)

        update_button = Button(self, text='Update Data', command=update_info)
        update_button.configure(background=button_background_color, foreground='white')
        update_button.place(x=240, y=400, width=120, height=50)

        trend_button = Button(self, text='Show Trend', command=show_trend)
        trend_button.configure(background=button_background_color, foreground='white')
        trend_button.place(x=420, y=400, width=120, height=50)


def show_main_window():
    root = Tk()
    app = Window(root)
    root.wm_title("FluTrax")
    root.wm_iconbitmap('FluTrax Logo - Small.ico')
    root.resizable(False, False)
    root.geometry("600x500")
    root.configure(background='white')
    root.mainloop()


if __name__ == '__main__':
    show_main_window()
