from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("./tracrime.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

@app.route('/')
def home_html():
    return render_template('home.html', title='Home')

@app.route('/about/')
def about_html():
    return render_template('about.html', title='About')

@app.route('/recent crimes/')
def recent_crimes_html():
    # Example: Fetch data from Firestore
    crimes = db.collection('Crime_Records').stream()
    crime_list = [crime.to_dict() for crime in crimes]
    return render_template('recent_crimes.html', title='Recent Crimes', crimes=crime_list)

if __name__ == '__main__':
    app.run(debug=True)
