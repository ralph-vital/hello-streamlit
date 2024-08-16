from dotenv import load_dotenv
import os
import snowflake.connector

USER = os.getenv('user'),
PASSWORD = os.getenv('password'),
ACCOUNT = os.getenv('account'),
WAREHOUSE = os.getenv('warehouse'),
DATABASE = os.getenv('database'),
SCHEMA = os.getenv('schema'),

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA,
)
