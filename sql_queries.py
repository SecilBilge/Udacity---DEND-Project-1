# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL, start_time timestamp not null, user_id int not null, level varchar not null, song_id varchar , artist_id varchar , session_id int not null, location varchar not null, user_agent varchar not null, primary key (songplay_id));")

user_table_create = ("CREATE TABLE IF NOT EXISTS users(user_id int, first_name varchar not null, last_name varchar not null, gender char(1) not null, level varchar not null ,primary key(user_id) );")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs(song_id varchar, title varchar not null, artist_id varchar not null, year int not null, duration float not null, primary key (song_id));")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists(artist_id  varchar, name varchar not null, location varchar not null, latitude float, logtitude float, primary key (artist_id ));")

time_table_create = ("CREATE TABLE IF NOT EXISTS time(start_time timestamp, hour int, day int , week int, month int, year int, weekday int, primary key (start_time));")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES ( %s, %s,%s, %s, %s,%s, %s, %s)")

# Fixed user need to update the level field during insert conflict - Rv.2 Date:20201206
user_table_insert = ("INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) on conflict(user_id) do update set level=excluded.level")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES  (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING")

artist_table_insert = ("INSERT INTO artists (artist_id, name, location, latitude, logtitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING")

time_table_insert = ("INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s,%s, %s, %s,%s)  ON CONFLICT (start_time) DO NOTHING")

# FIND SONGS

song_select = ("Select songs.song_id, songs.artist_id from songs JOIN artists a ON songs.artist_id = a.artist_id WHERE songs.title = %s AND a.name = %s AND songs.duration = %s")

# FOR ANALYTICS

analytics_select = ("Select * from songplays sp join users u on (sp.user_id = u.user_id) join songs s on (sp.song_id= s.song_id) join artists a on (sp.artist_id=a.artist_id) join time t on (sp.start_time = t.start_time)")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

