from rdflib import Graph, RDF, Namespace, Literal, URIRef
from flask import Flask, Response, request
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# opening the graph without parsing it (otherwise function runs too long)
with open('ontology_pickled.pk', 'rb') as fi:
    g = pickle.load(fi)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    req_query = request.args.get('query')
    if req_query is None:
        return "\
        <h1>How to use the SPARQL endpoint: </h1>\
        <ul>\
            <li>The endpoint is a regular HTTP get request.</li>\
            <li>Add your SPARQL Query as query parameter e.g. '.../api/sparql?query={YOUR SPARQL QUERY}'</li>\
            <li>Make sure that your SPARQL Query does not include prefix definitions e.g. @PREFIX vu <something> instead start the query with SELECT ...</li>\
            <li>Your Query must contain whitespace (which are automatically parsed with %)</li>\
            <li>The response is a JSON</li>\
            <li>The endpoint uses RDFLib, thus all queries that RDFLib allows are valid and vice versa.</li>\
        </ul>\
        "
    else:
        req_query = request.args.get('query')
        qres = g.query(req_query)
        return Response(qres.serialize(format="json"))
