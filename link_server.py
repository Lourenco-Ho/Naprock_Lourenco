import requests
import json

#my labrary
import show_gui

url = "http://localhost:3000"
token = "?token=" + "0987"
#token = "?token=" + "1234"

def get_data(end_point):
    respone = requests.get(end_point)
    res_text = respone.text
    res_decode = json.loads(res_text) #解碼
    return res_decode


def first_getting(frame_class):
    endpoint = url + "/matches" + token
    server_data = get_data(endpoint)["matches"][0]

    #setting variable
    #info data
    frame_class.game_turns = server_data["turns"]
    frame_class.my_turns = 0
    frame_class.game_turns_time = server_data["turnSeconds"]
    frame_class.my_turns_time = frame_class.game_turns_time
    frame_class.game_id = server_data["id"]
    
    frame_class.wall_bonus = server_data["bonus"]["wall"]
    frame_class.my_wall_bonus = 0
    frame_class.enemy_wall_bonus = 0
    
    frame_class.territory_bonus = server_data["bonus"]["territory"]
    frame_class.my_territory_bonus = 0
    frame_class.enemy_territory_bonus = 0
    
    frame_class.castle_bonus = server_data["bonus"]["castle"]
    frame_class.my_castle_bonus = 0
    frame_class.enemy_castle_bonus = 0
    
    #layout data
    frame_class.board_width = server_data["board"]["width"]
    frame_class.board_height = server_data["board"]["height"]
    frame_class.board_structures = server_data["board"]["structures"]
    frame_class.board_masons = server_data["board"]["masons"]
    frame_class.board_num_mason = server_data["board"]["mason"]
    frame_class.my_masons = [{"coor" : [0, 0], "path": []} for i in range(frame_class.board_num_mason)] #[x, y]
    frame_class.update_my_masons()
    frame_class.board_walls = [[0 for column in range(frame_class.board_width)] for row in range(frame_class.board_height)]
    frame_class.board_territories = [[0 for column in range(frame_class.board_width)] for row in range(frame_class.board_height)]
    
    #my action data
    frame_class.my_action = [{"type":0, "dir":0} for i in range(frame_class.board_num_mason)]

    
def get(frame_class):
    try:
        initMatches_endpoint = url + "/matches/"+ str(frame_class.game_id) + token
        respone = requests.get(initMatches_endpoint)
        res_text = respone.text
        res_decode = json.loads(res_text) #解碼

        if int(res_decode["turn"]) != int(frame_class.my_turns):
            frame_class.my_turns = res_decode["turn"]
            frame_class.my_turns_time = frame_class.game_turns_time
            
            frame_class.my_wall_bonus = sum(row_data.count(1) for row_data in res_decode["board"]["walls"]) * frame_class.wall_bonus
            frame_class.enemy_wall_bonus = sum(row_data.count(2) for row_data in res_decode["board"]["walls"]) * frame_class.wall_bonus
            
            frame_class.my_territory_bonus = sum(row_data.count(1)+row_data.count(3) for row_data in res_decode["board"]["territories"]) * frame_class.territory_bonus
            frame_class.enemy_territory_bonus = sum(row_data.count(2)+row_data.count(3) for row_data in res_decode["board"]["territories"]) * frame_class.territory_bonus

            frame_class.my_castle_bonus = 0

            #update layout
            show_gui.update(frame_class, res_decode)

            frame_class.board_masons = res_decode["board"]["masons"]
            frame_class.board_walls = res_decode["board"]["walls"]
            frame_class.board_territories = res_decode["board"]["territories"]
            
    except:
        pass

    frame_class.after(500, lambda: get(frame_class))


def post(frame_class):
    initMatches_endpoint = url + "/matches/"+ str(frame_class.game_id) + token
    content = {
        "turn":frame_class.my_turns + 1,
        "actions":frame_class.my_action}
        
    post_action = requests.post(initMatches_endpoint, json = content)
    #print(post_action.text)