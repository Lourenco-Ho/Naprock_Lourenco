#import labrary
from tkinter import *
import re
import numpy as np

#this app labrary
import show_gui
import link_server
import keyboard_control
import Astar


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
        selected_masons = -1
        for key_name in frame_class.move_key_isPressed:
            if frame_class.move_key_isPressed[key_name]:
                selected_masons = int(re.findall(r"_(\d)", key_name)[0])
                print(selected_masons)
                break

        if selected_masons != -1:
            start_coor = (frame_class.my_masons[selected_masons-1]["coor"][0], frame_class.my_masons[selected_masons-1]["coor"][1])
            dest_coor = (coordinate[0], coordinate[1])
            graph = Astar.spawn_graph(frame_class)
            path = Astar.a_star(start_coor, dest_coor, graph)
            print(path)
            
    def update_my_masons(frame_class):
        #mark down my masons
        for row_index, row_data in enumerate(frame_class.board_masons):
            for column_index, column_data in enumerate(row_data):
                if column_data > 0:
                    frame_class.my_masons[column_data-1]["coor"] [0] = column_index
                    frame_class.my_masons[column_data-1]["coor"] [1] = row_index
    

if __name__ == "__main__":
    naprock_ui_lourenco().mainloop()