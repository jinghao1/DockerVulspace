from demo.global_var import dt_get_value

db = dt_get_value("db")


class UserMysql(db.Model):
    __tablename__ = 'muser'
    __bind_key__ = 'mysqlDb'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    phone = db.Column(db.String(120), unique=False)


class UserPostgreSQL(db.Model):
    __tablename__ = 'puser'
    __bind_key__ = 'pySqlDb'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    phone = db.Column(db.String(120), unique=False)


class Usersqlite(db.Model):
    __bind_key__ = 'sqlite3'
    __tablename__ = 'suser'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    phone = db.Column(db.String(120), unique=False)