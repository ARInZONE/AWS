import boto3
from botocore.exceptions import ClientError
import csv
with open('em_sender_credentials_aws.csv') as File:
  reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
  header = next(reader)
  for row in reader:
    sender_email_ids=row[0]
    print sender_email_ids
    sender_email_ids=row[0]
    aws_access_id=row[1]
    aws_key_id=row[2]
    print aws_access_id
    print aws_key_id
    key= open("/home/arinzone/.aws/credentials", "w")
    key.write('[default]\naws_access_key_id = '+aws_access_id+'\naws_secret_access_key = '+aws_key_id)
    key.close()
    with open('em_recipient_email_ids.csv') as File2:
      reader = csv.reader(File2, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
      header = next(reader)
      for row in reader:
        receiver_email_ids=row[0]
        print "\t"+receiver_email_ids
        # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        AWS_REGION = "us-west-2"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses',region_name=AWS_REGION)
        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = client.send_raw_email(
            RawMessage={
                'Data': 'From: '+sender_email_ids+'\nTo: '+receiver_email_ids+'\nSubject: Test email (contains an attachment)\nMIME-Version: 1.0\nContent-type: Multipart/Mixed; boundary="NextPart"\n\n--NextPart\nContent-Type: text/plain\n\nThis is the message body.\n\n--NextPart\nContent-Type: text/plain;\nContent-Disposition: attachment; filename="em_recipient_email_ids.csv"\n\nThis is the text in the attachment.\n\n--NextPart--',
            }
            #ConfigurationSetName='string'
        )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
