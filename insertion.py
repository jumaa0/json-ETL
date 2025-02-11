import mysql.connector
import csv
import os

DB_CONFIG = {
    "host": "localhost",
    "user": "gomaa",
    "password": "****",
    "database": "ny_philharmonic",
}

TABLES = {
    "./trg/orchestra.txt": ("orchestra", ["orchestraID", "orchestraName"]),
    "./trg/program.txt": ("program", ["programID", "season", "orchestraID"]),
    "./trg/concert.txt": ("concert", ["concertID", "eventType", "date", "venue", "location", "time", "programID"]),
    "./trg/works.txt": ("works", ["workID", "workTitle", "composerName", "conductorID", "concertID"]),
    "./trg/person.txt": ("person", ["personID", "name"]),
    "./trg/soloist_work_person.txt": ("soloist_work_person", ["soloistID", "workID"]),
}

def connect_db():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except:
        return None

def insert_data_from_file(cursor, table_name, columns, file_path):
    if not os.path.exists(file_path):
        return
    
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
        data = [tuple(row) for row in reader]
        if data:
            cursor.executemany(query, data)

conn = connect_db()
if not conn:
    return

cursor = conn.cursor()
for file_name, (table_name, columns) in TABLES.items():
    insert_data_from_file(cursor, table_name, columns, file_name)

conn.commit()
cursor.close()
conn.close()
