import sqlite3

conn = sqlite3.connect('openingdb.sqlite')
cur = conn.cursor()

# Fill database
cur.executescript('''
DROP TABLE IF EXISTS Position;
DROP TABLE IF EXISTS RightToMove;
DROP TABLE IF EXISTS CastlingAbility;
DROP TABLE IF EXISTS EnPassantAbility;

CREATE TABLE RightToMove (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    color  CHAR UNIQUE
);

CREATE TABLE CastlingAbility (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE EnPassantAbility (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Position (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    fen   TEXT UNIQUE,
    rightToMove_id INTEGER,
    castlingAbility_id INTEGER,
    enPassantAbility_id INTEGER,
    bestOrigin TEXT,
    bestDestination TEXT,
    promotion CHAR
)
''')

cur.execute('''INSERT OR IGNORE INTO CastlingAbility (name)
    VALUES ( '-' )''' )
cur.execute('''INSERT OR IGNORE INTO CastlingAbility (name)
    VALUES ( 'KQkq' )''' )
cur.execute('''INSERT OR IGNORE INTO CastlingAbility (name)
    VALUES ( 'Kkq' )''' )
cur.execute('''INSERT OR IGNORE INTO CastlingAbility (name)
    VALUES ( 'Qkq' )''' )
cur.execute('''INSERT OR IGNORE INTO CastlingAbility (name)
    VALUES ( 'Kk' )''' )
cur.execute('''INSERT OR IGNORE INTO CastlingAbility (name)
    VALUES ( 'Kq' )''' )
cur.execute('''INSERT OR IGNORE INTO CastlingAbility (name)
    VALUES ( 'K' )''' )
cur.execute('''INSERT OR IGNORE INTO CastlingAbility (name)
    VALUES ( 'KQ' )''' )

cur.execute('''INSERT OR IGNORE INTO EnPassantAbility (name)
    VALUES ( '-' )''' )
cur.execute('''INSERT OR IGNORE INTO EnPassantAbility (name)
    VALUES ( 'h5' )''' )
cur.execute('''INSERT OR IGNORE INTO RightToMove (color)
    VALUES ( 'w' )''' )
cur.execute('''INSERT OR IGNORE INTO RightToMove (color)
    VALUES ( 'b' )''' )

cur.execute('''INSERT OR IGNORE INTO 
    Position (fen, RightToMove_id, CastlingAbility_id,EnPassantAbility_id, bestOrigin, bestDestination, promotion  )
    VALUES ( 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', 1, 2, 1, 'e2', 'e4', '-' )''')

# Read values from database

cur.execute('''SELECT bestOrigin, bestDestination 
    FROM Position WHERE fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR' 
    ''')

conn.commit()
row = cur.fetchone()
print(row[0], row[1])
