import sqlite3

class dataBase:
    def __init__(self):
        self.conn = sqlite3.connect("../db.sqlite3")
        self.cur = self.conn.cursor()