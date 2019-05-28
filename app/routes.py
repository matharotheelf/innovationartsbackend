import boto3
from flask import request
from app import app

@app.route("/posttos3/", methods=['POST'])
def posttos3():
    json = request.data
    s3 = boto3.resource('s3')
    object = s3.Object('innovationarts', 'json.txt')
    object.put(Body=json)
    return "Done"

@app.route("/")
def getfroms3():
    s3 = boto3.resource('s3')
    content_object = s3.Object('innovationarts', 'json.txt')
    return content_object.get()['Body'].read().decode('utf-8')
