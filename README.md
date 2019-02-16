# AWS
Install pip in ubuntu:

$ sudo apt-get install python-pip python-dev build-essential 

$ sudo pip install --upgrade pip 

$ sudo pip install --upgrade virtualenv

Install the latest Boto 3 release via pip:

$ pip install boto3

You may also install a specific version:

$ pip install boto3==1.0.0

create the credential file yourself. By default, its location is at ~/.aws/credentials:

[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY

change your id and key value accordingly 

Edit the file amazon-ses-sample.py content 

SENDER = "<sender aws email>"
RECIPIENT = "<receiver email>"

execute the code in terminal by :

$python  amazon-ses-sample.py 
