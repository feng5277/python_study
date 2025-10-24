# python测试（找bug）
class ShoppingList:
    def __init__(self,shopping_list):
        self.shopping_list = shopping_list
    """返回购物车清单上有多少项商品"""
    def get_item_count(self):
        return len(self.shopping_list)
    """返回购物车商品总额"""
    def get_total_price(self):
        total = 0
        for price in self.shopping_list.values():
            total += price
        return total