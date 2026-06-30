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
# Model assumptions - V0
# -----------------------------

total_matches = 104

scenario = st.radio(
    "Choose energy scenario",
    ["Low", "Base", "High"],
    horizontal=True,
)

energy_per_match = {
    "Low": 30,
    "Base": 60,
    "High": 100,
}

games_played = st.slider(
    "Games played",
    min_value=0,
    max_value=104,
    value=1,
)

energy_per_match_mwh = energy_per_match[scenario]
total_energy_mwh = games_played * energy_per_match_mwh

# Temporary placeholder assumption
annual_home_energy_mwh = 10
equivalent_homes = total_energy_mwh / annual_home_energy_mwh

# -----------------------------
# KPI cards
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Games Played", f"{games_played} / {total_matches}")

with col2:
    st.metric("Estimated Stadium Energy", f"{total_energy_mwh:,.0f} MWh")

with col3:
    st.metric("Equivalent Homes / Year", f"{equivalent_homes:,.1f}")

st.divider()

st.subheader("Current Model")

st.markdown(
    f"""
    **Scenario:** {scenario}  
    **Assumed energy per match:** {energy_per_match_mwh} MWh  
    **Formula:** Games Played × Energy per Match  
    """
)

st.info(
    "🚧 Model V0: This is a simplified stadium energy estimate. "
    "Future versions will include attendance, stadium type, weather, travel, broadcasting, and streaming."
)

st.subheader("Coming Next")

st.markdown(
    """
    - 🏟️ Stadium-level dataset  
    - 📊 Match-by-match energy estimate  
    - 🧾 World Cup Energy Receipt  
    - ✈️ Fan travel footprint  
    - 📺 Broadcasting and streaming energy  
    """
)