import os
import csv

# 入力フォルダと出力ファイルのパスを定義
input_folder = './dat'
output_file = 'hypocenter.csv'

# CSVのヘッダー行をリストで定義
csv_header = [
    "地震ID", "レコード種別", "西暦", "月", "日", "時", "分", "秒", "標準誤差(秒)", "緯度(度)", "緯度(分)", "標準誤差(分)", "経度(度)",
    "経度(分)", "標準誤差(分)", "深さ(km)", "標準誤差(km)", "マグニチュード1", "マグニチュード1種別", "マグニチュード2",
    "マグニチュード2種別", "使用走時表", "震源評価", "震源補助情報", "最大震度", "被害規模", "津波規模", "大地域区分番号",
    "小地域区分番号", "震央地名", "観測点数", "震源決定フラグ"
]

record_counter = 0

# 秒をフォーマットする関数を定義


def format_seconds(seconds_str):
    # 空白削除、右0埋め
    seconds_str = seconds_str.strip().ljust(4, '0')
    return seconds_str


# 出力ファイルを開く
with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:

    # ヘッダー行を書き込む
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(csv_header)

    # 入力フォルダのファイル一覧をループで処理
    for file in os.listdir(input_folder):
        if file.endswith(''):
            # 入力ファイルのフルパスを作成
            input_file = os.path.join(input_folder, file)

            # 入力ファイルをバイナリ読み込みモードで開く
            with open(input_file, 'rb') as infile:
                # ファイルの各行をリストとして読み込む
                lines = infile.readlines()
                line_idx = 0
                # ファイルの各行をループで処理
                while line_idx < len(lines):
                    # 行をバイト列として読み込む
                    line_bytes = lines[line_idx]
                    # 行が'J'、'U'、または'I'で始まる場合に処理を実行
                    if line_bytes.startswith(b'J') or line_bytes.startswith(b'U') or line_bytes.startswith(b'I'):
                        # 秒を取得してフォーマットし、先頭2文字を取得
                        seconds = line_bytes[13:17].decode('utf-8')
                        seconds = format_seconds(seconds)
                        seconds = seconds[0:2]
                        # idを生成
                        id = line_bytes[1:5].decode('utf-8') + line_bytes[5:7].decode('utf-8') + line_bytes[7:9].decode(
                            'utf-8') + line_bytes[9:11].decode('utf-8') + line_bytes[11:13].decode('utf-8') + seconds
                        # バイト列をutf-8エンコーディングで文字列に変換してレコードを作成
                        record = [
                            id,
                            line_bytes[0:1].decode('utf-8'),
                            line_bytes[1:5].decode('utf-8'),
                            line_bytes[5:7].decode('utf-8'),
                            line_bytes[7:9].decode('utf-8'),
                            line_bytes[9:11].decode('utf-8'),
                            line_bytes[11:13].decode('utf-8'),
                            line_bytes[13:17].decode('utf-8'),
                            line_bytes[17:21].decode('utf-8'),
                            line_bytes[21:24].decode('utf-8'),
                            line_bytes[24:28].decode('utf-8'),
                            line_bytes[28:32].decode('utf-8'),
                            line_bytes[32:36].decode('utf-8'),
                            line_bytes[36:40].decode('utf-8'),
                            line_bytes[40:44].decode('utf-8'),
                            line_bytes[44:49].decode('utf-8'),
                            line_bytes[49:52].decode('utf-8'),
                            line_bytes[52:54].decode('utf-8'),
                            line_bytes[54:55].decode('utf-8'),
                            line_bytes[55:57].decode('utf-8'),
                            line_bytes[57:58].decode('utf-8'),
                            line_bytes[58:59].decode('utf-8'),
                            line_bytes[59:60].decode('utf-8'),
                            line_bytes[60:61].decode('utf-8'),
                            line_bytes[61:62].decode('utf-8'),
                            line_bytes[62:63].decode('utf-8'),
                            line_bytes[63:64].decode('utf-8'),
                            line_bytes[64:65].decode('utf-8'),
                            line_bytes[65:68].decode('utf-8'),
                            line_bytes[68:92].decode('utf-8'),
                            line_bytes[92:95].decode('utf-8'),
                            line_bytes[95:96].decode('utf-8')
                        ]

                        # レコードをCSVに書き込む
                        csv_writer.writerow(record)

                    # 次の行に進む
                    line_idx += 1
