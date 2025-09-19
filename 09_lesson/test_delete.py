from sqlalchemy import create_engine, text
from config import DB_CONNECTION_STRING

def test_delete():
    engine = create_engine(DB_CONNECTION_STRING)
    with engine.connect() as conn:

        # Assert
        select_query = "SELECT * FROM student WHERE user_id=5"
        result = conn.execute(text(select_query))
        rows = result.mappings().all()

        assert len(rows) == 1
