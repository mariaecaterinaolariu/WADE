# import csv
# from rdflib import RDF, Graph, URIRef, Literal, Namespace

# # Define RDF namespaces
# SCHEMA = Namespace("http://schema.org/")

# # Create an RDF graph
# g = Graph()


# with open('D:/Facultate/Sem2.1/WADe/off-biscuits.csv', newline='', encoding='utf-8') as csvfile:
#     csvreader = csv.DictReader(csvfile, delimiter='\t') 
 
#     for row in csvreader:

#         product_uri = URIRef(f"http://example.org/product/{row['code']}")
#         g.add((product_uri, RDF.type, SCHEMA.Product))
#         g.add((product_uri, SCHEMA.code, Literal(row['code'])))
#         g.add((product_uri, SCHEMA.product_name, Literal(row['product_name'])))



# g.serialize(destination='D:/Facultate/Sem2.1/WADe/output.rdf', format='xml')


from rdflib import ConjunctiveGraph

graph = ConjunctiveGraph()

jsonld_file_path = 'D:\Facultate\Sem2.1\WADe\output.jsonld'
graph.parse(jsonld_file_path, format='json-ld')

query = """
    PREFIX ns1: <http://schema.org/>
    SELECT ?product ?product_name
    WHERE {
        ?product a ns1:Product ;
                 ns1:product_name ?product_name .
    }
"""
results = graph.query(query)

# Print query results
for row in results:
    print(f"Product: {row['product']} - Product Name: {row['product_name']}")