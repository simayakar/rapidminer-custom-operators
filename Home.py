import streamlit as st
import pandas as pd
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(layout="wide")

sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

nav = get_nav_from_toml(
    "/Users/simoyland/rapidminer-custom-operators/pages_sections.toml" if sections else "/Users/simoyland/rapidminer-custom-operators/pages_sections.toml"
)

st.logo("images/logo.png")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()
