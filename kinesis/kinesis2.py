import base64
import json

with open('records.json') as json_file:
	event = json.load(json_file)
	for record in event["Records"]:
		decoded_data = base64.b64decode(record["Data"]).decode("utf-8")
		print(decoded_data)