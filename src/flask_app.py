from flask import Flask,request,jsonify
from dongtai_agent_python.middlewares.flask_middleware import AgentMiddleware
app = Flask(__name__)

# from crypto.Hash import SHA384
# h = SHA384.new()
# h.update(b'Hello')
# print(h.hexdigest())
app.wsgi_app = AgentMiddleware(app.wsgi_app, app)


@app.route('/', methods=["GET","POST"])
def hello_world():
    name = request.args.get("name")
    print(name)
    return 'Hello, World!'


if __name__ == "__main__":

    app.run(debug=True, port=8080)