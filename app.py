from flask import Flask, render_template, redirect, request
from flask.helpers import url_for
app = Flask(__name__)

#url = "mailto:example@gmail.com?&subject=This is subject&body=This is body%0AThis is next line"

def helper(to,subject,body):
    string = "mailto:"+to+"?&subject="+subject+"&body="+body
    #print(url)
    url = convert_to_url_format(string)
    return url

def  convert_to_url_format(string):
    url = string.replace('\n','%0A')
    return url

@app.route("/", methods=["GET"])
def index():
    if request.method=='GET':
        return render_template("index.html")


@app.route("/leaveLetter", methods=["POST","GET"])
def leaveLetter():
    global url
    if request.method=='GET':
        return render_template("leaveLetter.html")
    if request.method=='POST':
        to = request.form['to'] 
        subject = request.form['subject']
        body = request.form['body']
        #fullname = request.form['fullname']
        url = helper(to,subject,body)
        return redirect(url) 
        
@app.route("/requestDocs", methods=["POST","GET"])
def requestDocs():
    global url
    if request.method=='GET':
        return render_template("requestDocs.html")
    if request.method=='POST':
        to = request.form['to'] 
        subject = request.form['subject']
        body = request.form['body']
        url = helper(to,subject,body)
        return redirect(url) 

if __name__=="__main__":   
    app.run(debug=True)