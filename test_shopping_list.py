import unittest
from shopping_list_10 import ShoppingList # 注意from后面的模块要求按照变量命名规则来命名，不能以数字开头

class TestShoppingList(unittest.TestCase):
    """注意定义的函数前面一定要以test_开头，这样才会被识别运行"""
    def test_get_item_price(self):
        shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})
        self.assertEqual(shopping_list.get_total_price(),53)
    def test_get_item_count(self):
        shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})
        self.assertEqual(shopping_list.get_item_count(), 3)
    """终端输入：python -m unittest (加文件名则只运行指定的测试文件)运行测试"""

class TestShoppingList2(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})
    def test_get_item_price(self):
        self.assertEqual(self.shopping_list.get_total_price(),53)
    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)