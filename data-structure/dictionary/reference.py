products = {
    "banana": 100,
    "apple": 150,
    "eggplant": 130
}

"""
キーの取得
"""
products.keys()

"""
 値の取得
"""
products.values()


"""
キーから参照
"""

banana_price = products["banana"]
#エラー発生
anonymous = products["hoge"]

"""
キーから参照(メソッド)
"""

banana_price = products.get("banana")
#Noneが格納
anonymous = products.get("hoge")

"""
キーの存在確認
"""

if "orange" in products:
    print("OK")
else:
    print("NG")