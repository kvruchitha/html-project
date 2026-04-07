from flask import Flask, render_template, request

app = Flask(__name__)

# First page
@app.route("/")
def home():
    return render_template("index2.html")
@app.route("/search", methods=["POST"])
def search():
    gene = request.form["gene"]
    handle = Entrez.esearch(db="gene", term=gene, retmax=5)
    record = Entrez.read(handle)
    handle.close()
    
    for gene_id in ids:
        summary= Entrez.esummary(db="gene",id=gene_id)
        data=Entrez.read(summary)

        gene_info =data["documentsummaryset"]["documentsummary"][0]

        results.append({
            "organi
        })
