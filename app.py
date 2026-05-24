import streamlit as st
from database import DB
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Flights Analytics", layout="wide")

# ================================
# DB INIT (cached)
# ================================
@st.cache_resource
def get_db():
    return DB()

db = get_db()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox(
    'Menu',
    ['Select One', 'Check Flights', 'Analytics']
)

# ================================
# CHECK FLIGHTS
# ================================
if user_option == 'Check Flights':

    st.title('✈️ Check Flights')

    try:
        source_cities = db.fetch_source_names()


        if not source_cities:
            st.warning("No city data available")
            st.stop()

        col1, col2 = st.columns(2)

        with col1:
            source = st.selectbox('Source', source_cities)

        destination_cities = db.fetch_destinations_for_source(source)

        if not destination_cities:
            st.warning(f"No destinations found for {source}")
            st.stop()

        with col2:
            destination = st.selectbox('Destination', destination_cities)

        if st.button('Search'):

            results = db.fetch_all_flights(source, destination)

            if not results:
                st.warning(f"No flights found from {source} to {destination}")
            else:
                df = pd.DataFrame(
                    results,
                    columns=["Airline", "Route", "Departure", "Duration", "Price"]
                )
                st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")

# ================================
# ANALYTICS
# ================================
elif user_option == 'Analytics':

    st.title("📊 Analytics Dashboard")

    try:
        # ---------------------------
        # Airline Pie Chart
        # ---------------------------
        airline, frequency = db.fetch_airline_frequency()

        if airline:
            fig = go.Figure(
                go.Pie(
                    labels=airline,
                    values=frequency,
                    hoverinfo="label+percent",
                    textinfo="value"
                )
            )

            st.subheader("Airline Distribution")
            st.plotly_chart(fig, use_container_width=True)

        # ---------------------------
        # Busy Airports
        # ---------------------------
        city, frequency1 = db.busy_airport()

        if city:
            fig = px.bar(
                x=city,
                y=frequency1,
                labels={"x": "City", "y": "Traffic"}
            )

            st.subheader("Busy Airports")
            st.plotly_chart(fig, use_container_width=True)

        # ---------------------------
        # Daily Frequency
        # ---------------------------
        date, frequency2 = db.daily_frequency()

        if date:
            df = pd.DataFrame({
                "Date": date,
                "Flights": frequency2
            })

            fig = px.line(df, x="Date", y="Flights")

            st.subheader("Daily Flight Trend")
            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Error: {e}")

# ================================
# DEFAULT
# ================================
else:
    st.title('📌 Flights Analytics Project')

    st.markdown("""
    This project provides:

    - ✈️ Flight search between cities  
    - 📊 Airline distribution analysis  
    - 🏙️ Airport traffic insights  
    - 📅 Daily flight trends  

    Built using:
    - Streamlit  
    - Supabase PostgreSQL  
    - psycopg2  
    - Plotly  
    """)

# ================================
# CLEANUP (optional)
# ================================
# db.close()  # avoid closing cached connection
