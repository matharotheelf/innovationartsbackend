import boto3
from app import app

@app.route("/posttos3", methods=['POST'])
def posttos3():
    json = '{ "name":"John", "age":30, "city":"New York"}'
    s3 = boto3.resource('s3')
    object = s3.Object('innovationarts', 'json.txt')
    object.put(Body=json)
    return "done"
