#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# from flask import Flask
# from flask import request, jsonify
# import json,copy
# from dongtai_agent_python.middlewares.flask_middleware import AgentMiddleware
# import pymysql
# pymysql.install_as_MySQLdb()

# import MySQLdb
# app = Flask(__name__)
# if __name__ == '__main__':

#     app.wsgi_app = AgentMiddleware(app.wsgi_app,app)
#     app.run()

# exit()

import rasp
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':

    main()

