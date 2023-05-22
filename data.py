import sqlite3

conn = sqlite3.connect('database.db') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS voter
          (voter_id INTEGER PRIMARY KEY, voter_nim INTEGER, voter_name TEXT, voter_pass TEXT, status BOOLEAN);
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS vote
          (vote_id INTEGER PRIMARY KEY, vote INTEGER);
        ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS candidate
          (candidate_id INTEGER PRIMARY KEY, candidate_name TEXT);
        ''')

c.execute('''
        INSERT INTO voter(voter_id, voter_nim, voter_name, voter_pass, status) VALUES
        (1, 18220500, "nama1", "pass1", FALSE),
        (2, 18220501, "nama2", "pass2", FALSE),
        (3, 18220503, "nama3", "pass3", FALSE),
        (4, 18220504, "nama4", "pass4", FALSE),
        (5, 18220505, "nama5", "pass5", FALSE),
        (6, 18220506, "nama6", "pass6", FALSE)
        ''')

c.execute('''
          INSERT INTO candidate(candidate_id, candidate_name) VALUES
          (1, "kandidat1"),
          (2, "kandidat2");
          ''')
                     
conn.commit()