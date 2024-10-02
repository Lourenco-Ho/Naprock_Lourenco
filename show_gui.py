from tkinter import *

#this app labrary
import board_pad_appearance
import action_pad_appearance


def window_layout(frame_class):
    frame_class.Frame_L = Frame(frame_class)
    frame_class.Frame_L.grid(row=1, column=0, sticky="nswe", padx = 30)

    frame_class.Frame_R = Frame(frame_class)
    frame_class.Frame_R.grid(row=1, column=1, sticky="ns")



def info_pad(frame_class):
    head_title_label2 = Label(frame_class, text="Game Data",font=('Arial', 48, 'bold'))
    head_title_label2.grid(row=0, column=1, padx = 20)
    

    #Frame 1
    Frame_R1 = Frame(frame_class.Frame_R)
    Frame_R1.grid(row=0, column=0, sticky="w")
    
    turns_name_label = Label(Frame_R1, **action_pad_appearance.content_label_config(action_pad_appearance.text_content["turns_label"]))
    turns_name_label.grid(row=0, column=0, sticky="w")
    
    frame_class.turns_label = Label(Frame_R1, **action_pad_appearance.turns_label_config(""))
    frame_class.turns_label.grid(row=0, column=1, sticky="nw",padx = (0, 20))
    
    turns_time_name_label = Label(Frame_R1, **action_pad_appearance.content_label_config(action_pad_appearance.text_content["turns_time_label"]))
    turns_time_name_label.grid(row=1, column=0, sticky="w")
    
    frame_class.turns_time_label = Label(Frame_R1, **action_pad_appearance.turns_time_label_config(""))
    frame_class.turns_time_label.grid(row=1, column=1, sticky="nw",padx = (0, 20))
    
    id_name_label = Label(Frame_R1, **action_pad_appearance.content_label_config(action_pad_appearance.text_content["id_label"]))
    id_name_label.grid(row=2, column=0, sticky="w")
    
    frame_class.id_label = Label(Frame_R1, **action_pad_appearance.content_label_config(""))
    frame_class.id_label.grid(row=2, column=1, sticky="nw",padx = (0, 20))


    #Frame 3
    Frame_R3 = Frame(frame_class.Frame_R,pady = 100)
    Frame_R3.grid(row=2, column=0, sticky="sw")
    
    wall_name_label = Label(Frame_R3, **action_pad_appearance.content_label_config(action_pad_appearance.text_content["wall"]))
    wall_name_label.grid(row=0, column=0, sticky="w")
    
    frame_class.wall_bonus_label = Label(Frame_R3, **action_pad_appearance.content_label_config(action_pad_appearance.text_content["ori_num"]))
    frame_class.wall_bonus_label.grid(row=0, column=1, sticky="w",padx = (0, 40))
    frame_class.my_wall_bonus_label = Label(Frame_R3, **action_pad_appearance.my_bonus_label_config(action_pad_appearance.text_content["ori_num"]))
    frame_class.my_wall_bonus_label.grid(row=0, column=2, sticky="w",padx = (0, 40))
    frame_class.enemy_wall_bonus_label = Label(Frame_R3, **action_pad_appearance.enemy_bonus_label_config(action_pad_appearance.text_content["ori_num"]))
    frame_class.enemy_wall_bonus_label.grid(row=0, column=3, sticky="w",padx = (0, 40))
    
    territory_name_label = Label(Frame_R3, **action_pad_appearance.content_label_config(action_pad_appearance.text_content["territory"]))
    territory_name_label.grid(row=1, column=0, sticky="w")
    
    frame_class.territory_bonus_label = Label(Frame_R3, **action_pad_appearance.content_label_config(action_pad_appearance.text_content["ori_num"]))
    frame_class.territory_bonus_label.grid(row=1, column=1, sticky="w",padx = (0, 40))
    frame_class.my_territory_bonus_label = Label(Frame_R3, **action_pad_appearance.my_bonus_label_config(action_pad_appearance.text_content["ori_num"]))
    frame_class.my_territory_bonus_label.grid(row=1, column=2, sticky="w",padx = (0, 40))
    frame_class.enemy_territory_bonus_label = Label(Frame_R3, **action_pad_appearance.enemy_bonus_label_config(action_pad_appearance.text_content["ori_num"]))
    frame_class.enemy_territory_bonus_label.grid(row=1, column=3, sticky="w",padx = (0, 40))
    
    castle_name_label = Label(Frame_R3, **action_pad_appearance.content_label_config(action_pad_appearance.text_content["castle"]))
    castle_name_label.grid(row=2, column=0, sticky="w")
    
    frame_class.castle_bonus_label = Label(Frame_R3, **action_pad_appearance.content_label_config(action_pad_appearance.text_content["ori_num"]))
    frame_class.castle_bonus_label.grid(row=2, column=1, sticky="w",padx = (0, 40))
    frame_class.my_castle_bonus_label = Label(Frame_R3, **action_pad_appearance.my_bonus_label_config(action_pad_appearance.text_content["ori_num"]))
    frame_class.my_castle_bonus_label.grid(row=2, column=2, sticky="w",padx = (0, 40))
    frame_class.enemy_castle_bonus_label = Label(Frame_R3, **action_pad_appearance.enemy_bonus_label_config(action_pad_appearance.text_content["ori_num"]))
    frame_class.enemy_castle_bonus_label.grid(row=2, column=3, sticky="w",padx = (0, 40))



def masons_pad(frame_class):
    frame_class.Frame_R2 = Frame(frame_class.Frame_R, pady = 100)
    frame_class.Frame_R2.grid(row=1, column=0, sticky="w")

def post_btn(frame_class):
    frame_class.post_btn = Button(frame_class, text="POST", font=('Arial', 30), command= frame_class.post_btn_clicked)
    frame_class.post_btn.grid(row=2, column=1, sticky="w", padx = 20, pady = (0, 20))