from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

def initialize_firebase_app():
    cred = credentials.Certificate('./tracrime.json')
    firebase_admin.initialize_app(cred)

initialize_firebase_app()  

@app.route('/')
def home_html():
    return render_template('home.html', title='Home')

@app.route('/about/')
def about_html():
    return render_template('about.html', title='About')

@app.route('/recent crimes/')
def recent_crimes_html():
    return render_template('recent_crimes.html', title='Recent Crimes', crimes=crimes)

if __name__ == '__main__':
    db = firestore.client()
    crimes_ref = db.collection('Crime_Records')
    crimes = [doc.to_dict() for doc in crimes_ref.get()]
    print( crimes )
    app.run(debug=True)
