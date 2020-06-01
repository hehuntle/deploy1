# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST'] # must 'localhost' when running this script outside of Docker

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# Create a TStudents table (wrapping it in a try-except is good practice)
try:
  cursor.execute("""
    CREATE TABLE Users (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30) NOT NULL,
      last_name   VARCHAR(30) NOT NULL,
      email       VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP
    );
  """)
except:
  print("Users table already exists. Not recreating it.")

# Create a Tnews table (wrapping it in a try-except is good practice)
try:
  cursor.execute("""
    CREATE TABLE News (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      title       VARCHAR(30) NOT NULL,
      date        VARCHAR(30) NOT NULL,
      content     VARCHAR(50) NOT NULL,
      created_at  TIMESTAMP
    );
  """)
except:
  print("News table already exists. Not recreating it.")

  # Insert Records
query = "insert into News (title, date, content) values (%s, %s, %s)"
values = [
  ('Here is the title','May 5, 2020','Here is the description for this cool news article and a brief bit of info for your users to read.'),
  ('Here is the title','May 5, 2020','Here is the description for this cool news article and a brief bit of info for your users to read.')
]
cursor.executemany(query, values)
db.commit()

cursor.execute("select * from Users;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]
db.close()

# Selecting Records
cursor.execute("select * from News;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]
db.close()
