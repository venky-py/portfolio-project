from flask import Flask, render_template

app = Flask(__name__)

# Sample data for two individuals
individuals = {
    "individual1": {
        "name": "John Doe",
        "roll_no": "12345",
        "projects": [
            {"title": "Project A", "description": "This is the description for Project A."},
            {"title": "Project B", "description": "This is the description for Project B."},
        ]
    },
    "individual2": {
        "name": "Jane Smith",
        "roll_no": "67890",
        "projects": [
            {"title": "Project X", "description": "This is the description for Project X."},
            {"title": "Project Y", "description": "This is the description for Project Y."},
        ]
    }
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/individual1')
def individual1():
    return render_template('individual.html', individual=individuals["individual1"])

@app.route('/individual2')
def individual2():
    return render_template('individual.html', individual=individuals["individual2"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
