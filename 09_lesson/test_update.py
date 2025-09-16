from sqlalchemy import create_engine, inspect, text

def test_update():
    db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
    engine = create_engine(db_connection_string)
    # inspector = inspect(engine)
    # names = inspector.get_columns(table_name = 'student')
    # print(names)
    with engine.connect() as conn:
        # Insert
        query = "INSERT INTO student(\"user_id\") VALUES (5)"
        conn.execute(text(query))

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
