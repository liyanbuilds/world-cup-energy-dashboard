from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hidden Energy Behind World Cup 2026",
    page_icon="⚽",
    layout="wide",
)

# -----------------------------
# Load match dataset
# -----------------------------

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "matches.csv"
matches = pd.read_csv(DATA_PATH)

# -----------------------------
# Model calculations
# -----------------------------

total_world_cup_matches = 104
games_in_dataset = len(matches)
total_energy_mwh = matches["estimated_energy_mwh"].sum()

# Placeholder assumptions
annual_home_energy_mwh = 10
ev_battery_kwh = 75

equivalent_homes = total_energy_mwh / annual_home_energy_mwh
equivalent_ev_charges = (total_energy_mwh * 1000) / ev_battery_kwh

top_match = matches.sort_values(
    by="estimated_energy_mwh",
    ascending=False
).iloc[0]

# -----------------------------
# Page header
# -----------------------------

st.title("⚽ Hidden Energy Behind World Cup 2026")

st.markdown(
    """
    How much energy does the world's biggest sporting event actually consume?

    This project estimates the hidden energy footprint of FIFA World Cup 2026
    using public data, simple models, and transparent assumptions.
    """
)

st.divider()

# -----------------------------
# KPI cards
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Games in Dataset", f"{games_in_dataset} / {total_world_cup_matches}")

with col2:
    st.metric("Estimated Stadium Energy", f"{total_energy_mwh:,.0f} MWh")

with col3:
    st.metric("Equivalent Homes / Year", f"{equivalent_homes:,.1f}")

st.divider()

# -----------------------------
# Energy receipt
# -----------------------------

st.subheader("🧾 World Cup Energy Receipt")

receipt_css = """
<style>
.energy-receipt {
    background-color: #fffaf0;
    color: #1f1f1f;
    padding: 28px;
    border-radius: 16px;
    border: 2px dashed #333333;
    max-width: 520px;
    font-family: "Courier New", monospace;
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
}
.receipt-title {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 4px;
}
.receipt-subtitle {
    text-align: center;
    font-size: 14px;
    margin-bottom: 20px;
}
.receipt-row {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px dotted #999999;
    padding: 8px 0;
    font-size: 16px;
}
.receipt-total {
    display: flex;
    justify-content: space-between;
    padding-top: 14px;
    margin-top: 12px;
    border-top: 2px solid #333333;
    font-size: 20px;
    font-weight: bold;
}
.receipt-footer {
    text-align: center;
    margin-top: 22px;
    font-size: 13px;
}
</style>
"""

receipt_html = f"""
<div class="energy-receipt">
    <div class="receipt-title">FIFA WORLD CUP 2026</div>
    <div class="receipt-subtitle">Hidden Energy Receipt</div>

    <div class="receipt-row">
        <span>Matches counted</span>
        <span>{games_in_dataset}</span>
    </div>

    <div class="receipt-row">
        <span>Stadium energy</span>
        <span>{total_energy_mwh:,.0f} MWh</span>
    </div>

    <div class="receipt-row">
        <span>Equivalent homes</span>
        <span>{equivalent_homes:,.1f} / year</span>
    </div>

    <div class="receipt-row">
        <span>Equivalent EV charges</span>
        <span>{equivalent_ev_charges:,.0f}</span>
    </div>

    <div class="receipt-total">
        <span>Total</span>
        <span>{total_energy_mwh:,.0f} MWh</span>
    </div>

    <div class="receipt-footer">
        Model V0 · Stadium energy only · More hidden energy coming soon
    </div>
</div>
"""

components.html(receipt_css + receipt_html, height=520)

st.caption(
    "This receipt is designed as a social-friendly snapshot. "
    "Current scope: estimated stadium energy only."
)

st.divider()

# -----------------------------
# Highest energy match
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
# Match dataset
# -----------------------------

st.subheader("Match Energy Dataset")

st.dataframe(matches, use_container_width=True)

st.info(
    "🚧 Model V0: This dataset uses simplified match-level energy assumptions. "
    "Future versions will estimate energy based on stadium type, attendance, weather, "
    "travel, broadcasting, and streaming."
)