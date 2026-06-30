import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Hidden Energy Behind World Cup 2026",
    page_icon="⚽",
    layout="wide",
)

st.title("⚽ Hidden Energy Behind World Cup 2026")

st.markdown(
    """
    How much energy does the world's biggest sporting event actually consume?

    This project estimates the hidden energy footprint of FIFA World Cup 2026 using public data and transparent assumptions.
    """
)

st.divider()

# -----------------------------
# Load match dataset
# -----------------------------

matches = pd.read_csv("data/matches.csv")

total_matches = 104
games_played = len(matches)
total_energy_mwh = matches["estimated_energy_mwh"].sum()

# Temporary placeholder assumption:
# 1 US household uses around 10 MWh of electricity per year.
annual_home_energy_mwh = 10
equivalent_homes = total_energy_mwh / annual_home_energy_mwh

top_match = matches.sort_values(
    by="estimated_energy_mwh",
    ascending=False
).iloc[0]

# -----------------------------
# KPI cards
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Games in Dataset", f"{games_played} / {total_matches}")

with col2:
    st.metric("Estimated Stadium Energy", f"{total_energy_mwh:,.0f} MWh")

with col3:
    st.metric("Equivalent Homes / Year", f"{equivalent_homes:,.1f}")

st.divider()

# -----------------------------
# Top energy match
# -----------------------------

st.subheader("⚡ Highest Energy Match So Far")

st.markdown(
    f"""
    **{top_match["home_team"]} vs {top_match["away_team"]}**  
    Stadium: **{top_match["stadium"]}**, {top_match["city"]}  
    Estimated energy: **{top_match["estimated_energy_mwh"]} MWh**
    """
)

st.divider()

# -----------------------------
# Match table
# -----------------------------

st.subheader("Match Energy Dataset")

st.dataframe(matches, use_container_width=True)

st.info(
    "🚧 Model V0: This dataset uses simplified match-level energy assumptions. "
    "Future versions will estimate energy based on stadium type, attendance, weather, travel, broadcasting, and streaming."
)