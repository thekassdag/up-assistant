#flask
from flask import session,url_for,redirect

#del session from def account on logout page
def logout(logoutFrom):
    if (logoutFrom == 'admin'):
        #del
        session.pop('APP_ADMIN_USERNAME')
        #redirect
        return redirect(url_for('adminLogin'))
    
    elif(logoutFrom == 'std'):
        #del
        session.pop('STD_ID')
        #redirect
        return redirect(url_for('studentLogin'))