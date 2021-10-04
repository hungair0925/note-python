products = {
    "banana": 100,
    "apple": 150,
    "eggplant": 130
}

"""
更新
"""
new_product = {
    "orange": 80
}

update_price_product = {
    "banana": 200
}

products.update(new_product)
products.update(update_price_product)

"""
キーから削除(返り値あり)
"""
apple_price = products.pop("apple")

"""
キーから削除(返り値無し)
"""
del products["eggplant"]

"""
初期化
"""
products.clear()


"""
コピー
"""

name_by_age = {
    "Taro": 20,
    "Hanako": 18
}
new_name_by_age = name_by_age.copy()

