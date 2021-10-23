import boto3
import json
import base64

gRegionName="us-east-1"
gQueueURL=None

# create queue
def createQueue(queueName):
    sqsClient = boto3.client("sqs", region_name=gRegionName)
    response = sqsClient.create_queue(
        QueueName=queueName,
        Attributes={
            "DelaySeconds": "0",
            "VisibilityTimeout": "120",  
        }
    )
    print(response)

# get queue URL
def getQueueURL(queueName):
    try: 
        sqsClient = boto3.client("sqs", region_name=gRegionName)
        response = sqsClient.get_queue_url(
            QueueName=queueName,
        )
        return response["QueueUrl"]
    except:
        return None

# send message to queue
def sendMessage():
    sqsClient = boto3.client("sqs", region_name=gRegionName)
    message = {"deviceID": "dev1", "temp": 100}
    response = sqsClient.send_message(QueueUrl=gQueueURL,MessageBody=json.dumps(message)
    )
    print(response)

# delete queue
def deleteQueue():
    sqsClient = boto3.client("sqs", region_name=gRegionName)
    response = sqsClient.delete_queue(QueueUrl=gQueueURL)
    print(response)

def receiveMessages():
    sqs_client = boto3.client("sqs", region_name=gRegionName)
    response = sqs_client.receive_message(
        QueueUrl=gQueueURL,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10,
    )

    print(f"Number of messages received: {len(response.get('Messages', []))}")

    for message in response.get("Messages", []):
        message_body = message["Body"]
        print(f"Message body: {json.loads(message_body)}")
        #print(f"Receipt Handle: {message['ReceiptHandle']}")
        

# queue Name
queueName="raj-sqs-1"

# get queue URL
gQueueURL = getQueueURL(queueName)

# create queue if not
if gQueueURL is None:    
    createQueue(queueName)

# get queue URL
gQueueURL = getQueueURL(queueName)
print('Your queue is ' + gQueueURL)

# send a message
sendMessage()
receiveMessages()

#deleteQueue()


