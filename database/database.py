import sqlite3

class Database:
    def init(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    CREATE TABLE IF NOT EXISTS homeworks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        group_name TEXT,
                        number_hw INTEGER,
                        link TEXT
                    )
                """
            )
            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)
            conn.commit()