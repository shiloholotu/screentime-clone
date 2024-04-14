from flask import Flask, render_template, request, url_for, redirect
from twilio.rest import Client
import os

account_sid = os.environ.get("ACC")
auth_token = os.environ.get("AUTH")
client = Client(account_sid, auth_token)




app = Flask(__name__)


@app.route("/")
def index():


    return render_template("index.html")


@app.route("/approved/<passcode>")
def approved(passcode):
     message = client.messages.create(
        from_='+18667167730',
        body=passcode,
        to='+18777804236'
    )
     
     return render_template("approved.html")



if __name__ == "__main__":
    app.run(debug=True)
