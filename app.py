from flask import Flask, render_template, redirect, request
from flask.helpers import url_for
app = Flask(__name__)

#url = "mailto:abhishekanavekar32@gmail.com?&subject=This is subject&body=This is body%0AThis is next line"

def helper(fullname,to,subject,body):
    string = "mailto:"+to+"?&subject="+subject+"&body="+body+fullname+"\n\n"
    #print(url)
    url = convert_to_url_format(string)
    return url

def  convert_to_url_format(string):
    url = string.replace('\n','%0A')
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