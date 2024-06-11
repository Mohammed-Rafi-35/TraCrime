from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_html():
    return render_template('home.html', title = 'Home')

@app.route('/about/')
def about_html():
    return render_template('about.html', title = 'About')

@app.route('/recent crimes')
def recent_crimes_html():
    return render_template('recent_crimes.html', title = 'Recent Crimes')

if __name__ == '__main__':
    app.run(debug=True)