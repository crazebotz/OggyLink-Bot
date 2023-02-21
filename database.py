import pymongo

# ------------Database----------
DB_URL = "mongodb+srv://mdisk:mdisk@cluster0.5f5kz5s.mongodb.net/?retryWrites=true&w=majority"
mongo = pymongo.MongoClient(DB_URL)
db = mongo["oggylink"]
dbcol = db["users"]


# database functions
def total_user() -> str:
    user = dbcol.count_documents({})
    return str(user)


# insert user data
def insert(chat_id,NAME):
    user_id = int(chat_id)
    user_det = {"_id": user_id,"name": NAME, "API": None, "footer": None, "invite_link": None}
    try:
        dbcol.insert_one(user_det)
    except:
        return True

#find any data from just query
def find_any(id,query):
    id = {"_id": id}
    x = dbcol.find(id)
    for i in x:
        try:
            result = i[f"{query}"]
            
        except Exception as ex:
            result = None
    
        return result

   
#add Dynamic DATA
def addDATA(chat_id,KEY, VALUE):
    dbcol.update_one({"_id": chat_id}, {"$set": {f"{KEY}": VALUE}})


#Delete DATA Dynamic
def delDATA(chat_id,KEY):
    dbcol.update_one({"_id": chat_id}, {"$set": {f"{KEY}": None}})

def getid():
    values = []
    for key in dbcol.find():
        id = key["_id"]
        values.append((id))
    return values


def delete(id):
    dbcol.delete_one(id)

