from flask import Flask, request, url_for, render_template, redirect
from xml.dom import minidom

USERNAME = "song"
PASSWORD = "jing"


def doLogin():

    try:
        DOMTree = minidom.parseString(request.data)
        username = DOMTree.getElementsByTagName("username")
        username = username[0].childNodes[0].nodeValue
        password = DOMTree.getElementsByTagName("password")
        password = password[0].childNodes[0].nodeValue

        if username == USERNAME and password == PASSWORD:
            result = "<result><code>%d</code><msg>%s</msg></result>" % (1, username)
        else:
            result = "<result><code>%d</code><msg>%s</msg></result>" % (0, username)
    except Exception as e:
        result = "<result><code>%d</code><msg>%s</msg></result>" % (3, e.message)

    return result, {'Content-Type': 'text/xml;charset=UTF-8'}

