from flask import Flask, request, render_template, redirect, url_for
from app import app, utils
import requests

from app.db import db_session, Urls

u = Urls

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name="bar", title='Index page')

@app.route('/cut', methods=['POST'])
def cut():
    print(request.form.get("longUrl"))
    longUrl = utils.convert(str(request.form.get("longUrl")))
    req = u.query.filter(u.longUrl==longUrl).first()
    print(req)
    if(req != None):
        shortUrl = req.shortUrl
    else:
        shortUrl = utils.random_string(size=4)
        db_session.add(Urls(shortUrl, longUrl))
        db_session.commit()
    response = {"status": True, "shortUrl":shortUrl, "longUrl": longUrl}
    print(longUrl)
    try:
        requests.get(response["longUrl"])
    except:
        response["status"] = False
    return render_template('cut.html', response = response)
@app.route('/template')
def lol():
    return render_template('index.html', name="lol")

@app.route('/<shortUrl>')
def display(shortUrl):
    req = u.query.filter(u.shortUrl==shortUrl).first()
    print(req)
    if(req != None):
        return redirect(req.longUrl)