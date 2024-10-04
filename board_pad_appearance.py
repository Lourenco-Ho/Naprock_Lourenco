#board pad
unit_size_L = 70
unit_size_M = 44
unit_size_s = 37

def unit_size(board_width, board_height):
    unit_size = 0
    if (board_width >22) or (board_height >22):
        unit_size = unit_size_s
    elif (board_width >14) or (board_height >14):
        unit_size = unit_size_M
    else:
        unit_size = unit_size_L

    return unit_size


def headtitle_label_config(text):
    config_value = {
        "text" : text,
        "font" : ('Arial', 48, 'bold'),
        "fg" : "black"
        }
    
    return config_value


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