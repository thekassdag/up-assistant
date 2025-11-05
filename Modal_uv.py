import sqlite3

#app config
from config import DB_PATH

con = sqlite3.connect(DB_PATH,check_same_thread=False)

#get uv list for def stream e.g social/nat
def getUv(uvFor):
    cur = con.cursor()
    res = cur.execute('SELECT * FROM universty WHERE uvFor="NS" OR uvFor=? ORDER BY abrName',uvFor.upper())
    return res.fetchall()

def getFieldsInUv(uvId):
    cur = con.cursor()
    res = cur.execute('SELECT fieldName FROM fileldInUV WHERE uvId=?',str(uvId))
    return res.fetchall()

def getGalleryInUv(uvId):
    cur = con.cursor()
    res = cur.execute('SELECT picLink FROM universtyGallery WHERE uvId=?',str(uvId))
    return res.fetchall()

def getUpOrder(stdId,stream):
    cur = con.cursor()
    res = cur.execute('SELECT UpOrder.listOrder,universty.id,universty.FullName,universty.abrName FROM UpOrder,universty,student WHERE student.admissionId=? AND student.admissionId=UpOrder.studentId AND UpOrder.uvId=universty.id ORDER BY UpOrder.listOrder ASC',[stdId,])
    upOrder = res.fetchall()
    
    query = cur.execute('SELECT etRank,id,FullName,abrName FROM universty WHERE uvFor="NS" OR uvFor=?',stream.upper())
    defaultOrder = query.fetchall()
    if(len(upOrder) > 0):
        return upOrder
    else:
        return defaultOrder

def insertUp(upData):
    stdId = upData[0][0]
    if(isStdInsertedUp(stdId) != True):
        cur = con.cursor()
        cur.executemany('INSERT INTO UpOrder VALUES(NULL,?,?,?)',upData)
        con.commit()
    else:
        updateUp(upData)

def updateUp(upData):
    i=0
    while i<len(upData):
        cur = con.cursor()
        cur.execute(f'UPDATE UpOrder SET listOrder={upData[i][2]} WHERE studentId={upData[i][0]} AND uvId={upData[i][1]}')
        i+=1

def isStdInsertedUp(stdId):
    cur = con.cursor()
    res = cur.execute('SELECT * FROM UpOrder WHERE studentId=?',(stdId,))
    if(len(res.fetchall()) > 0):
        return True
