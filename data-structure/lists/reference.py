a = [1, 3, 5, 5, 2, 3]

"""
値のインデックスを参照(小さい順から)
"""
first_three_index = a.index(3)

"""
値のインデックスを参照(指定インデックスから)
"""
three_index_from_specified_index = a.index(3, 2)

"""
指定した値の出現回数をカウント
"""
three_count = a.count(3)

"""
指定した値の存在チェック
"""
if 6 in a:
    print("exist")
else:
    print("not exist")