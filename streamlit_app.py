import networkx as nx
import osmnx as ox
import geopandas as gpd
place_name="Al Taif, Makkah Region, Saudi Arabia"
place_name='Makkah Al Mukarramah, Makkah Region, Saudi Arabia'

ubc = (ox.geometries_from_place(place_name, tags={'building':True})
         .loc[:, ["geometry"]]                 # just keep the geometry column for now
         .query("geometry.type == 'Polygon'")  # only what polygons (buidling footprints)
         .assign(Label="Building Footprints")  # assign a label for later use
         .reset_index(drop=True)               # reset to 0 integer indexing
      )
ubc.head()
import plotly.express as px
fig = px.choropleth_mapbox(ubc, geojson=ubc.geometry, locations=ubc.index, color="Label",
                           center={"lat": 21.422510, "lon": 39.826168}, zoom=12.5,
                           mapbox_style="open-street-map")
fig.update_layout(margin=dict(l=0, r=0, t=30, b=10))
st.write(fig) 
