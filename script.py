import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")

# Adding multiple markers: use loop or add them manually
# fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi i am a Marker", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[38.2, -98.2], popup="Hi i am a second Marker", icon=folium.Icon(color='green')))

# for coordinates in[[38.2, -99.1],[38.2, -98.2]]:
    # fg.add_child(folium.Marker(location=coordinates, popup="Hi i am a Marker", icon=folium.Icon(color='green')))

def color_producer(elevation):
    if elevation < 1000:
          return "green"
    elif  1000 <= elevation < 3000:
          return "orange"
    else:
          return "red"

for lt, ln, el in zip(lat, lon, elev):
        fg.add_child(folium.Marker(location=[lt, ln], popup=f"The elevation is {el} m", icon=folium.Icon(color=color_producer(el))))


fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fg)

map.save("Map1.html")
