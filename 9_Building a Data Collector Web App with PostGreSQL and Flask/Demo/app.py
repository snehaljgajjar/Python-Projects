from flask import  Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)  #flask app name==> app here
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root123@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://njjlkjjgppsbkj:ec8cad48162cf04d86654569445f160f1014fc5e3256065be081f715ad7ddcc7@ec2-54-163-236-33.compute-1.amazonaws.com:5432/d37aktcaeunm7e?sslmode=require'
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
    if request.method =='POST':
        email=request.form["email_name"]
        height=request.form["height"]

        #print(request.form)
        if db.session.query(Data).filter(Data.email_var==email).count() ==0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()

            average_height= db.session.query(func.avg(Data.height_var)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height_var).count()
            send_email(email,height,average_height,count)
            return render_template("success.html")
    return render_template("index.html",
    text="Seems like we've got something from that email address already!")

if __name__=='__main__':
    app.debug=True
    app.run(port=18797)
