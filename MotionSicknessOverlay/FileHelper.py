import json

def get_json_string(args):
    jsonString = json.dumps(args)
    return jsonString

def write_to_file(args):
    f = open("SaveFile.txt", "w")
    f.write(args)
    f.close()
    return

def get_saved_data():
    try:
        f = open("SaveFile.txt", "r")
        jsonString = f.read()
        saveProperties = json.loads(jsonString)
        return saveProperties
    except:
        return {
            "radius" : 300,
            "offsetx" : 0,
            "offsety" : 0,
            "sensitivity" : 1,
            "fade_speed" : 1,
            "control_type" : "Gamepad"
        }