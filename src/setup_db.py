import sqlite3

con = sqlite3.connect("./wingscore.db")
cur = con.cursor()

tables = [
    ("player", 
     "id VARCHAR(255) PRIMARY KEY, name VARCHAR(25), favorite_bird VARCHAR(25)"),
    ("game", 
     "id VARCHAR(255) PRIMARY KEY, date_played DATETIME, expansions_used BLOB, play_mode VARCHAR(25), automa BOOLEAN"),
    ("scoresheet", 
     "id VARCHAR(255) PRIMARY KEY, game_id VARCHAR(255), player_id VARCHAR(255), bird_points INTEGER, bonus_card_points INTEGER, round_goals_points INTEGER, eggs INTEGER, food_on_cards INTEGER, tucked_cards INTEGER, nector_points INTEGER, FOREIGN KEY(game_id) REFERENCES game(id), FOREIGN KEY(player_id) REFERENCES player(id)"),
]

for table_name, cols in tables:
    sql = f"CREATE TABLE IF NOT EXISTS {table_name}({cols})"
    cur.execute(sql)

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())