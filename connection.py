from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql
import os

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

create_table_mentors = """ 

Create table Mentors (
    id VARCHAR(255), 
    name VARCHAR(255), 
    gender VARCHAR(255),
    age INT,
    city VARCHAR(255),
    biography VARCHAR(255)
)


"""

# insert statement
insert_stmt = sqlalchemy.text(
    "",
)

# interact with Cloud SQL database using connection pool
with pool.connect() as db_conn:
    # insert into database
    db_conn.execute(insert_stmt, parameters={"id": "book1", "title": "Book One"})

    # commit transaction (SQLAlchemy v2.X.X is commit as you go)
    db_conn.commit()

    # query database
    result = db_conn.execute(sqlalchemy.text("SELECT * from my_table")).fetchall()

    # Do something with the results
    for row in result:
        print(row)