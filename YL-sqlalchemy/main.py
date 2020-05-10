from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    db = db_session.create_session()
    jobs = db.query(Jobs).all()
    return render_template('jobs.html', jobs=jobs)


db_session.global_init('db/mars_explorer.db')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
