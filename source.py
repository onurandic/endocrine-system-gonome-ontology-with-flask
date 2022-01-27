from flask import Flask,render_template,request
from rdflib_helper import RDFHelper
app = Flask(__name__)


rdf = RDFHelper()


@app.route('/main',methods=['GET'])
def get_main():
    return render_template('index.html',output=None)

@app.route('/main', methods=['POST'])
def post_main():
    query = request.form["query"]
    output = rdf.process_query(query)
    return render_template('index.html',output=output)



@app.route('/dbpedia',methods=['GET'])
def getdbpedia():
    return render_template('index.html',dbpedia_output=None)

@app.route('/dbpedia', methods=['POST'])
def postdbpedia():
    query = request.form["dbpedia_output"]
    output = rdf.process_dbpedia_query(query)
    return render_template('index.html',dbpedia_output=output)

@app.route('/federated',methods=['GET'])
def getfederated():
    return render_template('index.html',federated=None)

@app.route('/federated', methods=['POST'])
def postfederated():
    query = request.form["federated"]
    output = rdf.process_federated(query)
    return render_template('index.html',federated=output)