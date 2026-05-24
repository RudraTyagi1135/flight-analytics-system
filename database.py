import psycopg2
import streamlit as st


class DB:

    def __init__(self):
        self.conn = None
        self.columns = None
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

    @staticmethod
    def _quote_identifier(identifier):
        return '"' + identifier.replace('"', '""') + '"'

    def _load_columns(self):
        query = """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = 'public' AND table_name = 'flights'
        """

        try:
            self.conn.rollback()
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                columns = [row[0] for row in cursor.fetchall()]
        except psycopg2.Error as e:
            if self.conn and not self.conn.closed:
                self.conn.rollback()
            detail = e.pgerror.strip() if e.pgerror else str(e)
            raise RuntimeError(f"Could not read database schema: {detail}") from e

        if not columns:
            raise RuntimeError('Table "public.flights" was not found in the connected database')

        self.columns = {column.lower(): column for column in columns}

    def _column(self, name):
        if self.columns is None:
            self._load_columns()

        column = self.columns.get(name.lower())
        if column is None:
            available = ", ".join(sorted(self.columns.values()))
            raise RuntimeError(f'Column "{name}" was not found in flights. Available columns: {available}')

        return self._quote_identifier(column)

    def _fetchall(self, query, params=None):
        self._ensure_connection()

        try:
            self.conn.rollback()
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except psycopg2.Error as e:
            if self.conn and not self.conn.closed:
                self.conn.rollback()
            detail = e.pgerror.strip() if e.pgerror else str(e)
            raise RuntimeError(f"Database query failed: {detail}") from e

    # ============================
    # FETCH CITY NAMES
    # ============================
    def fetch_city_names(self):

        destination_col = self._column("Destination")
        source_col = self._column("Source")

        query = f"""
        SELECT DISTINCT {destination_col} FROM flights
        UNION
        SELECT DISTINCT {source_col} FROM flights
        """

        data = self._fetchall(query)

        return [item[0] for item in data]

    # ============================
    # FETCH FLIGHTS
    # ============================
    def fetch_all_flights(self, source, destination):

        airline_col = self._column("Airline")
        route_col = self._column("Route")
        dep_time_col = self._column("Dep_Time")
        duration_col = self._column("Duration")
        price_col = self._column("Price")
        source_col = self._column("Source")
        destination_col = self._column("Destination")

        query = f"""
        SELECT {airline_col}, {route_col}, {dep_time_col}, {duration_col}, {price_col}
        FROM flights
        WHERE {source_col} = %s AND {destination_col} = %s
        """

        return self._fetchall(query, (source, destination))

    # ============================
    # AIRLINE FREQUENCY
    # ============================
    def fetch_airline_frequency(self):

        airline_col = self._column("Airline")

        query = f"""
        SELECT {airline_col}, COUNT(*)
        FROM flights
        GROUP BY {airline_col}
        """

        data = self._fetchall(query)

        airline = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return airline, frequency

    # ============================
    # BUSY AIRPORTS
    # ============================
    def busy_airport(self):

        source_col = self._column("Source")
        destination_col = self._column("Destination")

        query = f"""
        SELECT city, COUNT(*) FROM (
            SELECT {source_col} AS city FROM flights
            UNION ALL
            SELECT {destination_col} AS city FROM flights
        ) t
        GROUP BY city
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

        date_col = self._column("Date_of_Journey")

        query = f"""
        SELECT {date_col}, COUNT(*)
        FROM flights
        GROUP BY {date_col}
        """

        data = self._fetchall(query)

        date = [item[0] for item in data]
        frequency = [item[1] for item in data]

        return date, frequency

    def close(self):
        if self.conn and not self.conn.closed:
            self.conn.close()
