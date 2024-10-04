#import labrary
from tkinter import *

#this app labrary
import show_gui
import link_server
import keyboard_control


# *** change url at link_server.py ***


class naprock_ui_lourenco(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)
        
        self.title("Light Rail Data Editor") #name of window
        
        self.attributes("-fullscreen", True)
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        frame = globals()["ui_frame"]
        frame = frame(parent=container, controller=self)
        frame.config(highlightbackground="black", highlightthickness=1)
        frame.grid(row=0, column=0, sticky = "nsew")
        frame.tkraise()
        
        
class ui_frame(Frame):
    def __init__(frame_class, parent, controller): #self = frame class, parent = window frame, controller = window class
        Frame.__init__(frame_class, parent)
        
        #spwan layout
        show_gui.window_layout(frame_class)
        show_gui.info_pad(frame_class)
        show_gui.masons_pad(frame_class)
        show_gui.post_btn(frame_class)
        
        #getting data and display
        link_server.first_getting(frame_class)
        show_gui.first_update(frame_class)
        
        #setting keyboard control
        keyboard_control.set_handler(controller, frame_class)

        frame_class.after(10, lambda: link_server.get(frame_class))
        frame_class.after(10, frame_class.count_down)
        
        
    def count_down(frame_class):
        frame_class.my_turns_time -= 1
        frame_class.turns_time_label.config(text=str(frame_class.my_turns_time)+"/"+ str(frame_class.game_turns_time))
        frame_class.after(1000, frame_class.count_down)
        
        
    def board_btn_clicked(frame_class, coordinate):
        frame_class.my_selected_unit[0] = coordinate[0]
        frame_class.my_selected_unit[1] = coordinate[1]
        #print(coordinate)

    

if __name__ == "__main__":
    naprock_ui_lourenco().mainloop()