import folium
import pandas

data=pandas.read_csv("Volcanoes_USA.txt")

latitude=list(data["LAT"])
longitude=list(data["LON"])

elevation_height=list(data["ELEV"])

def color_distributor(elevation):
    if elevation<1000:
        return 'green'
    elif elevation<3000 and elevation>=1000:
        return 'orange'
    else:
        return 'red'
map=folium.Map(Location=[22.57,88.35],zoom_start=10,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Volcanoes in USA")
for lat,lon,elev in zip(latitude,longitude,elevation_height):
    fgv.add_child(folium.Marker(location=[lat,lon],popup=str(elev)+" m",icon=folium.Icon(color=color_distributor(elev))))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")
