from flask import render_template
from flask import Flask
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route("/mypage/me", methods=['GET', 'POST'])
def about_me():
    if request.method == 'GET':
        items_dict = {"Imię": "Bridget", "Nazwisko": "Bardot"}
        return render_template("wizytowka_omnie.html", items=items_dict)
    elif request.method == 'POST':
        return redirect(url_for('contact'))


@app.route("/mypage/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        items_dict = {"Telefon": "555-555-555", "Email": "bridget.bardot@star.com"}
        return render_template("wizytowka_kontakt.html", items=items_dict)
    elif request.method == 'POST':
        message = request.form['message']
        print(message)
        return redirect(url_for('contact'))
