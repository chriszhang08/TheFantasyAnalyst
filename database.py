import sqlite3
import pandas as pd

# scoreboard = pd.read_excel(r'/Users/chris/Documents/CS/league_data.xlsx')

# five data types
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# draft recap table called draft_recap (draft_recap.db)
# season scoreboard table called scoreboard (scoreboard.db)
# optimized season scoreboard table called opt_scoreboard (opt_scoreboard.db)

conn = sqlite3.connect('scoreboard.db')
c = conn.cursor()
# c.execute("""CREATE TABLE scoreboard (
#     Week integer,
#     TeamPackingSteel real,
#     TeamSeed6 real,
#     SUPRISEMOTHERBUTKER real,
#     TeamGotetibear real,
#     Team2Girls1Kupp real,
#     TeamSuckmydiggs real,
#     TeamCeedeezNUTS real,
#     TeamOgirala real,
#     MeandMahomies real,
#     ZhangsGang real,
#     KushRush real,
#     TeamThiccyMouse real
# )
# """)

# c.execute("DELETE from scoreboard WHERE rowid = 14 or rowid = 15 or rowid = 16 or rowid = 17")

# scoreboard.to_sql('scoreboard', conn, if_exists='append', index=False)

# c.execute("SELECT rowid, * FROM draft_recap")
#
# items = c.fetchall()
# for item in items:
#     print(item)

conn.commit()
conn.close()

# Query the DB and return all records
def show_all():
    conn = sqlite3.connect('draft_recap.db')
    c = conn.cursor()
    #query the database
    c.execute("SELECT rowid, * FROM draft_recap")
    items = c.fetchall()
    print("draft_recap.db:")
    for item in items:
        print(item)
    # commit our commmand
    conn.commit()
    # close our connection
    conn.close()

    # one connection for each database
    conn = sqlite3.connect('scoreboard.db')
    c = conn.cursor()
    #query the database
    c.execute("SELECT rowid, * FROM scoreboard")
    items = c.fetchall()
    print("scoreboard.db:")
    for item in items:
        print(item)
    conn.commit()
    conn.close()

    conn = sqlite3.connect('opt_scoreboard.db')
    c = conn.cursor()
    #query the database
    c.execute("SELECT rowid, * FROM opt_scoreboard")
    items = c.fetchall()
    print("opt_scoreboard.db:")
    for item in items:
        print(item)
    conn.commit()
    conn.close()


def add_opt(week, team):
    conn = sqlite3.connect('opt_scoreboard.db')
    c = conn.cursor()
    c.execute("INSERT INTO opt_scoreboard VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (week, team[0], team[1], team[2], team[3], team[4], team[5], team[6], team[7], team[8], team[9], team[10], team[11]))
    # commit our commmand
    conn.commit()
    # close our connection
    conn.close()

def add_many(list):
    conn = sqlite3.connect('box_score.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    # commit our commmand
    conn.commit()
    # close our connection
    conn.close()


def delete_one(id):
    conn = sqlite3.connect('box_score.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)

    # commit our commmand
    conn.commit()
    # close our connection
    conn.close()

# def create_connection(path):
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print("Connection to SQLite DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#     return connection
