import psycopg2
import streamlit as st


class DB:

    def __init__(self):
        self.conn = None
        self.connect()

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=st.secrets["DB_HOST"],
                user=st.secrets["DB_USER"],
                password=st.secrets["DB_PASSWORD"],
                dbname=st.secrets["DB_NAME"],
                port=st.secrets["DB_PORT"],
                sslmode="require"
            )

            self.conn.autocommit = True

            st.success("Database Connected Successfully")

        except Exception as e:
            st.error(f"Database Connection Error: {e}")
            raise e

    def _ensure_connection(self):
        if self.conn is None or self.conn.closed:
            self.connect()

    def _fetchall(self, query, params=None):
        self._ensure_connection()

        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except psycopg2.Error:
            if self.conn and not self.conn.closed:
                self.conn.rollback()
            raise

    # ============================
    # FETCH CITY NAMES
    # ============================
    def fetch_city_names(self):

        query = """
        SELECT DISTINCT "Destination" FROM flights
        UNION
        SELECT DISTINCT "Source" FROM flights
        """

        data = self._fetchall(query)

        return [item[0] for item in data]

    # ============================
    # FETCH FLIGHTS
    # ============================
    def fetch_all_flights(self, source, destination):

        query = """
        SELECT "Airline", "Route", "Dep_Time", "Duration", "Price"
        FROM flights
        WHERE "Source" = %s AND "Destination" = %s
        """

        return self._fetchall(query, (source, destination))

    # ============================
    # AIRLINE FREQUENCY
    # ============================
    def fetch_airline_frequency(self):

        query = """
        SELECT "Airline", COUNT(*)
        FROM flights
        GROUP BY "Airline"
        """

        data = self._fetchall(query)

        airline = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return airline, frequency

    # ============================
    # BUSY AIRPORTS
    # ============================
    def busy_airport(self):

        query = """
        SELECT "Source", COUNT(*) FROM (
            SELECT "Source" FROM flights
            UNION ALL
            SELECT "Destination" FROM flights
        ) t
        GROUP BY t."Source"
        ORDER BY COUNT(*) DESC
        """

        data = self._fetchall(query)

        city = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return city, frequency

    # ============================
    # DAILY FLIGHT TREND
    # ============================
    def daily_frequency(self):

        query = """
        SELECT "Date_of_Journey", COUNT(*)
        FROM flights
        GROUP BY "Date_of_Journey"
        """

        data = self._fetchall(query)

        date = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return date, frequency

    def close(self):
        if self.conn and not self.conn.closed:
            self.conn.close()
