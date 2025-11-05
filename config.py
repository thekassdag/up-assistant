import os

def getDbPath():
    #return /app
    BaseDir = os.path.dirname(os.path.abspath(__file__))
    relativeDbPath = './db/UPAssistant.db'
    fullDbPath = os.path.join(BaseDir,relativeDbPath)
    
    return fullDbPath

APP_ADMIN_USERNAME='upadmin'
APP_ADMIN_PASSWORD='upadmin123'
DB_PATH=getDbPath()
