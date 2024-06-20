import json
import os.path

class Player():
    default = [("money", 0, int), ("win", 0, str), ("password", "0000", str), ("bad", 0, int)]
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
                        exit()

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
