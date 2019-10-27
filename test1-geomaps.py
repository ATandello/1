import osmnx as ox

import matplotlib.pyplot as plt

place_name = "Kamppi, Helsinki, Finland"

graph = ox.graph_from_place('kujawsko_pomorskie_latest.osm.pbf')

type(graph)