import psycopg2
import streamlit as st


class DB:

    def __init__(self):

        try:

            self.conn = psycopg2.connect(
                host=st.secrets["DB_HOST"],
                user=st.secrets["DB_USER"],
                password=st.secrets["DB_PASSWORD"],
                dbname=st.secrets["DB_NAME"],
                port=st.secrets["DB_PORT"],
                sslmode="require"
            )

            self.cursor = self.conn.cursor()

            st.success("Database Connected Successfully")

        except Exception as e:

            st.error(f"Database Connection Error: {e}")

            raise e

    # ============================
    # FETCH CITY NAMES
    # ============================
    def fetch_city_names(self):

        query = """
        SELECT DISTINCT Destination FROM flights
        UNION
        SELECT DISTINCT Source FROM flights
        """

        self.cursor.execute(query)

        data = self.cursor.fetchall()

        return [item[0] for item in data]

    # ============================
    # FETCH FLIGHTS
    # ============================
    def fetch_all_flights(self, source, destination):

        query = """
        SELECT Airline, Route, Dep_Time, Duration, Price
        FROM flights
        WHERE Source = %s AND Destination = %s
        """

        self.cursor.execute(query, (source, destination))

        return self.cursor.fetchall()

    # ============================
    # AIRLINE FREQUENCY
    # ============================
    def fetch_airline_frequency(self):

        query = """
        SELECT Airline, COUNT(*)
        FROM flights
        GROUP BY Airline
        """

        self.cursor.execute(query)

        data = self.cursor.fetchall()

        airline = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return airline, frequency

    # ============================
    # BUSY AIRPORTS
    # ============================
    def busy_airport(self):

        query = """
        SELECT Source, COUNT(*) FROM (
            SELECT Source FROM flights
            UNION ALL
            SELECT Destination FROM flights
        ) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """

        self.cursor.execute(query)

        data = self.cursor.fetchall()

        city = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return city, frequency

    # ============================
    # DAILY FLIGHT TREND
    # ============================
    def daily_frequency(self):

        query = """
        SELECT Date_of_Journey, COUNT(*)
        FROM flights
        GROUP BY Date_of_Journey
        """

        self.cursor.execute(query)

        data = self.cursor.fetchall()

        date = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return date, frequency
