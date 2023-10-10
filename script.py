import folium


map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")

# Adding multiple markers: use loop or add them manually
# fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi i am a Marker", icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[38.2, -98.2], popup="Hi i am a second Marker", icon=folium.Icon(color='green')))

for coordinates in[[38.2, -99.1],[38.2, -98.2]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi i am a Marker", icon=folium.Icon(color='green')))    


map.add_child(fg)

map.save("Map1.html")
