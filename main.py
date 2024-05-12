from aa_flight_paths import aa_flight_paths
from global_companies_map import global_companies_map
from state_city_map import state_city_scatter_mapbox, state_city_choropleth_mapbox
import streamlit as st

st.set_page_config(layout="wide")
st.title("GHW Data Week - 2024")

SIDEBAR_DICT = {
    "GLOBAL COMPANIES MAP": global_companies_map,
    "AA FLIGHT PATHS": aa_flight_paths,
    "STATE-CITY SCATTER MAP": state_city_scatter_mapbox,
    "STATE-CITY CHOROPLETH MAP": state_city_choropleth_mapbox,
}


def main():
  chart_type = st.sidebar.radio("Select chart type:", SIDEBAR_DICT.keys())
  SIDEBAR_DICT[chart_type]()


if __name__ == "__main__":
  main()
