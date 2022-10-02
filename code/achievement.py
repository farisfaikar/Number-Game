import json
from globalvar import MAX_ATTEMPTS, day_elapsed

def check_achievements(seconds, minutes, hours, atmpts):

    data_json = open("data.json", "r")
    data_json_object = json.load(data_json)
    data_json.close()
    
    data_json_object["achievement"]["achv01"]="X"
    
    if int(minutes)<1:
        data_json_object["achievement"]["achv02"]="X"
    
    if int(seconds)<10:
        data_json_object["achievement"]["achv03"]="X"
    
    if int(atmpts)==MAX_ATTEMPTS:
        data_json_object["achievement"]["achv04"]="X"
    
    if int(hours)>=1:
        data_json_object["achievement"]["achv05"]="X"
    
    if day_elapsed:
        data_json_object["achievement"]["achv06"]="X"

    
    data_json = open("data.json", "w")
    json.dump(data_json_object, data_json, indent=2)
    data_json.close()

