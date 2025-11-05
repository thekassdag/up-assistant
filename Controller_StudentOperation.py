from flask import request
import json

#modal
import Modal_uv

def getFiledInUv():
    uvId = request.form['uvId']
    return Modal_uv.getFieldsInUv(uvId)

def getGalleryInUv():
    uvId = request.form['uvId']
    return Modal_uv.getGalleryInUv(uvId)

def insertUp():
    upData = request.form['upData']
    upData = json.loads(upData)
    
    Modal_uv.insertUp(upData)
    
    return "okay"