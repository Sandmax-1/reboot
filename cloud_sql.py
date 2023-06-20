from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql
import os
from generate_mentors import generate_mentors

# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "de-idiomisers:us-central1:mentor",
        "pymysql",
        user=os.environ.get("username"),
        password=os.environ.get("password"),
        db="mentors"
    )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)


# insert statement
mentors_table = sqlalchemy.text(
    """ 

Create table Mentors (
    id VARCHAR(255), 
    name VARCHAR(255), 
    gender VARCHAR(255),
    age INT,
    city VARCHAR(255),
    biography VARCHAR(255)
)
""",
)

# interact with Cloud SQL database using connection pool
with pool.connect() as db_conn:
    # insert into database
    # db_conn.execute(mentors_table, parameters={"id": "book1", "title": "Book One"})

    mentors = generate_mentors(1000)

    mentors.to_sql(name="Mentors", con=db_conn, if_exists="replace")

    db_conn.commit()

    result = db_conn.execute(sqlalchemy.text("SELECT * from Mentors")).fetchall()

    for row in result:
        print(row)