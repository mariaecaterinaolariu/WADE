from rdflib import Graph, Namespace, Literal, RDF, OWL
from SPARQLWrapper import SPARQLWrapper, POST, JSON
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
g.add((onto.ArtMovement, RDF.type, OWL.Class))

# Object Properties
g.add((onto.hasEmotion, RDF.type, OWL.ObjectProperty))
g.add((onto.hasAge, RDF.type, OWL.ObjectProperty))
g.add((onto.hasRace, RDF.type, OWL.ObjectProperty))
g.add((onto.paintedBy, RDF.type, OWL.ObjectProperty))
g.add((onto.belongsToArtMovement, RDF.type, OWL.ObjectProperty))
g.add((onto.hasDescription, RDF.type, OWL.DatatypeProperty))
g.add((onto.hasBirthDate, RDF.type, OWL.DatatypeProperty))
g.add((onto.hasDeathDate, RDF.type, OWL.DatatypeProperty))

portrait1 = onto.Portrait1
emotion1 = onto.Happy
age1 = onto.Young
race1 = onto.Caucasian
painter1 = onto.VanGogh
art_movement1 = onto.Impressionism

description1 = Literal("Vincent van Gogh was a Dutch Post-Impressionist painter.")
birth_date1 = Literal("1853-03-30", datatype=schema.date)
death_date1 = Literal("1890-07-29", datatype=schema.date)

g.add((portrait1, RDF.type, onto.Portrait))
g.add((portrait1, onto.hasEmotion, emotion1))
g.add((portrait1, onto.hasAge, age1))
g.add((portrait1, onto.hasRace, race1))
g.add((portrait1, onto.paintedBy, painter1))
g.add((painter1, onto.belongsToArtMovement, art_movement1))
g.add((painter1, onto.hasDescription, description1))
g.add((painter1, onto.hasBirthDate, birth_date1))
g.add((painter1, onto.hasDeathDate, death_date1))

serialized_ontology = g.serialize()
# print(serialized_ontology)

sparql = SPARQLWrapper("http://localhost:9999/blazegraph/sparql")
sparql.method = POST

sparql.setQuery("""
    INSERT DATA {
        %s
    }
""" % serialized_ontology)

sparql.query()



'''
Am facut in blazegraph (http://localhost:9999/blazegraph/#query) query-ul asta si datele de mai sus erau inserate
    SELECT ?s ?p ?o 
    WHERE {
        ?s ?p ?o .
    }

'''
