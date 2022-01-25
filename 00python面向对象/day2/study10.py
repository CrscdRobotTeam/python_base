# 动态加载模块,热加载
# 即程序运行过程中，动态加载

# 方法1
# __import__("study09")  # 解释器用的

# 方法2
import importlib

#importlib.import_module("study09")  # 官方推荐 同工程同包
importlib.import_module("day1.study01") # 同工程不同包
