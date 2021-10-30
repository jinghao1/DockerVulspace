import json,os,yaml,subprocess
from flask import request
from demo.common import SerializerJsonResponse


# 命令执行
#   description=_("System command execution api of os.system;eg: code=whoami"),
def exec_post_e():
    ser = request.form
    if ser:
        code = ser['code']
    else:
        return SerializerJsonResponse(None,202,"params error")
    new_code = "ping -c1 {}".format(code)
    end = os.system(new_code)
    return SerializerJsonResponse(end)


# 命令执行
#  description=_("System command execution api of os.popen and get List of all files in the folder; eg: code=ls"),
def exec_post_popen():
    ser = request.form
    if ser:
        code = ser['code']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    # 文件夹内所有文件的列表.
    files = os.popen(code).readlines()
    return SerializerJsonResponse(files)


# 子进程命令执行
# description=_("System command execution api of os.popen ; eg: cmd=cat,name=/etc/passwd"),
def exec_post_subprocess():
    ser = request.form
    if ser:
        cmd = ser['cmd']
        name = ser['name']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    # 将一个子进程的输出，作为另一个子进程的输入：
    child1 = subprocess.Popen([cmd, name],
                              stdout=subprocess.PIPE)

    child2 = subprocess.Popen(["grep", "0:0"],
                              stdin=child1.stdout,
                              stdout=subprocess.PIPE)
    out = child2.communicate()

    outInfo = out[0]
    if isinstance(outInfo,bytes):
        outInfo = str(outInfo, encoding="utf-8")
    return SerializerJsonResponse(outInfo)


# 命令执行
# description=_("System command execution api of os.popen ; eg: cmd=whoami"),
def cmd_exec():
    ser = request.form
    if ser:
        cmd = ser['cmd']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    magic = [].__class__.__base__.__subclasses__()
    ret = []
    for item in magic:
        if "<class 'subprocess.Popen'>" == str(item):
            ret_in = item.__init__.__globals__['os'].system(cmd)
            ret.append(str(ret_in))

    return SerializerJsonResponse(",".join(ret))