# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

cypher_query = '''
MATCH (a:Officer {name: $name})-[r:OFFICER_OF|INTERMEDIARY_OF|REGISTERED_ADDRESS*..5]-(b)
RETURN distinct b.name as name LIMIT 20
'''

with GraphDatabase.driver(
    "neo4j://<HOST>:<BOLTPORT>",
    auth=("<USERNAME>", "<PASSWORD>")
) as driver:
    result = driver.execute_query(
        cypher_query,
        name="Stuart Onslow-Smith",
        database_="neo4j")
    for record in result.records:
        print(record['name'])
