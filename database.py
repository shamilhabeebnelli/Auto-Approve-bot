from pymongo import MongoClient
from configs import cfg

client = MongoClient(cfg.MONGO_URI)

userss = client['main']['userss']
groupss = client['main']['groupss']

def alread(user_id):
        user = users.find_one({"user_id" : str(user_id)})
        if not user:
            return False
        return True

def alreadg(chat_id):
        group = groups.find_one({"chat_id" : str(chat_id)})
        if not group:
            return False
        return True

def addu(user_id):
    in_db = already_db(user_id)
    if in_db:
        return
    return users.insert_one({"uid": str(user_id)}) 

def remu(user_id):
    in_db = alread(user_id)
    if not in_db:
        return 
    return users.delete_one({"uid": str(user_id)})
    
def addg(chat_id):
    in_db = alreadg(chat_id)
    if in_db:
        return
    return groups.insert_one({"cid": str(chat_id)})

def allu():
    user = userss.find({})
    usrs = len(list(user))
    return usrs

def allg():
    group = groupss.find({})
    grps = len(list(group))
    return grps
