import folium
import pandas

df = pandas.read_csv("Volcanoes_USA.txt")
map=folium.Map(location=[df['LAT'].mean(), df['LON'].mean()],zoom_start=6,tiles='Stamen Terrain')

def color(elevation):
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV'])-min(df['ELEV']))/3)
    if elevation in range (minimum , minimum+step) :
        return 'green'
    elif elevation in range(minimum+step , minimum+step*2):
        return 'orange'
    else :
        return 'red'
fg = folium.FeatureGroup(name ="Volcanoes Locations")

for lat,lon,name,elev in zip(df['LAT'] , df['LON'] , df['NAME'] , df['ELEV']):
    #map.simple_marker(location =[lat,lon], popup = name , marker_color = color(elev))
    fg.add_child(folium.Marker(location =[lat,lon], popup = name , icon = folium.Icon(color(elev),icon_color='green')))

map.add_child(fg)
map.add_child(folium.GeoJson(data=open('World_population.json'),
name = 'World Population',
style_function=lambda x:{'fillColor' : 'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005']< 20000000 else 'red'}))
#map.create_map(path = 'test.html')

map.add_child(folium.LayerControl())
map.save(outfile='test.html')
