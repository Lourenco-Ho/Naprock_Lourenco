# U = Up, D = Down, L = Left, R = Right
old_keycode = {
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

keycode = {
    "move_1" : 49,
    "move_2" : 50,
    "move_3" : 51,
    "move_4" : 52,
    "move_5" : 53,
    "move_6" : 54,
    "bulid_1" : 81,
    "bulid_2" : 87,
    "bulid_3" : 69,
    "bulid_4" : 82,
    "bulid_5" : 84,
    "bulid_6" : 89,
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
    "dir_L" : {"code_type": "dir", "server_code" : 8, "view_text": "⇐"}
}

def handler(event, frame_class):
    #if event.keycode in keycode.values():
    if event.keycode in old_keycode.values():
        selected_masons = frame_class.board_masons[frame_class.my_selected_unit[1]][frame_class.my_selected_unit[0]]
        if selected_masons > 0:
            #keyname = list(keycode.keys())[list(keycode.values()).index(event.keycode)] #find keyname by value
            keyname = list(old_keycode.keys())[list(old_keycode.values()).index(event.keycode)]
            code_type = view_code[keyname]["code_type"]
            which_label = 1 if code_type == "type" else 2
            frame_class.my_action[selected_masons - 1][code_type] = view_code[keyname]["server_code"]
            frame_class.board_actions_views[selected_masons - 1][which_label].config(text=view_code[keyname]["view_text"])
    
    print(event.char, event.keysym, event.keycode)


def set_handler(window_class, frame_class):
    window_class.bind("<Key>", lambda event: handler(event, frame_class))