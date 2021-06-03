import os
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import boto3
import random


s3_client = boto3.resource('s3')





# Define a flask app
app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        
        key = random.randint(1, 10)

        s3_client.meta.client.upload_file(
            Filename=file_path,
            Bucket='khangt1k25-aws-challenge',
            Key=str(key)
        )

        result = "Done, Uploaded!"
        return result

    return "False, try again!"


if __name__ == '__main__':
    app.run(debug=True)