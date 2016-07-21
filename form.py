from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory

# Create Flask application
app = Flask(__name__, static_url_path='')

# Routes
@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():
    import re
    from hazard_assessment_cas_lookup import process

    CASpattern = '\d+\-\d+\-\d+'
    text = request.form['text']
    CASlist = re.findall(CASpattern, text)
    process(CASlist)

    return Results()
    # return text

@app.route('/Results/Hazards')
def Hazards():
    return render_template("Hazards.html")

@app.route('/Results/Precautions')
def Precautions():
    return render_template("Precautions.html")

@app.route('/Results/PPE')
def PPE():
    return render_template("PPE.html")

@app.route('/Results/Inventory')
def Inventory():
    return render_template("Inventory.html")

@app.route('/Results/SDS')
def SDS():
    return send_from_directory('Results', 'SDS.zip')

@app.route('/Results')
def Results():
    return render_template("Results.html")

if __name__ == '__main__':
    app.run()
