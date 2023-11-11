import pandas as pd

# 1. `hypocenter_convert_test.csv`を読み込む
hypocenter_convert = pd.read_csv(
    "hypocenter_convert.csv", dtype={'大地域区分番号': str})
# 小地域区分番号を数値に変換
hypocenter_convert['小地域区分番号'] = pd.to_numeric(
    hypocenter_convert['小地域区分番号'], errors='coerce')

# 2. `hypocenter_name.csv`を読み込み、小地域区分番号を数値に変換
hypocenter_name = pd.read_csv("hypocenter_name.csv", dtype={'大地域区分番号': str})
hypocenter_name['小地域区分番号'] = pd.to_numeric(
    hypocenter_name['小地域区分番号'], errors='coerce')

# 3. 両データフレームを大地域区分番号と小地域区分番号で結合する
merged = pd.merge(hypocenter_convert, hypocenter_name[['大地域区分番号', '小地域区分番号', '震央地名(漢字)']],
                  on=['大地域区分番号', '小地域区分番号'], how='left')

# 4. 小地域区分番号と観測点数を数値に変換し、その後整数型(Nullable Integer)に変更
merged['小地域区分番号'] = pd.to_numeric(
    merged['小地域区分番号'], errors='coerce').astype('Int64')
merged['観測点数'] = pd.to_numeric(merged['観測点数'], errors='coerce').astype('Int64')

# 5. 震央地名の位置を特定し、震央地名(漢字)をその右側に配置するカラムの順序を生成する
index_of_shincho = merged.columns.to_list().index('震央地名')
columns_order = merged.columns.to_list(
)[:index_of_shincho+1] + ['震央地名(漢字)'] + merged.columns.to_list()[index_of_shincho+1:-1]
merged = merged[columns_order]

# 6. 結果をCSVファイルとして出力する
merged.to_csv("hypocenter_convert_add_name.csv", index=False)
