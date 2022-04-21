# from neo4j import GraphDatabase;
# import pandas as pd;
#
# from Neo4jConnection import Neo4jConnection
# url1 = 'https://raw.githubusercontent.com/ngshya/datasets/master/cora/cora_content.csv'
#
# url2 = 'https://raw.githubusercontent.com/ngshya/datasets/master/cora/cora_cites.csv'
# papers = pd.read_csv(url1, delimiter=",")
# cites = pd.read_csv(url2, delimiter=",")
#
# print(papers.head(20))
# print(papers.describe())
#
# query_string1 = '''
#      USING PERIODIC COMMIT 500
#      LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/ngshya/datasets/master/cora/cora_content.csv"
#      AS line FIELDTERMINATOR ','
#      CREATE (:Paper {id: line.paper_id, class: line.label})
#     '''
#
#
# conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", pwd="1234")
#
# query_string2 = '''
#     USING PERIODIC COMMIT 500
#     LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/ngshya/datasets/master/cora/cora_cites.csv'
#     AS line FIELDTERMINATOR ','
#     MATCH (citing_paper:Paper {id: line.citing_paper_id}),(cited_paper:Paper {id: line.cited_paper_id})
#     CREATE (citing_paper)-[:CITES]->(cited_paper)
#     '''
#
# conn.query(query_string1, db="neo4j")
# conn.query(query_string2, db="neo4j")

