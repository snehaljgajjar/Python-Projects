import pandas
import geopy
from geopy.geocoders import Nominatim
nom = Nominatim()
file_name = "Book1.csv"
df = pandas.read_csv(file_name)
#df["Cordinates"] = df["Address"].apply(nom.geocode)
def geoLatLong(df,column_name):
    df["Latitude"] = df[column_name].apply(nom.geocode).apply(lambda x: x.latitude if x != None else None)
    df["Longnitude"] = df[column_name].apply(nom.geocode).apply(lambda x: x.longitude if x != None else None)
    df.to_csv("new_"+file_name)
    html_code = df.to_html()

for item in df.columns:
    if item == "Address":
        column_name = "Address"
        geoLatLong(df,column_name)
        break
        #print("File has column Address")
    elif item =="address":
        column_name = "address"
        geoLatLong(df,column_name)
        break
        #print("File has column address")
    else:
        print("Column is not equal address/Address")

print("File is ready to download")
#df.drop("Cordinates")
#print (df.columns)
#print("Table contains")
#print(df)
#list_columns = df.columns
