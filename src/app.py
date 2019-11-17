from flask import Flask, redirect, request, url_for
from  db.dbutils import *
from helpers.config import *


app = Flask(__name__)
domain="http://localhost:8001/"


@app.route('/error',methods = ['POST', 'GET'])
def error_page():
    return "Sorry the url entered is incorrect"


@app.route('/new/url',methods = ['POST', 'GET'])
def create_short_url():
    old_url=request.form.get('url_old')
    new_url= domain + config().generate_random_string()
    dbutils().update_new_url_in_db(old_url, new_url)
    return new_url


@app.route('/<random>',methods = [ 'GET'])
def fetch_and_reroute(random):
    data= dbutils().get_old_url_from_new_url(domain+random)
    if data:
        return redirect(str(data))
    else:
        return redirect(url_for('error_page'))



if __name__ == '__main__':
    app.run(debug=True, port=8001)