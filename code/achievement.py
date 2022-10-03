import json
import globalvar as gv

def check_achievements(seconds, minutes, hours, atmpts):
    
    data_json = open("data.json", "r")
    data_json_object = json.load(data_json)
    data_json.close()
    data_json_object["achievement"]["achv01"]="X"
    
    if minutes and int(minutes)<1:
        data_json_object["achievement"]["achv02"]="X"
    
    if seconds and int(seconds)<10:
        data_json_object["achievement"]["achv03"]="X"
    
    if atmpts and int(atmpts)==gv.MAX_ATTEMPTS:
        data_json_object["achievement"]["achv04"]="X"
    
    if hours and int(hours)>=1:
        data_json_object["achievement"]["achv05"]="X"
    
    if gv.day_elapsed:
        data_json_object["achievement"]["achv06"]="X"

    
    data_json = open("data.json", "w")
    json.dump(data_json_object, data_json, indent=2)
    data_json.close()

def check_day_elapsed_achievements():
    data_json = open("data.json", "r")
    data_json_object = json.load(data_json)
    data_json.close()

    if gv.day_elapsed:
        print("point 2")
        data_json_object["achievement"]["achv06"]="X"

    data_json = open("data.json", "w")
    json.dump(data_json_object, data_json, indent=2)
    data_json.close()

