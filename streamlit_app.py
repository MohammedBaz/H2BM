
import networkx as nx
! pip install osmnx
import osmnx as ox
! pip install geopandas
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


#buildings = ox.geometries_from_place(place_name, tags={
#'building':True
#})


#ax = ubc.plot(figsize=(8, 8), column="Label", legend=True,
#              edgecolor="0.2", markersize=200, cmap="rainbow")
#import matplotlib.pyplot as plt
#plt.title("UBC");
#! pip install contextily
#import contextily as ctx
#ax = (ubc.to_crs("EPSG:3857")
#         .plot(figsize=(10, 8), column="Label", legend=True,
#               edgecolor="0.2", markersize=200, cmap="rainbow")
#     )
#ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)  # I'm using OSM as the source. See all provides with ctx.providers
#plt.axis("off")
#plt.title("UBC");
import plotly.express as px
fig = px.choropleth_mapbox(ubc, geojson=ubc.geometry, locations=ubc.index, color="Label",
                           center={"lat": 21.422510, "lon": 39.826168}, zoom=12.5,
                           mapbox_style="open-street-map")
fig.update_layout(margin=dict(l=0, r=0, t=30, b=10))
