from flask import Flask,render_template,request,render_template_string
from demo.common import SerializerJsonResponse

# safe
def xssTemplate():
    content = request.args.get("content","null")
    return render_template('xss_index.html',contents=content)


# safe
def xssTemplateString():
    message = request.args.get("content","null")
    template = (
        "<h2>{{ message }}</h2> "
        "<p>Note: This feature is still early in development, "
        "please reach out to Security if you have any feedback.</p>"
    )
    return render_template_string(template, message=message)


# no safe
def xssReturn():
    content = request.args.get("content", "null")
    return SerializerJsonResponse(content)