import base64
import json

x=""" 
{
	"Records": [ 
        {
            "SequenceNumber": "49622964956294716863648450629069557626908440027692269570",
            "ApproximateArrivalTimestamp": 1634216929.114,
            "Data": "ZGV2MX5yZXN1bHR+MTAw",
            "PartitionKey": "1"
        },
        {
            "SequenceNumber": "49622964956294716863648450629070766552728055550220173314",
            "ApproximateArrivalTimestamp": 1634216941.635,
            "Data": "ZGV2MX5yZXN1bHR+MTAx",
            "PartitionKey": "1"
        }
    ]
}

"""

event=json.loads(x)


for record in event["Records"]:
    decoded_data = base64.b64decode(record["Data"]).decode("utf-8")

    print(decoded_data)
    # Record 1: Hello, this is a test.
    # Record 2: This is only a test.