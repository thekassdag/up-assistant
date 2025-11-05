import sqlite3

#app config
from config import DB_PATH

con = sqlite3.connect(DB_PATH,check_same_thread=False)

def stdList():
    cur = con.cursor()
    res = cur.execute('SELECT * FROM student')
    return res.fetchall()

def getStudent(admissionId):
    cur = con.cursor()
    res = cur.execute(f'SELECT admissionId,fullName,stream FROM student WHERE admissionId={int(admissionId)}')
    return res.fetchmany()

def addStudents(stdData):
    cur = con.cursor()
    cur.execute('DELETE FROM student')
    cur.execute('DELETE FROM sqlite_sequence WHERE name="student"')
    
    cur.executemany("INSERT INTO  student(id,fullName,admissionId,stream) VALUES(NULL,?,?,?)",stdData)
    con.commit()

def getUPStatusOfStd(stdId):
    cur = con.cursor()
    res = cur.execute('SELECT count(id) FROM UpOrder WHERE studentId=?',(stdId,))
    return res.fetchone()[0]

#get total std that submited theri upData
def getTotalUPSubmittedStd():
    cur = con.cursor()
    res = cur.execute('SELECT student.admissionId,student.fullName FROM student INNER JOIN UpOrder ON student.admissionId=UpOrder.studentId ORDER BY student.fullName')
    submittedStds = res.fetchall()
    
    totalStd = len([*set(submittedStds)])
    return totalStd

#get uv order num of one std by using std id
def getStdUpOrder(stdId):
    cur = con.cursor()
    res = cur.execute('SELECT UpOrder.listOrder FROM UpOrder LEFT JOIN universty ON UpOrder.uvId=universty.id WHERE UpOrder.studentId=? ORDER BY universty.abrName',(stdId,))
    return res.fetchall()

#get std aId,name who submitted up-data
def getUPSubmittedStd(stream):
    cur = con.cursor()
    res = cur.execute('SELECT student.admissionId,student.fullName FROM student INNER JOIN UpOrder ON student.admissionId=UpOrder.studentId WHERE student.stream=? ORDER BY student.fullName',(stream.upper(),))
    submittedStds = res.fetchall()
    
    return [*set(submittedStds)]
           
