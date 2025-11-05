#flask component
from flask import session,url_for,redirect
from flask import render_template as view

#modal
import Modal_Student
import Modal_uv

#std dashboard page
def stdDashboard():
    if 'STD_ID' in session:
        stdId = session['STD_ID']
        stdInfo = Modal_Student.getStudent(stdId)
        
        #stream => stdInfo[0][2]
        stream = stdInfo[0][2]
        allUv = Modal_uv.getUv(stream)

        stdDashboardView = view('studentDashboard.html',data={
            'stdInfo':stdInfo,
            'allUv':allUv,
            'fieldsInUv':Modal_uv.getFieldsInUv,
            'upOrders':Modal_uv.getUpOrder
        },stream=stream)
        
        return stdDashboardView
    
    return redirect(url_for('studentLogin'))