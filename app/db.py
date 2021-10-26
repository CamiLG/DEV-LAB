from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    global db
    conf = app.config
    app.config['SQLALCHEMY_DATABASE_URI']=f'mysql://{conf["DB_USER"]}:{conf["DB_PASS"]}@{conf["DB_HOST"]}/{conf["DB_NAME"]}'
    db.init_app(app)
    db.create_all()

'''
def connection():
    if "db_conn" not in g:
        conf = current_app.config
        g.db_conn = pymysql.connect(
            host=conf["DB_HOST"],
            user=conf["DB_USER"],
            password=conf["DB_PASS"],
            db=conf["DB_NAME"],
            cursorclass=pymysql.cursors.DictCursor,
        )

    return g.db_conn


def close(e=None):
    conn = g.pop("db_conn", None)

    if conn is not None:
        conn.close()


def init_app(app):
    app.teardown_appcontext(close)
'''