from sqlalchemy import create_engine, text
from config import DB_CONNECTION_STRING

def test_update():
    engine = create_engine(DB_CONNECTION_STRING)
    with engine.connect() as conn:

        # Assert
        select_query = "SELECT * FROM student WHERE user_id=5"
        result = conn.execute(text(select_query))
        rows = result.mappings().all()
        assert len(rows) == 1

        # Update
        query = "UPDATE student SET subject_id=787878 WHERE user_id=5"
        conn.execute(text(query))

        # Assert
        select_query = "SELECT * FROM student where user_id=5"
        result = conn.execute(text(select_query))
        rows = result.mappings().all()

        assert len(rows) == 1
        assert rows[0]['subject_id'] == 787878
