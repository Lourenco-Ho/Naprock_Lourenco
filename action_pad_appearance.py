
#action pad
text_content = {
    "turns_label" : "Turns: ",
    "turns_time_label" : "Turns Time: ",
    "id_label" : "ID: ",
    "ori_num" : "0",
    "wall" : "W: ",
    "territory" : "T: ",
    "castle" : "C: ",
}


#common
def content_label_config(text):
    config_value = {
        "text" : text,
        "font" : ("Arial", 24),
        "fg" : "black"
        }
    
    return config_value


#frame 1
def turns_label_config(text):
    config_value = {
        "text" : text,
        "font" : ("Arial", 30),
        "fg" : "red"
        }
    
    return config_value


def turns_time_label_config(text):
    config_value = {
        "text" : text,
        "font" : ("Arial", 30),
        "fg" : "black"
        }
    
    return config_value


#frame 3
def my_bonus_label_config(text):
    config_value = {
        "text" : text,
        "font" : ("Arial", 24),
        "fg" : "red"
        }
    
    return config_value


def enemy_bonus_label_config(text):
    config_value = {
        "text" : text,
        "font" : ("Arial", 24),
        "fg" : "green"
        }
    
    return config_value