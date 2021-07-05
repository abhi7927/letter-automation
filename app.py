from flask import Flask, render_template, redirect, request
from flask.helpers import url_for
app = Flask(__name__)

#url = "mailto:abhishekanavekar32@gmail.com?&subject=This is subject&body=This is body%0AThis is next line"

def helper(fullname,to,subject,body):
    url = "mailto:"+to+"?&subject="+subject+"&body="+body+fullname
    #print(url)
    return url

@app.route("/", methods=["POST","GET"])
def home():
    global url
    if request.method=='GET':
        return render_template("index.html")
    if request.method=='POST':
        sender_name = request.form['fullname'] 
        to = request.form['to'] 
        subject = request.form['subject']
        body = request.form['body']
        url = helper(sender_name,to,subject,body)
        return redirect(url) 

if __name__=="__main__":
    app.run(debug=True)