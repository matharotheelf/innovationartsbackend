import boto3
from app import app
import json

@app.route("/posttos3", methods=['POST'])
def posttos3():
    json = '{ "name":"John", "age":30, "city":"New York"}'
    s3 = boto3.resource('s3')
    object = s3.Object('innovationarts', 'json.txt')
    object.put(Body=json)
    return "done"

@app.route("/")
def getfroms3():
    s3 = boto3.resource('s3')
    content_object = s3.Object('innovationarts', 'json.txt')
    file_content = content_object.get()['Body'].read().decode('utf-8')
    return file_content
