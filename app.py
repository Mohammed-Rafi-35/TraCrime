from flask import Flask, render_template

app = flask(__name__)

@app.route('/')
def home_html():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)