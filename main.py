from flask import Flask, render_template, request

app = Flask(__name__)

# First page
@app.route("/")
def home():
    return render_template("index.html")

# Search result page
@app.route("/search")
def search():
    gene = request.args.get("gene")
    return render_template("result.html", gene=gene)

if __name__ == "__main__":
    app.run(debug=True)