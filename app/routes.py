from flask import render_template, url_for
from flask import request
from app import app, db
from app.models import User


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('personal_home.html')


@app.route('/focus', methods=['GET', 'POST'])
def focus_app():
    if request.method == 'GET':
        print('GET entered')
        l = [u.userid for u in User.query.all()]
        return render_template('focus.html', ids=l)
    elif request.method == 'POST':
        # store posted data in python database
        u = User(userid=request.form.get('userid'), token=request.form.get('token'))
        db.session.add(u)
        db.session.commit()
        l = [u.userid for u in User.query.all()]
        return render_template('focus.html', ids=l)
    else:
        print('Other method??')


@app.route('/focus_send_notif')
def focus_send_notif():
    print("hello")
    return "nothing"
