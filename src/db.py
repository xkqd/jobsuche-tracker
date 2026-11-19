import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('jobs.db')
        self.conn.executescript(open('src/schema.sql').read())


    def insert_job(self, joblist: list):
        with self.conn:
            for job in joblist:
                self.conn.execute('''
                    INSERT OR IGNORE INTO jobs (referenznummer, type, title, company, location, date_posted, url, date_begins)
                    VALUES (:referenznummer, :type, :title, :company, :location, :date_posted, :url, :date_begins)
                ''', job)
            self.conn.commit()