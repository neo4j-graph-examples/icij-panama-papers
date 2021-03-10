# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://<HOST>:<BOLTPORT>",
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

cypher_query = '''
MATCH (a:Officer {name: $name})-[r:OFFICER_OF|INTERMEDIARY_OF|REGISTERED_ADDRESS*..5]-(b)
RETURN distinct b.name as name LIMIT 20
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      name="Stuart Onslow-Smith").data())
  for record in results:
    print(record['name'])

driver.close()
