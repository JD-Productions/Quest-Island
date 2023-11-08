import json, os

__author__="Dalton"

def intinput(question=""):
    answer = input(question)
    try:
        int(answer)
        return int(answer)
    except:
        pass

def get_users():
    path = os.getcwd()
    users = [json_data for json_data in os.listdir(path) if json_data.endswith('.json')]
    for user in users:
        num = users.index(user)
        users[num] = user.split(".")[0] 
    return users

def add_user(user):
    users = get_users()
    users.append(user)

def _reset_user(user):
    setup = {
    "money": 5,
    "inventory": [],
    "job": None
    }
    with open(f"{user}.json", "w") as file:
        json.dump(setup, file)
        print(f"USER {user.upper()} HAS BEEN RESET")

def dialogue(name=""):
    name += ".txt"
    path = os.getcwd() + "/Dialogue"
    names = [name for name in os.listdir(path) if name.endswith('.txt')]
    if name not in names:
        raise ValueError()
    with open(name, "r") as file:
        print(file)

class Db:
    def __init__(self, user):
        self.user = user
        if user not in get_users():
            add_user(user)
        self.setup = {
        "money": 5,
        "inventory": [],
        "job": None
        }
        self.create_save_file()

    def create_save_file(self, overwrite=False):
        try:
            with open(f"{self.user}.json", "x") as file:
                json.dump(self.setup, file)
        except FileExistsError:
            if overwrite:
                with open(f"{self.user}.json", "w") as file:
                    json.dump(self.setup, file)
            else:
                pass
    
    def get_file(self):
        with open(f"{self.user}.json", "r") as file:
            save = json.load(file)
            return save
    
    def save_file(self, file):
        with open(f"{self.user}.json", "w") as f:
            json.dump(file, f)
    
    def add_item(self, item):
        with open(f"{self.user}.json") as file:
            save = json.load(file)
            save['inventory'].append(item)
            self.save_file(save)
    
    def remove_item(self, item):
        with open(f"{self.user}.json") as file:
            save = json.load(file)
            try:
                save['inventory'].remove(item)
                self.save_file(save)
            except:
                raise

def choose_user():
    users = get_users()
    while True:
        print("Type the number for the user")
        i = 1
        print("[0] New User")
        for user in users:
            print(f"[{i}] {user}")
            i += 1
        i -= 1
        user = intinput()
        if user == 0:
            name = input("User Name: ").strip().title()
            Db(name)
            return name
        if type(user) == int:
            if user <= i:
                user = users[user-1]
                break
    return user
