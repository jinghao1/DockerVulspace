import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from demo.global_var import dt_set_value

app = Flask(__name__)
curDir = os.path.dirname(__file__)

sqlitePath = str(os.path.join(curDir, "./db.sqlite3"))
app.config['SQLALCHEMY_BINDS'] = {
    "sqlite3": "sqlite:///"+sqlitePath,
    # "mysqlDb": "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format("mysiteuser", "mysitepass", "mysqldb", "3306", "mysite"),
    # "pySqlDb": "postgresql://{}:{}@{}:{}/{}".format("mysiteuser", "mysitepass", "postgresql", "5432", "mysite")
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# from dongtai_agent_python.middlewares.flask_middleware import AgentMiddleware
# app.wsgi_app = AgentMiddleware(app.wsgi_app, app)

db = SQLAlchemy(app)
dt_set_value("app",app)
dt_set_value("db",db)

from routes import setup_routes
setup_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
