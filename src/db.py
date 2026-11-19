import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('jobs.db')
        self.conn.executescript(open('src/schema.sql').read())


    def insert_job(self, job: dict):
        with self.conn:
            self.conn.execute('''
                INSERT OR IGNORE INTO jobs (referenznummer, type, title, company, location, date_posted, url)
                VALUES (:referenznummer, :type, :title, :company, :location, :date_posted, :url)
            ''', job)