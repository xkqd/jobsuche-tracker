CREATE TABLE IF NOT EXISTS jobs (
    referenznummer TEXT PRIMARY KEY ,
    type TEXT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT,
    date_posted DATE,
    url TEXT UNIQUE,
    date_begins DATE
);