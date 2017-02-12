from flask import  Flask, render_template, request,send_file
import pandas
import geopy
from geopy.geocoders import Nominatim


app=Flask(__name__)  #flask app name==> app here

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success-table",methods=['POST'])
def success_table():

    global file
    if request.method =='POST':
        file=request.files["file"]
        df=pandas.read_csv("uploaded_" + file.filename)

        for item in df.columns:
            if item == "Address":
                column_name = "Address"
                break
            elif item =="address":
                column_name = "address"
                break
            else:
                column_name = "Not Found"
                #print("Please make sure you have an address column in your CSV file!")
        if column_name != "Not Found":
            nom = Nominatim()
            df["Latitude"] = df[column_name].apply(nom.geocode).apply(lambda x: x.latitude if x != None else None)
            df["Longnitude"] = df[column_name].apply(nom.geocode).apply(lambda x: x.longitude if x != None else None)
            df.to_csv("new_"+ file.filename)
            print("File is ready to download")
            table_code = df.to_html()
            return render_template("index.html" ,btn="download.html" ,text=table_code)

        show_text="Please make sure you have an address column in your CSV file!"
        return render_template("index.html",text=show_text)

@app.route("/download-file")
def download():
    return send_file("new_"+file.filename,attachment_filename="yourfile.csv",as_attachment=True)

if __name__=='__main__':
    app.debug=True
    app.run()
