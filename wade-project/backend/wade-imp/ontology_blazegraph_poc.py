import json
from rdflib import Graph, Namespace, Literal, RDF, OWL
from SPARQLWrapper import POSTDIRECTLY, SPARQLWrapper, POST, JSON
from rdflib.plugins.sparql import prepareQuery

onto = Namespace("http://example.org/ontology/") #-> schema.org?

schema = Namespace("http://www.w3.org/2001/XMLSchema#") #->asta nu cred ca trebuie

g = Graph()

# Classes
g.add((onto.Portrait, RDF.type, OWL.Class))
g.add((onto.Emotion, RDF.type, OWL.Class))
g.add((onto.Age, RDF.type, OWL.Class))
g.add((onto.Race, RDF.type, OWL.Class))
g.add((onto.Painter, RDF.type, OWL.Class))

g.add((onto.hasEmotion, RDF.type, OWL.DatatypeProperty))
g.add((onto.hasAge, RDF.type, OWL.DatatypeProperty))
g.add((onto.hasRace, RDF.type, OWL.DatatypeProperty))
g.add((onto.paintedBy, RDF.type, OWL.DatatypeProperty))
g.add((onto.hasDescription, RDF.type, OWL.DatatypeProperty))
g.add((onto.hasBirthDate, RDF.type, OWL.DatatypeProperty))
g.add((onto.hasDeathDate, RDF.type, OWL.DatatypeProperty))
#
# # portrait1 = onto.Portrait1
# # emotion1 = onto.Happy
# # age1 = onto.Young
# # race1 = onto.White
# # painter1 = onto.VanGogh
# #
# # description1 = Literal("Vincent van Gogh was a Dutch Post-Impressionist painter.")
# # birth_date1 = Literal("1853-03-30", datatype=schema.date)
# # death_date1 = Literal("1890-07-29", datatype=schema.date)
# #
# # g.add((portrait1, RDF.type, onto.Portrait))
# # g.add((portrait1, onto.hasEmotion, emotion1))
# # g.add((portrait1, onto.hasAge, age1))
# # g.add((portrait1, onto.hasRace, race1))
# # g.add((portrait1, onto.paintedBy, painter1))
# # g.add((painter1, onto.hasDescription, description1))
# # g.add((painter1, onto.hasBirthDate, birth_date1))
# # g.add((painter1, onto.hasDeathDate, death_date1))
#
# # Load data from JSON file
# with open('portraits.json', 'r') as f:
#     portraits = json.load(f)
#
# print(portraits['0'])
# # Add data to the ontology
# for portrait_data in portraits:
#     portrait_data = portraits[portrait_data]
#     # Create unique identifiers for each instance
#     portrait = onto[portrait_data["filename"].replace(".jpg", "")]
#     emotion = Literal(portrait_data["emotion"].capitalize())
#     age = Literal(str(portrait_data["age"]))
#     race = Literal(portrait_data["race"].replace(" ", "_").capitalize())
#     painter = Literal(portrait_data["painter"])
#
#     g.add((portrait, RDF.type, onto.Portrait))
#     g.add((portrait, onto.hasEmotion, emotion))
#     g.add((portrait, onto.hasAge, age))
#     g.add((portrait, onto.hasRace, race))
#     g.add((portrait, onto.paintedBy, painter))
#
# # Serialize the ontology
# serialized_ontology = g.serialize()
# #print(serialized_ontology)
#
# sparql = SPARQLWrapper("http://localhost:9999/blazegraph/sparql")
# sparql.method = POST
#
# sparql.setQuery("""
#     INSERT DATA {
#         %s
#     }
# """ % serialized_ontology)
#
# sparql.query()
#
#
#
# '''
# Am facut in blazegraph (http://localhost:9999/blazegraph/#query) query-ul asta si datele de mai sus erau inserate
#     SELECT ?s ?p ?o
#     WHERE {
#         ?s ?p ?o .
#     }
#
# '''

def add_portrait_entity_to_graph(new_entity):
    # Create unique identifiers for each instance
    print(new_entity)
    filename = new_entity["filename"].replace(".jpg", "")
    emotion = new_entity["emotion"].capitalize()
    age = int(new_entity["age"])
    gender = new_entity["gender"]
    race = new_entity["race"].replace(" ", "_").capitalize()
    painter = new_entity["painter"].replace("-", "_")

    sparql = SPARQLWrapper("http://localhost:9999/blazegraph/sparql")
    sparql.method = "POST"

    sparql_query = f"""
        PREFIX : <http://imp-wade.com/ontology/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        INSERT DATA {{
          :{filename} a :Painting ;
              :hasEmotion "{emotion}" ;
              :hasAge {age} ;
              :hasRace "{race}" ;
              :hasGender "{gender}" ;
              :createdBy :{painter} .
              }}
              """

    print(sparql_query)
    sparql.setQuery(sparql_query)
    sparql.query()
    print("updated the Blazegraph database")


def add_painter_entity_to_graph(new_entity):
    # Create unique identifiers for each instance
    painter = new_entity["painter"]
    summary = new_entity["summary"]
    lifespan = new_entity["lifespan"]

    sparql = SPARQLWrapper("http://localhost:9999/blazegraph/sparql")
    sparql.method = "POST"

    sparql_query = f"""
        PREFIX : <http://imp-wade.com/ontology/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        INSERT DATA {{
          :{painter} a :Painter ;
              :hasName "{painter}" ;
              :hasDescription "{summary}" ;
              :hasLifespan "{lifespan}" .
              }}
              """

    print(sparql_query)
    sparql.setQuery(sparql_query)
    sparql.query()
    print("updated the Blazegraph database")
