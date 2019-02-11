import os
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

account_sid = "ACf39ad1ed1ee546bd2e656d56ab89ab7a"
auth_token = "a0fb3871c2a7f899e0e73280eed2f2ea"

@app.route("/", methods=['GET'])
def hello():
	return "Hello Pyhton Flask"

@app.route("/sms", methods=['POST'])
def send_otp_sms():
	request_data = request.get_json()
	print(request_data['To'])
	print(request_data['Body'])
	client = Client(account_sid,auth_token)

	message = client.messages.create(
	to= request_data['To'],
	from_= "+12092523518",
	body=request_data['Body']
	)
	print(message.sid)
	return str(message.sid)

if __name__ == "__main__":
    app.run(debug=True)