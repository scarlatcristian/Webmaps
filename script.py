import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6)


def color_producer(elevation):
    if elevation < 1000:
          return "green"
    elif  1000 <= elevation < 3000:
          return "orange"
    else:
          return "red"

fg_volcanoes = folium.FeatureGroup(name="Volcanoes")

# Add Color Dots for Volcanoes
for lt, ln, el in zip(lat, lon, elev):
        fg_volcanoes.add_child(folium.CircleMarker(location=[lt, ln], popup=f"The elevation is {el} m", fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))


fg_population = folium.FeatureGroup(name="Population")

# Color Areas By Population Number
fg_population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg_volcanoes)
map.add_child(fg_population)
# Turn off volcanoes/population filter 
map.add_child(folium.LayerControl())

map.save("Map1.html")
