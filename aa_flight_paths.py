import pandas as pd
import folium
from folium.features import CustomIcon
import streamlit as st
import streamlit.components.v1 as components

PATH_TO_DATA = "aa_flights_paths_data.csv"


def aa_flight_paths():
  # add a subtitle
  st.subheader("AA Flight Paths")
  # load data from CSV into dataframe
  flight_paths = pd.read_csv(PATH_TO_DATA)
  # add a column called row_id at the beginning
  flight_paths.insert(0, 'row_id', range(1, 1 + len(flight_paths)))
  # display data on web in a table
  st.dataframe(flight_paths, hide_index=True)
  map = folium.Map(location=(37.09, -95.71),
                   zoom_start=4,
                   tiles="cartodb positron")
  # define a list of colors
  colors = [
      'red', 'green', 'blue', 'purple', 'orange', 'darkred', 'pink',
      'darkblue', 'beige', 'lightred', 'darkgreen', 'lightgreen', 'lightblue',
      'gray', 'lightpink', 'darkpink', 'white', 'cyan', 'magenta'
  ]
  color_index = 0
  # iterate over the dataframe rows
  for index, row in flight_paths.iterrows():
    # start and end coordinates
    start_coords = (row['start_lat'], row['start_lon'])
    end_coords = (row['end_lat'], row['end_lon'])
    # select a color for the airline
    color = colors[color_index % len(colors)]
    color_index += 1
    # draw a line
    line = folium.PolyLine(
        locations=[start_coords, end_coords],
        color=color,
        weight=1,
        popup=f"{row['row_id']}: {row['airport1']} to {row['airport2']}")
    # add line to map
    map.add_child(line)
    # calculate mid-point
    midpoint = [(start_coords[0] + end_coords[0]) / 2,
                (start_coords[1] + end_coords[1]) / 2]
    icon_url = "https://cdn.iconscout.com/icon/free/png-512/free-plane-3802463-3168528.png"
    icon = CustomIcon(icon_url, icon_size=(24, 24))
    folium.Marker(
        location=midpoint,
        icon=icon,
        popup=f"{row['row_id']}: {row['airport1']} to {row['airport2']}"
    ).add_to(map)
  # save it as HTML
  map.save("flight_paths.html")
  # Open the HTML file and read
  HtmlFile = open("flight_paths.html", "r", encoding="utf-8")
  my_map = HtmlFile.read()
  components.html(my_map, height=700)

"""
# CHALLENGE: create a random_colour_generator() function, which replaces colors array, and can be used to colour the lines
"""