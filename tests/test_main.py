#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MCP 测试项目的单元测试
"""

import unittest
import sys
import os

# 添加 src 目录到 Python 路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import MCPDemo

class TestMCPDemo(unittest.TestCase):
    """测试 MCPDemo 类的功能"""
    
    def setUp(self):
        """测试前的设置"""
        self.demo = MCPDemo("测试实例")
    
    def test_initialization(self):
        """测试初始化功能"""
        self.assertTrue(self.demo.initialized)
        self.assertEqual(self.demo.name, "测试实例")
    
    def test_run(self):
        """测试运行功能"""
        result = self.demo.run()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()