#import labrary
from tkinter import *
import random
from datetime import datetime
import sys
import os
import sqlite3
import re
import hashlib
import json
import requests
import numpy as np
from PIL import Image, ImageTk



url = "http://localhost:3000"
token = "?token=" + "0987"
#token = "?token=" + "1234"


empty_btn_config = {
    "text" : "",
    "bg" : "gray80"
    }

my_masons_btn_config = {
    "font": ("Arial", 30),
    "fg": "black",
    "bg": "red"
    }
    
enemy_masons_btn_config = {
    "font": ("Arial", 30),
    "fg": "black",
    "bg": "green"
    }
    
    
my_walls_btn_config = {
    "text" : "",
    "font": ("Arial", 36),
    "fg": "black",
    "bg": "red4"
    }
    
enemy_walls_btn_config = {
    "text" : "",
    "font": ("Arial", 36),
    "fg": "black",
    "bg": "dark green"
    }
    
    
my_territories_btn_config = {
    "text" : "",
    "font": ("Arial", 36),
    "fg": "black",
    "bg": "hot pink"
    }
    
enemy_territories_btn_config = {
    "text" : "",
    "font": ("Arial", 36),
    "fg": "black",
    "bg": "pale green"
    }
    
both_territories_btn_config = {
    "text" : "",
    "font": ("Arial", 36),
    "fg": "black",
    "bg": "tan4"
    }
    
    
pond_btn_config = {
    "text" : "",
    "bg": "dodger blue"
    }
    
castle_btn_config = {
    "text" : "CASTLE",
    "font" : ("Arial", 12),
    "fg" : "white",
    "bg" : "MediumOrchid2"
    }
    

class naprock_ui_lourenco(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)
        
        self.title("Light Rail Data Editor") #name of window
        
        self.attributes("-fullscreen", True)
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.show_frame(container=container, page_name="ui_frame", column=0)
    
    
    def show_frame(self,container, page_name, column):
        '''Show a frame for the given page name'''
        frame = globals()[page_name]
        frame = frame(parent=container, controller=self)
        frame.config(highlightbackground="black", highlightthickness=1)
        frame.grid(row=0, column=column, sticky = "nsew")
        frame.tkraise()
        
        
class ui_frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        #Window element
        Frame_L = Frame(self)
        Frame_L.grid(row=1, column=0, sticky="nswe", padx = 30)
        
        head_title_label = Label(self, text="Game Board",font=('Arial', 48, 'bold'), width=15)
        head_title_label.grid(row=0, column=0, padx = 20)
        
        
        #Frame R
        Frame_R = Frame(self)
        Frame_R.grid(row=1, column=1, sticky="ns")
        
        head_title_label2 = Label(self, text="Game Data",font=('Arial', 48, 'bold'))
        head_title_label2.grid(row=0, column=1, padx = 20)
        
        Frame_R1 = Frame(Frame_R)
        Frame_R1.grid(row=0, column=0, sticky="w")
        
        self.turns_name_label = Label(Frame_R1, text="Turns: ",font=('Arial', 24))
        self.turns_name_label.grid(row=0, column=0, sticky="w")
        
        self.turns_label = Label(Frame_R1, text="",font=('Arial', 30), fg="red")
        self.turns_label.grid(row=0, column=1, sticky="nw",padx = (0, 20))
        
        self.turns_time_name_label = Label(Frame_R1, text="Turns Time: ",font=('Arial', 24))
        self.turns_time_name_label.grid(row=1, column=0, sticky="w")
        
        self.turns_time_label = Label(Frame_R1, text="",font=('Arial', 30))
        self.turns_time_label.grid(row=1, column=1, sticky="nw",padx = (0, 20))
        
        self.id_name_label = Label(Frame_R1, text="ID: ",font=('Arial', 24))
        self.id_name_label.grid(row=2, column=0, sticky="w")
        
        self.id_label = Label(Frame_R1, text="",font=('Arial', 24))
        self.id_label.grid(row=2, column=1, sticky="nw",padx = (0, 20))
        
        #Frame R2
        Frame_R2 = Frame(Frame_R,pady = 100)
        Frame_R2.grid(row=1, column=0, sticky="w")
        #Frame R3
        Frame_R3 = Frame(Frame_R,pady = 100)
        Frame_R3.grid(row=2, column=0, sticky="sw")
        
        self.wall_name_label = Label(Frame_R3, text="W:",font=('Arial', 24))
        self.wall_name_label.grid(row=0, column=0, sticky="w")
        
        self.wall_bonus_label = Label(Frame_R3, text="0",font=('Arial', 24))
        self.wall_bonus_label.grid(row=0, column=1, sticky="w",padx = (0, 40))
        self.my_wall_bonus_label = Label(Frame_R3, text="0",font=('Arial', 24), fg="red")
        self.my_wall_bonus_label.grid(row=0, column=2, sticky="w",padx = (0, 40))
        self.enemy_wall_bonus_label = Label(Frame_R3, text="0",font=('Arial', 24), fg="green")
        self.enemy_wall_bonus_label.grid(row=0, column=3, sticky="w",padx = (0, 40))
        
        self.territory_name_label = Label(Frame_R3, text="T:",font=('Arial', 24))
        self.territory_name_label.grid(row=1, column=0, sticky="w")
        
        self.territory_bonus_label = Label(Frame_R3, text="0",font=('Arial', 24))
        self.territory_bonus_label.grid(row=1, column=1, sticky="w",padx = (0, 40))
        self.my_territory_bonus_label = Label(Frame_R3, text="0",font=('Arial', 24), fg="red")
        self.my_territory_bonus_label.grid(row=1, column=2, sticky="w",padx = (0, 40))
        self.enemy_territory_bonus_label = Label(Frame_R3, text="0",font=('Arial', 24), fg="green")
        self.enemy_territory_bonus_label.grid(row=1, column=3, sticky="w",padx = (0, 40))
        
        self.castle_name_label = Label(Frame_R3, text="C:",font=('Arial', 24))
        self.castle_name_label.grid(row=2, column=0, sticky="w")
        
        self.castle_bonus_label = Label(Frame_R3, text="0",font=('Arial', 24))
        self.castle_bonus_label.grid(row=2, column=1, sticky="w",padx = (0, 40))
        self.my_castle_bonus_label = Label(Frame_R3, text="0",font=('Arial', 24), fg="red")
        self.my_castle_bonus_label.grid(row=2, column=2, sticky="w",padx = (0, 40))
        self.enemy_castle_bonus_label = Label(Frame_R3, text="0",font=('Arial', 24), fg="green")
        self.enemy_castle_bonus_label.grid(row=2, column=3, sticky="w",padx = (0, 40))
        
        #getting data
        self.game_data = self.get_data_from_server()
        #print(self.game_data)
        
        #setting variable
        self.game_turns = self.game_data["turns"]
        self.my_turns = 0
        self.game_turns_time = self.game_data["turnSeconds"]
        self.my_turns_time = self.game_turns_time
        self.game_id = self.game_data["id"]
        
        self.wall_bonus = self.game_data["bonus"]["wall"]
        self.my_wall_bonus = 0
        self.enemy_wall_bonus = 0
        
        self.territory_bonus = self.game_data["bonus"]["territory"]
        self.my_territory_bonus = 0
        self.enemy_territory_bonus = 0
        
        self.castle_bonus = self.game_data["bonus"]["castle"]
        self.my_castle_bonus = 0
        self.enemy_castle_bonus = 0
        
        self.turns_label.config(text=str(self.my_turns) +"/" + str(self.game_turns))
        self.turns_time_label.config(text=str(self.my_turns_time) +" s /" + str(self.game_turns_time)+" s")
        self.id_label.config(text=str(self.game_id))
        
        self.wall_bonus_label.config(text=str(self.wall_bonus))
        self.my_wall_bonus_label.config(text=str(self.my_wall_bonus))
        self.enemy_wall_bonus_label.config(text=str(self.enemy_wall_bonus))
        
        self.territory_bonus_label.config(text=str(self.territory_bonus))
        self.my_territory_bonus_label.config(text=str(self.my_territory_bonus))
        self.enemy_territory_bonus_label.config(text=str(self.enemy_territory_bonus))
        
        self.castle_bonus_label.config(text=str(self.castle_bonus))
        self.my_castle_bonus_label.config(text=str(self.my_castle_bonus))
        self.enemy_castle_bonus_label.config(text=str(self.enemy_castle_bonus))
        
        
        self.post_btn = Button(self, text="POST", font=('Arial', 30), command= lambda: self.post_btn_clicked(parent, controller))
        self.post_btn.grid(row=2, column=1, sticky="w", padx = 20, pady = (0, 20))
        
        
        #setting board
        self.board_width = self.game_data["board"]["width"]
        self.board_height = self.game_data["board"]["height"]
        self.board_structures = self.game_data["board"]["structures"]
        self.board_masons = self.game_data["board"]["masons"]
        self.board_num_mason = self.game_data["board"]["mason"]
        self.my_masons = [[0, 0] for i in range(self.board_num_mason)]
        
        self.my_selected_unit = [None,None]
        self.my_action = [{"type":0, "dir":0} for i in range(self.board_num_mason)]
        self.board_walls = [[0 for column in range(self.board_width)] for row in range(self.board_height)]
        self.board_territories = [[0 for column in range(self.board_width)] for row in range(self.board_height)]
        
        
        unit_size = 0
        if (self.board_width >22) or (self.board_height >22):
            unit_size = 37
        elif (self.board_width >14) or (self.board_height >14):
            unit_size = 44
        else:
            unit_size = 70
        self.board_views = [[self.create_board_unit(Frame_L,parent, controller, row, column, unit_size) for column in range(self.board_width)] for row in range(self.board_height)]
        self.board_actions_views = [[None for j in range(3)] for i in range(self.board_num_mason)]
        
        
        for row_index, row_data in enumerate(self.board_structures): #creating empty board
            for column_index, column_data in enumerate(self.board_structures[row_index]):
                if column_data == 1:
                    self.board_views[row_index][column_index].config(**pond_btn_config)
                elif column_data == 2:
                    self.board_views[row_index][column_index].config(**castle_btn_config)
                    
        for row_index, row_data in enumerate(self.board_masons): #add masons to the board
            for column_index, column_data in enumerate(self.board_masons[row_index]):
                if column_data > 0:
                    self.board_views[row_index][column_index].config(text=int(column_data),**my_masons_btn_config)
                    self.my_masons[column_data -1][0] = column_index
                    self.my_masons[column_data -1][1] = row_index
                    self.board_actions_views[column_data -1][0] = Label(Frame_R2, text=str(column_data)+". ",font=('Arial', 24))
                    self.board_actions_views[column_data -1][0].grid(row=column_data-1, column=0, sticky="w",padx = (0, 40))
                    self.board_actions_views[column_data -1][1] = Label(Frame_R2, text="",font=('Arial', 24))
                    self.board_actions_views[column_data -1][1].grid(row=column_data-1, column=1, sticky="w",padx = (0, 40))
                    self.board_actions_views[column_data -1][2] = Label(Frame_R2, text="",font=('Arial', 24))
                    self.board_actions_views[column_data -1][2].grid(row=column_data-1, column=2, sticky="w",padx = (0, 40))
                elif column_data < 0:
                    self.board_views[row_index][column_index].config(text=int(column_data), **enemy_masons_btn_config)
                    
        print(np.matrix(self.board_masons))
        print(self.my_masons)
        controller.bind("<Key>", self.key_handler)
        self.after(10, self.get_data_from_server_2)
        self.after(10, self.count_down)
        
        
        
    def get_data_from_server(self):
        initMatches_endpoint = url + "/matches" + token
        respone = requests.get(initMatches_endpoint)
        res_text = respone.text
        res_decode = json.loads(res_text) #解碼
        
        return res_decode["matches"][0]
        
        
    def get_data_from_server_2(self):
        try:
            initMatches_endpoint = url + "/matches/"+ str(self.game_id) + token
            respone = requests.get(initMatches_endpoint)
            res_text = respone.text
            res_decode = json.loads(res_text) #解碼
            #print(np.matrix(res_decode))
            if int(res_decode["turn"]) != int(self.my_turns):
                self.my_turns = res_decode["turn"]
                self.turns_label.config(text= str(res_decode["turn"])+"/" + str(self.game_turns))
                self.my_turns_time = self.game_turns_time
                self.turns_time_label.config(text=str(self.my_turns_time)+"/"+ str(self.game_turns_time))
                
                self.my_wall_bonus = sum(row_data.count(1) for row_data in res_decode["board"]["walls"]) * self.wall_bonus
                self.my_wall_bonus_label.config(text=str(self.my_wall_bonus))
                
                self.enemy_wall_bonus = sum(row_data.count(2) for row_data in res_decode["board"]["walls"]) * self.wall_bonus
                self.enemy_wall_bonus_label.config(text=str(self.enemy_wall_bonus))
                
                self.my_territory_bonus = sum(row_data.count(1)+row_data.count(3) for row_data in res_decode["board"]["territories"]) * self.territory_bonus
                self.my_territory_bonus_label.config(text=str(self.my_territory_bonus))
                self.enemy_territory_bonus = sum(row_data.count(2)+row_data.count(3) for row_data in res_decode["board"]["territories"]) * self.territory_bonus
                self.enemy_territory_bonus_label.config(text=str(self.enemy_territory_bonus))
                
                print(np.matrix(res_decode["board"]["territories"]))
                print(np.matrix(self.board_territories))
                
                
                
                for row_index, row_data in enumerate(res_decode["board"]["masons"]): #update masons
                    for column_index, column_data in enumerate(row_data):
                        if column_data != self.board_masons[row_index][column_index]:
                            if column_data == 0:
                                self.board_masons[row_index][column_index] = column_data
                                self.board_views[row_index][column_index].config(**empty_btn_config)
                            elif column_data > 0:
                                self.board_masons[row_index][column_index] = column_data
                                self.board_views[row_index][column_index].config(text=str(column_data),**my_masons_btn_config)
                            elif column_data < 0:
                                self.board_masons[row_index][column_index] = column_data
                                self.board_views[row_index][column_index].config(text=str(column_data),**enemy_masons_btn_config)
                                
                for row_index, row_data in enumerate(res_decode["board"]["walls"]): #update walls
                    for column_index, column_data in enumerate(row_data):
                        if column_data != self.board_walls[row_index][column_index]:
                            if column_data == 0:
                                self.board_walls[row_index][column_index] = column_data
                                self.board_views[row_index][column_index].config(**empty_btn_config)
                                if self.board_structures[row_index][column_index] == 1:
                                    self.board_views[row_index][column_index].config(**pond_btn_config)
                            elif column_data == 1:
                                self.board_walls[row_index][column_index] = column_data
                                self.board_views[row_index][column_index].config(**my_walls_btn_config)
                                if self.board_structures[row_index][column_index] == 1:
                                    self.board_views[row_index][column_index].config(text="O")
                            elif column_data == 2:
                                self.board_walls[row_index][column_index] = column_data
                                self.board_views[row_index][column_index].config(**enemy_walls_btn_config)
                                if self.board_structures[row_index][column_index] == 1:
                                    self.board_views[row_index][column_index].config(text="O")
                                
                self.my_castle_bonus == 0
                for row_index, row_data in enumerate(res_decode["board"]["territories"]): #update territories
                    for column_index, column_data in enumerate(row_data):
                        if column_data != self.board_territories[row_index][column_index]:
                            if res_decode["board"]["structures"][row_index][column_index] != 2 and res_decode["board"]["masons"][row_index][column_index] == 0: 
                                if column_data == 0:
                                    self.board_territories[row_index][column_index] = column_data
                                    self.board_views[row_index][column_index].config(**empty_btn_config)
                                elif column_data == 1:
                                    self.board_territories[row_index][column_index] = column_data
                                    self.board_views[row_index][column_index].config(**my_territories_btn_config)
                                elif column_data == 2:
                                    self.board_territories[row_index][column_index] = column_data
                                    self.board_views[row_index][column_index].config(**enemy_territories_btn_config)
                                elif column_data == 3:
                                    self.board_territories[row_index][column_index] = column_data
                                    self.board_views[row_index][column_index].config(**both_territories_btn_config)
                            elif (res_decode["board"]["structures"][row_index][column_index] == 2) and (column_data == (1 or 3)):
                                self.my_castle_bonus += self.castle_bonus
                            elif (res_decode["board"]["structures"][row_index][column_index] == 2) and (column_data == (2 or 3)):
                                self.enemy_castle_bonus += self.castle_bonus
                self.my_castle_bonus_label.config(text=str(self.my_castle_bonus))
                self.enemy_castle_bonus_label.config(text=str(self.enemy_castle_bonus))
                print("c: ",self.my_castle_bonus)
                                
                
        except:
            pass
                        
                        
        
        #return res_decode["matches"][0]
        self.after(500, self.get_data_from_server_2)
        
        
    def count_down(self):
        self.my_turns_time -= 1
        self.turns_time_label.config(text=str(self.my_turns_time)+"/"+ str(self.game_turns_time))
        self.after(1000, self.count_down) 
        
        
    def post_btn_clicked(self, parent, controller):
        initMatches_endpoint = url + "/matches/"+ str(self.game_id) + token
        content = {
            "turn":self.my_turns + 1,
            "actions":self.my_action}
            
        print(content)
            
        post_action = requests.post(initMatches_endpoint, json = content)

        print(post_action.text)
        
        
    def board_btn_clicked(self, parent, controller, coordinate):
        self.my_selected_unit[0] = coordinate[0]
        self.my_selected_unit[1] = coordinate[1]
        #print(coordinate)
        
        
    def create_board_unit(self, frame, parent, controller, row, column, square_size):
        
        #square_size = 70
        #square_size = 37
        label_frame = Frame(frame, width = square_size, height = square_size)
        label_frame.grid_propagate(False) #disables resizing of frame
        label_frame.columnconfigure(0, weight=1) #enables label to fill frame
        label_frame.rowconfigure(0,weight=1) #any positive number would do the trick
        label_frame.grid(row=row, column=column)
        square_btn = Button(label_frame, highlightbackground="black", highlightthickness=2, command= lambda: self.board_btn_clicked(parent, controller, [column, row]), bg="gray80")
        square_btn.grid(sticky="wens")
        return square_btn
        
        
    def key_handler(self, event):
        # U = Up, D = Down, L = Left, R = Right
        keycode = {
            "type_stay" : 81,
            "type_move" : 49,
            "type_bulid" : 50,
            "type_destroy" : 51,
            "dir_none" : 101,
            "dir_UL" : 103,
            "dir_U" : 104,
            "dir_UR" : 105,
            "dir_R" : 102,
            "dir_DR" : 99,
            "dir_D" : 98,
            "dir_DL" : 97,
            "dir_L" : 100
        }
        
        view_code = {
            "type_stay" : {"code_type": "type", "server_code" : 0, "view_text": "Stay"},
            "type_move" : {"code_type": "type", "server_code" : 1, "view_text": "Move"},
            "type_bulid" : {"code_type": "type", "server_code" : 2, "view_text": "Build"},
            "type_destroy" : {"code_type": "type", "server_code" : 3, "view_text": "Destroy"},
            "dir_none" : {"code_type": "dir", "server_code" : 0, "view_text": "X"},
            "dir_UL" : {"code_type": "dir", "server_code" : 1, "view_text": "⇖"},
            "dir_U" : {"code_type": "dir", "server_code" : 2, "view_text": "⇑"},
            "dir_UR" : {"code_type": "dir", "server_code" : 3, "view_text": "⇗"},
            "dir_R" : {"code_type": "dir", "server_code" : 4, "view_text": "⇒"},
            "dir_DR" : {"code_type": "dir", "server_code" : 5, "view_text": "⇘"},
            "dir_D" : {"code_type": "dir", "server_code" : 6, "view_text": "⇓"},
            "dir_DL" : {"code_type": "dir", "server_code" : 7, "view_text": "⇙"},
            "dir_L" : {"code_type": "dir", "server_code" : 8, "view_text": "⇐"}}
        
        if event.keycode in keycode.values():
            selected_masons = self.board_masons[self.my_selected_unit[1]][self.my_selected_unit[0]]
            if selected_masons > 0:
                keyname = list(keycode.keys())[list(keycode.values()).index(event.keycode)]
                code_type = view_code[keyname]["code_type"]
                which_label = 1 if code_type == "type" else 2
                self.my_action[selected_masons - 1][code_type] = view_code[keyname]["server_code"]
                self.board_actions_views[selected_masons - 1][which_label].config(text=view_code[keyname]["view_text"])
        
        
        print(event.char, event.keysym, event.keycode)

    

if __name__ == "__main__":
    naprock_ui_lourenco().mainloop()

