#flask component
from flask import render_template as view
from flask import request,session,url_for,redirect

#import app config file
import config

#modal
import Modal_Student

def adminLoginForm():
    #there is no form error in get req
    formError = ''
    return view('adminLogin.html',formError=formError)

def adminLoginFormHandler():
    #get user name and pwd from form data
    userName = request.form['username']
    password = request.form['password']
    
    #validating form
    formError = {}
    if(userName and password == ''):
        formError = {'password':'please input password'}
        formError = {'username' : 'please input username'}
    elif(userName == ''):
        formError = {'username' : 'please input username'}
    elif(password == ''):
        formError = {'password':'please input password'}
    elif(userName and password != ''):
        #check if username and pwd is correct
        appAdminUserName = config.APP_ADMIN_USERNAME
        appAdminPwd = config.APP_ADMIN_PASSWORD
        
        #on form submistion success
        if(userName == appAdminUserName and password == appAdminPwd):
            session['APP_ADMIN_USERNAME'] = userName
        else:
            formError = {'usernameOrPwdError':'username or password is incorrect'}
    
    if(len(formError) > 0):
        return view('adminLogin.html',formError=formError)
    else:
        #redirecting on success to admin page
        return redirect(url_for('adminDashboard'))

def stdLoginForm():
    #there is no form error in get req
    formError = {'id':'','fullName':''}
    return view('studentLogin.html',formError=formError)
    
def stdLoginFormHandler():
    formError = {'id':'','fullName':''}
    id = request.form['id']
    fullName = request.form['fullName']
    if(id  == ''):
        formError['id'] = 'please input ur id'
    elif(fullName == ''):
        formError['fullName'] = 'please input ur fullName'
    elif(id and fullName != ''):
        stdData = Modal_Student.getStudent(id)
        
        if(len(stdData) == 0):
            formError['id'] = 'please input correct id'
        else:
            stdId = stdData[0][0]
            stdName = stdData[0][1]
            
            stdName = stdName.lower().replace(" ", "").lstrip()
            fullName = fullName.lower().replace(" ","").lstrip()
            
            if(stdName == fullName):
                session['STD_ID'] = stdId
                return redirect(url_for('studentDashboard'))
            else:
                formError['fullName'] = 'please input correct fullName'
            
        
    return view('studentLogin.html',formError=formError)

