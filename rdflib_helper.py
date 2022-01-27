
import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON


class RDFHelper:

    def __init__(self):
        self.g = rdflib.Graph()
        self.federated = rdflib.Graph()
        self.g.parse("ont2.owl")
        self.federated.parse("m-ontology-2.owl")
        self.sparql = SPARQLWrapper("http://dbpedia.org/sparql")

    def process_query(self,query):
        # 1.
        qres = self.g.query(query)
        output = " ".join([str(q) for q in qres])
        return output

    def process_dbpedia_query(self,query):
        # 2.
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results =self.sparql.query().convert()
        output = ""
        for result in results["results"]["bindings"]:
            output += result["comment"]["value"] + " \n "
        return output
    

    def process_federated(self,query):
        qres = self.federated.query(query)
        output = " ".join([str(q) for q in qres])
        return output