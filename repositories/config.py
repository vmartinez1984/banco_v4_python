from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("uri")
db_name = os.getenv("db_name")