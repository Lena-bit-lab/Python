from sqlalchemy import create_engine, text
from config import DB_CONNECTION_STRING

def test_insert():
    engine = create_engine(DB_CONNECTION_STRING)
    with engine.connect() as conn:
        # Insert
        query = "INSERT INTO student(\"user_id\") VALUES (74532542)"
        conn.execute(text(query))

        # Assert
        select_query = "SELECT * FROM student WHERE user_id=74532542"
        result = conn.execute(text(select_query))
        rows = result.mappings().all()

        assert len(rows) == 2
        assert rows[0]['user_id'] == 74532542
