import json
from SPARQLWrapper import SPARQLWrapper

with open('portraits.json', 'r') as f:
    portraits = json.load(f)

with open('painters.json', 'r') as f:
    painters = json.load(f)

# Add data to the ontology
for portrait_data in portraits:
    filename = portrait_data["filename"].replace(".jpg", "")
    emotion = portrait_data["emotion"].capitalize()
    age = int(portrait_data["age"])
    gender = portrait_data["gender"]
    race = portrait_data["race"].replace(" ", "_").capitalize()
    painter = portrait_data["painter"].replace("-", "_")

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

for painters_data in painters:
    # Create unique identifiers for each instance
    painter = painters_data["painter"]
    summary = painters_data["summary"]
    lifespan = painters_data["lifespan"]

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