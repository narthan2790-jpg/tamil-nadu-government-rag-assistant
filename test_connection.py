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

print("Starting Neo4j connection test...")

try:
    driver = GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD),
        connection_timeout=30
    )

    driver.verify_connectivity()

    print("SUCCESS: Connected to Neo4j Aura!")

    with driver.session(database=DATABASE) as session:
        result = session.run("RETURN 1 AS test")
        print("Database test:", result.single()["test"])

    driver.close()

except Exception as error:
    print("CONNECTION FAILED")
    print(type(error).__name__, error)