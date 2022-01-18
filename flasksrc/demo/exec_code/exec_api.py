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

    # whoami
    exp = """!!python/object/apply:os.system ['{}']""".format(code)
    end = yaml.unsafe_load(exp)

    # https://github.com/yaml/pyyaml/issues/420
    # __import__('os').system('whoami')
#     exp = """
# !!python/object/new:tuple
# - !!python/object/new:map
#   - !!python/name:eval
#   - [ "{}" ]""".format(code)
#     end = yaml.load(exp)

    return SerializerJsonResponse(end)



