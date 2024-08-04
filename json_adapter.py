import json
import os

user_json_path = f"users/"
config_json_path = "config.json"


def get_upgrades_data():
    with open(config_json_path,"r") as file:
        data = json.load(file)
    return data
    

def write_user_data(id, balance: int = None, level: int = None):
    json_path = f"{user_json_path}{id}.json"
    user_data = get_user_data(id)
    if balance:
        user_data["balance"] = balance
    if level: 
        user_data["level"] = level
    with open(json_path, "w") as file:
        json.dump(user_data, file)
    return user_data


def get_user_data(id):
    json_path = f"{user_json_path}{id}.json"
    if not os.path.exists(json_path):
        return create_user(id)
    with open(json_path,"r") as file:
        user_data = json.load(file)
    return user_data

def create_user(id):
    json_path = f"{user_json_path}{id}.json"
    user_data = {
        "balance": 1,
        "level": 1
    }
    with open(json_path,"x") as file:
        json.dump(user_data, file)
    return user_data
