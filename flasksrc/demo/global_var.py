# -*- coding: utf-8 -*-
import os, json
global _global_dt_dict
from typing import IO


_global_dt_dict = {
    "app": False,
    "db": False
}


def _init():  # 初始化
    global _global_dt_dict


def dt_set_value(key, value):
    # 定义一个全局变量
    global _global_dt_dict
    _global_dt_dict[key] = value


def dt_get_value(key):
    global _global_dt_dict
    # 获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return _global_dt_dict[key]
    except Exception as e:
        print('读取'+key+'失败\r\n')
        return ""

