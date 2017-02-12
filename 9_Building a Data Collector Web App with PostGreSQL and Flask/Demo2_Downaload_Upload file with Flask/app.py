from flask import  Flask, render_template, request,send_file
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug  import secure_filename

app=Flask(__name__)  #flask app name==> app here
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root123@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']= #path of heroku databse
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_var=db.Column(db.String(120),unique=True)
    height_var=db.Column(db.Integer)

    def __init__(self, email_var, height_var):
        self.email_var = email_var
        self.height_var = height_var

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success",methods=['POST'])
def success():
    global file
    if request.method =='POST':
        email=request.form["email_name"]
        file=request.files["file"]
        file.save(secure_filename("uploaded_" + file.filename))
        #with open("uploaded_"+file.filename,"a") as f:
        #    f.write("This was added later!")
        content=type(file.read())
        print(content)
        return render_template("index.html" ,btn="download.html")
@app.route("/download")
def download():
    return send_file("uploaded_"+file.filename,attachment_filename="yourfile.csv",as_attachment=True)

if __name__=='__main__':
    app.debug=True
    #app.run(port=18797)
    app.run()
