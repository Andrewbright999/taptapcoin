from json_adapter import get_upgrades_data, get_user_data, write_user_data

def on_tap(id):
    user_data = get_user_data(id)
    balance = user_data["balance"]
    level = user_data["level"]
    new_balance = round(balance + (1+0.2*level),1)
    write_user_data(id, new_balance)
    
def on_buy_upgrade(id):
    user_data = get_user_data(id)
    cost = get_cost_upgrade(id)
    balance = user_data["balance"]
    level = user_data["level"]
    if balance < cost:
        return {"status": "error",
                "data": "insufficient funds"}
    new_balance = round(balance - cost, 2)
    level = level + 1
    write_user_data(id, new_balance, level)
    return {"status": "succes"}
    
def get_cost_upgrade(id):
    user_data = get_user_data(id)
    upgrades_data = get_upgrades_data()
    start_cost = upgrades_data["start_cost"] 
    mult = upgrades_data["mult"]
    level = user_data["level"]
    cost = start_cost * mult**level
    return cost