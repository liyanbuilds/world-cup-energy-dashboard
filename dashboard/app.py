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

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Games Played", "0 / 104")

with col2:
    st.metric("Estimated Energy", "0 MWh")

with col3:
    st.metric("Equivalent Homes", "0")

st.divider()

st.subheader("What this dashboard will track")

st.markdown(
    """
    - 🏟️ Stadium operations  
    - ✈️ Fan travel footprint  
    - 📺 Broadcasting and streaming  
    - ⚡ Electricity use  
    - 🌎 Carbon impact  
    """
)

st.info("🚧 Day 3: First dashboard prototype")