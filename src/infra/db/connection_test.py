from connect_settings import ConnectionHandler


def test_created_database_engine():
    db_connection_handle = ConnectionHandler()
    engine = db_connection_handle.get_engine()

    assert engine is not None
