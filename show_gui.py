from tkinter import *

#this app labrary
import board_pad_appearance
import action_pad_appearance
import link_server


# *** layout ***
def window_layout(frame_class):
    head_title_label = Label(frame_class, board_pad_appearance.headtitle_label_config("Game Board"))
    head_title_label.grid(row=0, column=0, padx = 20)

    frame_class.Frame_L = Frame(frame_class)
    frame_class.Frame_L.grid(row=1, column=0, sticky="nswe", padx = 30)

    frame_class.Frame_R = Frame(frame_class)
    frame_class.Frame_R.grid(row=1, column=1, sticky="ns")



def info_pad(frame_class):
    head_title_label = Label(frame_class, action_pad_appearance.headtitle_label_config("Game Data"))
    head_title_label.grid(row=0, column=1, padx = 20)
    

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
    frame_class.post_btn = Button(frame_class, text="POST", font=('Arial', 30), command= lambda: link_server.post(frame_class))
    frame_class.post_btn.grid(row=2, column=1, sticky="w", padx = 20, pady = (0, 20))


def board_unit(frame_class, target_frame, row_index, column_index, square_size):
    label_frame = Frame(target_frame, width = square_size, height = square_size)
    label_frame.grid_propagate(False) #disables resizing of frame
    label_frame.columnconfigure(0, weight=1) #enables label to fill frame
    label_frame.rowconfigure(0,weight=1) #any positive number would do the trick
    label_frame.grid(row=row_index, column=column_index)
    square_btn = Button(label_frame, highlightbackground="black", highlightthickness=2, command= lambda: frame_class.board_btn_clicked([column_index, row_index]), bg="gray80")
    #square_btn.grid(sticky="wens")
    return square_btn



# *** update UI ***
def first_update(frame_class):
    #display info
    frame_class.turns_label.config(text=str(frame_class.my_turns) +"/" + str(frame_class.game_turns))
    frame_class.turns_time_label.config(text=str(frame_class.my_turns_time) +" s /" + str(frame_class.game_turns_time)+" s")
    frame_class.id_label.config(text=str(frame_class.game_id))
    
    frame_class.wall_bonus_label.config(text=str(frame_class.wall_bonus))
    frame_class.my_wall_bonus_label.config(text=str(frame_class.my_wall_bonus))
    frame_class.enemy_wall_bonus_label.config(text=str(frame_class.enemy_wall_bonus))
    
    frame_class.territory_bonus_label.config(text=str(frame_class.territory_bonus))
    frame_class.my_territory_bonus_label.config(text=str(frame_class.my_territory_bonus))
    frame_class.enemy_territory_bonus_label.config(text=str(frame_class.enemy_territory_bonus))
    
    frame_class.castle_bonus_label.config(text=str(frame_class.castle_bonus))
    frame_class.my_castle_bonus_label.config(text=str(frame_class.my_castle_bonus))
    frame_class.enemy_castle_bonus_label.config(text=str(frame_class.enemy_castle_bonus))


    unit_size = board_pad_appearance.unit_size(frame_class.board_width, frame_class.board_height)

    #create array for views and create empty unit
    frame_class.board_views = [[board_unit(frame_class, frame_class.Frame_L, row_index, column_index, unit_size) for column_index in range(frame_class.board_width)] for row_index in range(frame_class.board_height)]
    frame_class.board_actions_views = [[None for j in range(3)] for i in range(frame_class.board_num_mason)]
    
    #display
    for row_index, row_data in enumerate(frame_class.board_structures): #update structure to the empty board
        for column_index, column_data in enumerate(frame_class.board_structures[row_index]):
            if column_data == 1:
                frame_class.board_views[row_index][column_index].config(**board_pad_appearance.pond_btn_config)
            elif column_data == 2:
                frame_class.board_views[row_index][column_index].config(**board_pad_appearance.castle_btn_config)
                
    for row_index, row_data in enumerate(frame_class.board_masons): #add masons to the board
        for column_index, column_data in enumerate(frame_class.board_masons[row_index]):
            if column_data > 0:
                frame_class.board_views[row_index][column_index].config(text=int(column_data), **board_pad_appearance.my_masons_btn_config) #display mason on the board
                frame_class.my_masons[column_data -1]["coor"][0] = column_index #record mason's coordinate
                frame_class.my_masons[column_data -1]["coor"][1] = row_index
                frame_class.board_actions_views[column_data -1][0] = Label(frame_class.Frame_R2, **action_pad_appearance.content_label_config( str(column_data)+". " ) ) #view for masons index
                frame_class.board_actions_views[column_data -1][0].grid(row=column_data-1, column=0, sticky="w",padx = (0, 40))
                frame_class.board_actions_views[column_data -1][1] = Label(frame_class.Frame_R2, **action_pad_appearance.content_label_config( "" ) ) #view for masons moving type
                frame_class.board_actions_views[column_data -1][1].grid(row=column_data-1, column=1, sticky="w",padx = (0, 40))
                frame_class.board_actions_views[column_data -1][2] = Label(frame_class.Frame_R2, **action_pad_appearance.content_label_config( "" ) ) #view for masons moving direction
                frame_class.board_actions_views[column_data -1][2].grid(row=column_data-1, column=2, sticky="w",padx = (0, 40))
            elif column_data < 0:
                frame_class.board_views[row_index][column_index].config(text=int(column_data), **board_pad_appearance.enemy_masons_btn_config)


def update(frame_class, server_data):
    frame_class.turns_label.config(text= str(server_data["turn"])+"/" + str(frame_class.game_turns))
    frame_class.turns_time_label.config(text=str(frame_class.my_turns_time)+"/"+ str(frame_class.game_turns_time))
    frame_class.my_wall_bonus_label.config(text=str(frame_class.my_wall_bonus))
    frame_class.enemy_wall_bonus_label.config(text=str(frame_class.enemy_wall_bonus))
    frame_class.my_territory_bonus_label.config(text=str(frame_class.my_territory_bonus))
    frame_class.enemy_territory_bonus_label.config(text=str(frame_class.enemy_territory_bonus))

    for row_index, row_data in enumerate(server_data["board"]["masons"]): #update masons
        for column_index, column_data in enumerate(row_data):
            if column_data != frame_class.board_masons[row_index][column_index]:
                if column_data == 0:
                    frame_class.board_views[row_index][column_index].config(**board_pad_appearance.empty_btn_config)
                elif column_data > 0:
                    frame_class.board_views[row_index][column_index].config(text=str(column_data),**board_pad_appearance.my_masons_btn_config)
                elif column_data < 0:
                    frame_class.board_views[row_index][column_index].config(text=str(column_data),**board_pad_appearance.enemy_masons_btn_config)
                    
    for row_index, row_data in enumerate(server_data["board"]["walls"]): #update walls
        for column_index, column_data in enumerate(row_data):
            if column_data != frame_class.board_walls[row_index][column_index]:
                if column_data == 0:
                    frame_class.board_views[row_index][column_index].config(**board_pad_appearance.empty_btn_config)
                    if frame_class.board_structures[row_index][column_index] == 1:
                        frame_class.board_views[row_index][column_index].config(**board_pad_appearance.pond_btn_config)
                elif column_data == 1:
                    frame_class.board_views[row_index][column_index].config(**board_pad_appearance.my_walls_btn_config)
                    if frame_class.board_structures[row_index][column_index] == 1:
                        frame_class.board_views[row_index][column_index].config(text="O")
                elif column_data == 2:
                    frame_class.board_views[row_index][column_index].config(**board_pad_appearance.enemy_walls_btn_config)
                    if frame_class.board_structures[row_index][column_index] == 1:
                        frame_class.board_views[row_index][column_index].config(text="O")
                    
    
    for row_index, row_data in enumerate(server_data["board"]["territories"]): #update territories
        for column_index, column_data in enumerate(row_data):
            if column_data != frame_class.board_territories[row_index][column_index]:
                if server_data["board"]["structures"][row_index][column_index] != 2 and server_data["board"]["masons"][row_index][column_index] == 0: #if it is not castle
                    if column_data == 0:
                        frame_class.board_views[row_index][column_index].config(**board_pad_appearance.empty_btn_config)
                    elif column_data == 1:
                        frame_class.board_views[row_index][column_index].config(**board_pad_appearance.my_territories_btn_config)
                    elif column_data == 2:
                        frame_class.board_views[row_index][column_index].config(**board_pad_appearance.enemy_territories_btn_config)
                    elif column_data == 3:
                        frame_class.board_views[row_index][column_index].config(**board_pad_appearance.both_territories_btn_config)

                elif (server_data["board"]["structures"][row_index][column_index] == 2) and (column_data == (1 or 3)): #if it is castle
                    frame_class.my_castle_bonus += frame_class.castle_bonus
                elif (server_data["board"]["structures"][row_index][column_index] == 2) and (column_data == (2 or 3)): #if it is castle
                    frame_class.enemy_castle_bonus += frame_class.castle_bonus
                    
    frame_class.my_castle_bonus_label.config(text=str(frame_class.my_castle_bonus))
    frame_class.enemy_castle_bonus_label.config(text=str(frame_class.enemy_castle_bonus))