#flask component
from flask import session,url_for,redirect
from flask import render_template as view

#modal
from Modal_Student import stdList,getTotalUPSubmittedStd,getUPStatusOfStd
from Modal_Student import getStdUpOrder,getUPSubmittedStd
from Modal_uv import getUv

#check if admin is login
def adminPageMiddleware(adminDashboardView):
    #if admin loing redi to dashboard
    if 'APP_ADMIN_USERNAME' in session:
        return adminDashboardView
    #other ways redi to admin login page
    else:
        return redirect(url_for('adminLogin'))

#admin dashboard page
def adminDashboard():
    #get std lis from the modal
    studentList = stdList()
    totalUPSubmittedStd = getTotalUPSubmittedStd()
    adminDashboardView = view('adminDashboard.html',data={
        'stdList':studentList,
        'numStd':len(studentList),
        'upStatusOfStd':getUPStatusOfStd,
        'totalUPSubmittedStd':totalUPSubmittedStd,
        'totalUPNotSubmittedStd':(len(studentList) - totalUPSubmittedStd)
    },data2={
        'getUvFor':getUv,
        'getUPSubmittedStd':getUPSubmittedStd,
        'getStdUpOrder':getStdUpOrder
    })
    return adminPageMiddleware(adminDashboardView)