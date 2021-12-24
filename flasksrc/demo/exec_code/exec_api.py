import json,os,yaml,subprocess
from flask import request
from demo.common import SerializerJsonResponse


# 代码执行
# description=_("code execution api of eval;eg: code=__ import __('os').system('whoami') "),
def eval_post_e():
    ser = request.form
    if ser:
        code = ser['code']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    end = eval(code)
    return SerializerJsonResponse(end)


# yaml 代码执行
# description=_("code execution api of yaml.unsafe_load;eg: code=whoami"),
def yaml_post_e():
    ser = request.form
    if ser:
        code = ser['code']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    exp = """!!python/object/apply:os.system ['{}']""".format(code)
    # yaml.__version__ < 5.1 hook yaml.load()  default UnsafeLoader
    end = yaml.unsafe_load(exp)
    return SerializerJsonResponse(end)



