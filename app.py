from flask import Flask,render_template,jsonify

app = Flask(__name__)



JOBS = [
    {
        "id": 1,
        "title": "Pompier",
        "location": "Romania",
        "salary": "120,000 RON"
    },
    {
        "id": 2,
        "title": "Salvamar",
        "location": "Romania, Bulgaria",
        "salary": "130,000 RON"
    },
    {
        "id": 3,
        "title": "Politist",
        "location": "Romania",
        "salary": "180,000 RON"
    },
    {
        "id": 4,
        "title": "Gradinar",
        "location": "Romania",
        "salary": "120,000 RON"  
    }
]

        

@app.route("/")
def hey():
    return render_template("home.html", jobs=JOBS)

@app.route("/api")
def list_job():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)