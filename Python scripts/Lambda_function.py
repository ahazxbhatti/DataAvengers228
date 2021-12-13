import json

import boto3

import base64

#create glue client
client = boto3.client('glue')
#Create sns Client
clients = boto3.client('sns')
#Arn used for connectivity
topic_arn = 'arn:aws:sns:us-west-1:143812385682:DataInsertedSNSAlarm'

def lambda_handler(event, context) :
    try:
        #Function for 228 class
       client.start_crawler(Name='228S3Crawler')
       #Functions for  class
       
    except Exception as e:
        print(e)
        print('Error starting crawler')
        raise e
        
    try:
        clients.publish(TopicArn=topic_arn, Message='S3DataInsert', Subject='DataInsert')
        print('Successfully delivered alarm message')
    except Exception:
        print('Delivery failure')