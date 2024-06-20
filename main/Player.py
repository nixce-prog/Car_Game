import json
import os.path

class Player():
    car_all = {"volvo":100,
               "maxbuk":1000
               }

    default = [("money", 0, int),
                ("win", 0, int), 
                ("password", "0000", str), 
                ("bad", 0, int),
                ("car",{x[0]:False for x in car_all.items()},dict)
                ]
    
    info_d = {x[0]: x[2](x[1]) for x in default}

    def __init__(self, login, password):
        info = {}
        if os.path.isfile("profile.json"):
            with open("profile.json", "r+") as f:
                s = json.load(f)
                if login in s:
                    if s["system"][login] == len(str(s[login])):
                        if s[login]["password"] == password:
                            if len(s[login]) == len(Player.default) + 1:
                                info = s[login]
                            else:
                                for x in Player.default:
                                    if x[0] not in s[login]:
                                        s[login][x[0]] = x[2](x[1])
                                info = s[login]
                                s["system"][login] = len(str(s[login]))
                                f.seek(0)
                                f.truncate()
                                json.dump(s, f)
                            self.accaunt = 1
                        else:
                            self.accaunt = 3
                    else:
                        self.accaunt = 4

                else:
                    f.seek(0)
                    f.truncate()
                    info = Player.info_d
                    info["password"] = password
                    s[login] = info
                    s["system"][login] = len(str(info))
                    json.dump(s, f)
                    self.accaunt = 2

        else:
            with open("profile.json", "w+") as f:
                info = Player.info_d
                info["password"] = password
                json.dump({login: info,"system":{login:len(str(info))}}, f)
                self.accaunt = 2

        g = {x[0]:x[2] for x in Player.default}
        self.info = {x[0]:g[x[0]](x[1]) for x in info.items()}
        self.login = login

    def save(self):
        with open("profile.json", "r+") as f:
            s = json.load(f)
            f.seek(0)
            f.truncate()
            s[self.login] = self.info
            s["system"][self.login] = len(str(self.info))
            json.dump(s, f)



    def buy(self,car):
        if self.info["money"] >= Player.car_all[car]:
            self.info['money'] -= Player.car_all[car]
            self.info["car"][car] = True
            self.save()
            print( "купленно" )
        print( "не хватает денег" )




