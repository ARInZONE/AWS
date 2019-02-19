import boto3
from botocore.exceptions import ClientError
import csv
count =0
# open the sender csv file for sender email ids with respective key and id 
with open('em_sender_credentials_aws.csv') as File:
  reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
  header = next(reader)
  for row in reader:
    sender_email_ids=row[0]
    print sender_email_ids
    sender_email_ids=row[0]
    aws_access_id=row[1]
    aws_key_id=row[2]
    email_accounts_limit=row[3]
    print aws_access_id
    print aws_key_id
    # writes the key and id to /.aws/credentials file
    key= open("/home/arinzone/.aws/credentials", "w")
    key.write('[default]\naws_access_key_id = '+aws_access_id+'\naws_secret_access_key = '+aws_key_id)
    key.close()
    # open the receiver's csv file for email ids and names
    with open('em_recipient_email_ids.csv') as File2:
      reader = csv.reader(File2, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
      header = next(reader)
      for row in reader:
        receiver_email_ids=row[0]
        print email_accounts_limit
        print "\t"+receiver_email_ids
        with open('em_email_body.csv') as File3:
            reader = csv.reader(File3,delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
            header = next(reader)
            for row in reader:
                body_subject=row[0]
                file_path=row[1]
                cc=row[2]
                bcc=row[3]
                email_body=row[4]
                print body_subject
                # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
                AWS_REGION = "us-west-2"
                # Create a new SES resource and specify a region.
                client = boto3.client('ses',region_name=AWS_REGION)
                # Try to send the email.
                try:
                    count+=1
                    print count
                    #Provide the contents of the email.
                    response = client.send_raw_email(
                    RawMessage={
                        'Data': 'From: '+sender_email_ids+'\nTo: '+receiver_email_ids+'\nSubject:'+body_subject+'\nMIME-Version: 1.0\nContent-type: Multipart/Mixed; boundary="NextPart"\n\n--NextPart\nContent-Type: text/plain\n\n'+email_body+'\n\n--NextPart\nContent-Type: text/plain;\nContent-Disposition: attachment; filename=\"'+file_path+'\"\n\nAttachment:\n\n--NextPart--',
                    }
                    #ConfigurationSetName='string'
                )
                # Display an error if something goes wrong. 
                except ClientError as e:
                    print(e.response['Error']['Message'])
                else:
                    print("Email sent! Message ID:"),
                    print(response['MessageId'])

