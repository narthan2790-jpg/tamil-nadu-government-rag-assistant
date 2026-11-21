
from pathlib import Path
from dotenv import load_dotenv
from neo4j import GraphDatabase
import os

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", override=True)

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")

DIRECT_URI = URI.replace("neo4j+s://", "bolt+s://")

print("DIRECT BOLT CONNECTION TEST")
print("URI:", DIRECT_URI)
print("Username:", USERNAME)

driver = None

try:
    driver = GraphDatabase.driver(
        DIRECT_URI,
        auth=(USERNAME, PASSWORD),
        connection_timeout=30
    )

    driver.verify_connectivity()

    print("SUCCESS: Direct connection established!")

    with driver.session(database=DATABASE) as session:
        result = session.run("RETURN 1 AS test")
        print("Database test:", result.single()["test"])

except Exception as error:
    print("CONNECTION FAILED")
    print(type(error).__name__, error)

finally:
    if driver:
        driver.close()
