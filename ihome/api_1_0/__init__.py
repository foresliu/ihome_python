
# coding:utf-8

from flask import Blueprint

# 创建蓝图对象
api = Blueprint("api_1_0", __name__)

# 导入蓝图的视图，让程序知道在api_1_0包下有个demo.py文件
from . import demo, verify_code, passport, profile, houses
