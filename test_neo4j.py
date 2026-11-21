
import os
import certifi
import traceback

from dotenv import load_dotenv
from neo4j import GraphDatabase

# Load environment variables
load_dotenv()

# Tell Python to use certifi's trusted certificates
os.environ["SSL_CERT_FILE"] = certifi.where()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")

if not all([URI, USERNAME, PASSWORD]):
    raise ValueError("Missing Neo4j credentials in .env")

# Create secure Aura connection
driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

try:
    driver.verify_connectivity()
    print("SUCCESS! Connected to Neo4j Aura.")

    with driver.session(database=DATABASE) as session:
        result = session.run(
            "RETURN 'Tamil Nadu Government RAG' AS project"
        )

        print("Project:", result.single()["project"])

except Exception:
    print("Connection or query failed:")
    traceback.print_exc()

finally:
    driver.close()
    print("Driver closed.")
