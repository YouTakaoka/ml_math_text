import numpy as np
import numpy.linalg as LA

# n個の数値を受取り，指定したタイプtに変換してリストに格納して返す関数
def my_input(n, t):
    line = list(map(t, input().split()))
    if len(line) is not n:
        raise Exception('入力データ数が合っていません')
    return line

# パラメータの入力
# n: 入力データの次元
# m: データ点の数
# l: 圧縮後のデータ次元
n, m, l = my_input(3, int)
if l > n:
    raise Exception('lはn以下にしてください．')
# データ入力
x = [[xij for xij in my_input(n, float)] for _ in range(m)]
# numpy配列に変換
x = np.array(x)

# 行列Sを計算
s = x.T @ x
# Sの固有値・固有ベクトルを計算
# w: 固有値のリスト， v: 固有ベクトルのリスト（列が個々の固有ベクトル）
w, v = LA.eig(s)
# 後のため，行が固有ベクトルを表わすように転置
v = v.T
# 固有ベクトルを固有値の降順にソート
li = list(zip(w, v))
li.sort(key=lambda x: -x[0])
# 行列Aを構成
a = [i[1] for i in li[:l]]
a = np.array(a).T

print(a)
