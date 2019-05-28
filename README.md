# Innovation Arts Backend Test
Creating an API with Flask and AWS

## Description

This app allows the user to post to and view an API. It has the following features:
* Users can upload a JSON body input to S3 using a POST request.
* Users can access this JSON body input from S3 using a GET request.

## Tech Stack

Python 3.7.2, Flask, Boto3, AWS S3

**Deployment**

AWS Lambda with Zappa

## Quickstart Local

To clone this repository and start the server:

```bash
$ git clone https://github.com/matharotheelf/innovationartsbackend
$ cd innovationartsbackend
$ python3 

```
To upload the JSON body input '{"username":"xyz","password":"xyz"}' to S3:

```bash
$ curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"xyz","password":"xyz"}' \
    http://127.0.0.1:5000/posttos3/

```

You can replace the above JSON body input with any.

To access the uploaded JSON body input, input http://127.0.0.1:5000/ in any browser.

## How to Use

The code is deployed to AWS Lambda so can be accessed remotely.

Similarly to locally, to upload the JSON body input '{"username":"xyz","password":"xyz"}' to S3:

```bash
$ curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"xyz","password":"xyz"}' \
    https://1d7ci3alv5.execute-api.eu-west-2.amazonaws.com/dev/posttos3/

```

You can replace the above JSON body input with any.

To access the uploaded JSON body input, input https://1d7ci3alv5.execute-api.eu-west-2.amazonaws.com/dev in any browser.

## User Stories
```
As a User 
So I can upload data, I can upload a JSON body input to S3 using a POST request.
So I can access data , I can access this JSON body input from S3 using a GET request.

```

## References

Learning Flask:

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

https://stackoverflow.com/questions/45476139/how-to-make-a-post-request-in-flask-post-method

http://flask.pocoo.org/docs/1.0/quickstart/

Uploading data to S3:

https://stackoverflow.com/questions/40336918/how-to-write-a-file-or-data-to-an-s3-object-using-boto3

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.upload_file

Reading data from S3:

https://stackoverflow.com/questions/40995251/reading-an-json-file-from-s3-using-python-boto3

Deploying to AWS Lambda:

https://books.agiliq.com/projects/django-deployments-cookbook/en/latest/using_zappa_lambda_aurora.html

https://www.freecodecamp.org/news/how-to-create-a-serverless-service-in-15-minutes-b63af8c892e5/

## Contributors 

[Tom Lawrence](https://github.com/matharotheelf)  

## How to Contribute

If you want to improve this project and see your name added to the above list of contributors, simply branch this repo, change the code, and make a pull request back to this repo explaining the contributions you made.
