
# coding: utf-8

# In[23]:

from pandas_datareader import data
import datetime
from bokeh.plotting import figure,show,output_file
from  bokeh.embed import components
from bokeh.resources import CDN #content delivary network

start_date=datetime.datetime(2016,11,1)
end_date=datetime.datetime(2017,1,25)
df=data.DataReader(name="AAPL",data_source="yahoo",start=start_date,end=end_date)


def inc_dec(c,o):
    if c>o:
        value="Increase"
    elif c<o:
        value="Decrease"
    else :
        value="Equal"
    return value

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df["Middle"] =(df.Open+df.Close)/2
df["Height"] = abs(df.Close-df.Open)

p=figure(x_axis_type='datetime',width=1000,height=300,responsive=True)
p.title.text="Candlestick Chart"
p.grid.grid_line_alpha=0.3
#df.index[df.Close>df.Open]

hours_12 = 12*60*60*1000

p.segment(df.index,df.High,df.index,df.Low,color="Black")

p.rect(df.index[df.Status=="Increase"],
       df.Middle[df.Status=="Increase"],hours_12,df.Height[df.Status=="Increase"],
      fill_color="#00FFFF",line_color="black")

p.rect(df.index[df.Status=="Decrease"],
        df.Middle[df.Status=="Decrease"],
       hours_12,df.Height[df.Status=="Decrease"],
      fill_color="#FF4500",line_color="black")

script1,div1 = components(p)
cdn_js= CDN.js_files
cdn_css=CDN.css_files
cdn_js[0]
cdn_css[0]


# In[24]:




# In[22]:




# 
