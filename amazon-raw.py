import boto3
from botocore.exceptions import ClientError
# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-east-1"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)
# sender email
sender_email_ids='sender@mail'
# receiver email
receiver_email_ids='reciver@mail'
#absolute attachment file path
file_path='file-path'
# Try to send the email.
try:
    #Provide the contents of the email.
    response = client.send_raw_email(
    RawMessage={
        'Data': 'From: '+sender_email_ids+'\nTo: '+receiver_email_ids+'\nSubject: Test email (contains an attachment)\nMIME-Version: 1.0\nContent-type: Multipart/Mixed; boundary="NextPart"\n\n--NextPart\nContent-Type: text/plain\n\nThis is the message body.\n\n--NextPart\nContent-Type: text/plain;\nContent-Disposition: attachment; filename='+file_path+'\n\nThis is the text in the attachment.\n\n--NextPart--',
    }
    #ConfigurationSetName='string'
)
# Display an error if something goes wrong.	
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])
