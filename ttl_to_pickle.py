from rdflib import Graph, RDF, Namespace, Literal, URIRef
import pickle
import argparse


parser = argparse.ArgumentParser(
    description='Transforming a ttl file into a parsed python object using pickle. The output file name is "ontology_pickled.pk".')

parser.add_argument('file_path', type=str, nargs=1,
                    help='Give the full input file path.')

args = parser.parse_args()


g = Graph()
g.parse(args.file_path[0], format="turtle")

# saving the parsed graph in the root directory of the website
# this is done so that the serverless function does not need
# to parse the graph each time which is compute intensive
with open("./ontology_pickled.pk", 'wb') as f:
    pickle.dump(g, f)
