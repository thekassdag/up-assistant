#flask components
from flask import Flask
from flask import redirect,url_for

#controller
import Controller_Auth
import Controller_Logout
import Controller_AdminDashboard
import Controller_AdminOperation
import Controller_StudentDashboard
import Controller_StudentOperation

app = Flask(__name__)

#flask configs
app.template_folder = './views'
app.static_folder = './public'
app.secret_key = 'up-assistant-9483380290292-secret'

@app.route('/')
def home():
    return redirect(url_for('studentDashboard'))

#login url for admin 
@app.route('/login/admin/',methods=['GET'])
def adminLogin():
    return Controller_Auth.adminLoginForm()

#admin login page handler
@app.route('/login/admin/',methods=['POST'])
def adminLoginFormHandler():
    return Controller_Auth.adminLoginFormHandler()

#admin Dashboard page
@app.route('/admin')
def adminDashboard():
    return Controller_AdminDashboard.adminDashboard()

#admin operation pages=import operation
@app.route('/admin/importStdList',methods = ['POST'])
def importStdList():
    return Controller_AdminOperation.importStdList()

#admin operation pages=export operation
@app.route('/admin/exportUPData/<stream>',methods=['post'])
def exportUPData(stream):
    return Controller_AdminOperation.exportUPData(stream)

#logoutFrom --std/admin account
@app.route('/logout/<logoutFrom>')
def logout(logoutFrom):
    return Controller_Logout.logout(logoutFrom)

#student login page
@app.route('/login/student/',methods=['GET'])
def studentLogin():
    return Controller_Auth.stdLoginForm()

#student login page handler
@app.route('/login/student/',methods=['POST'])
def studentLoginFormHandler():
    return Controller_Auth.stdLoginFormHandler()

#student dashboard page
@app.route('/student/')
def studentDashboard():
    return Controller_StudentDashboard.stdDashboard()

@app.route('/student/filedInUv',methods = ['POST'])
def getFiledInUv():
    return Controller_StudentOperation.getFiledInUv()

@app.route('/student/galleryInUv',methods = ['POST'])
def getGalleryInUv():
    return Controller_StudentOperation.getGalleryInUv()

@app.route('/student/insertUp',methods = ['POST'])
def insertUp():
    return Controller_StudentOperation.insertUp()


#Run the app
if __name__ == '__main__':
    app.run(debug=True)