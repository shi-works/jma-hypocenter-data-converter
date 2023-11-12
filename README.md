# jma-hypocenter-data-converter
## プログラムについて
- 本プログラムは、気象庁が公開している、[地震月報(カタログ編)の震源データ（1919～2022年3月）](https://www.data.jma.go.jp/eqev/data/bulletin/hypo.html)を読みやすい形式（GISデータ）に変換するプログラムです。
- オープンソースソフトウェアで構築

## データの入手
- 以下の気象庁のサイトより地震月報(カタログ編)の震源データ（dat）を入手します。
- https://www.data.jma.go.jp/eqev/data/bulletin/hypo.html
- なお、一括で震源データ（dat）をダウンロードするPythonスクリプトは以下にあります。
- https://github.com/shi-works/jma-hypocenter-data-converter/blob/main/src/dat_dl.py

## 震源データのマージとCSV形式への変換（dat_converter.py）
- 震源データ（dat）は、複数のファイル、かつ、固定長になっているので、データのマージとCSV形式に変換します。
### 使用データ
- 震源データ（datファイル）一式
### 出力結果
#### 震源データ（CSV形式）
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter.csv`,643MB

## 震源データを読みやすい形式へ変換（hypocenter_converter.py）
- 震源データ（CSV形式）を読みやすい形式（CSV形式）に変換するプログラムです。
- 震源データの西暦、月、日、時、分、秒より地震IDを作成し、付与しています。
- 震源データの西暦、月、日、時、分、秒よりDatTime及びUnixTimeを作成し、付与しています。
- 震源データの緯度(度)、緯度(分)、経度(度)、経度(分)よりLatitude、Longitudeを作成しています。
- 属性情報は必要最小限にしていますので適宜改変してください。
### 使用データ
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter.csv`,643MB
### 出力結果
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_convert.csv`,499MB

## 震源データに震央地名を付与（hypocenter_converter_add_name.py）
- 震央地名表を用いて、震源データに震央地名（漢字）を付与するプログラムです。
### 使用データ
#### 震源データ
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_convert.csv`,499MB
#### 震央地名表
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_name.csv`,15KB
### 出力結果
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_convert_add_name.csv`576MB

## 震源データをGISデータ（FaltGeobuf形式及びGeoParquet形式）へ変換
- 震源データのGISデータ（FaltGeobuf形式及びGeoParquet形式）への変換には[QGIS（バージョン3.28.4）](https://qgis.org/ja/site/)を使用します。
### 使用データ
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_convert_add_name.csv`576MB
### 出力結果（FaltGeobuf形式及びGeoParquet形式）
#### FaltGeobuf形式
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_convert_add_name.fgb`,1.4GB
#### GeoParquet形式（QGIS表示用）
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_convert_add_name.parquet`,234MB

## FaltGeobuf形式からPMTiles形式への変換
FaltGeobuf形式から[PMTiles形式](https://github.com/protomaps/PMTiles)への変換には[feltのtippecanoe](https://github.com/felt/tippecanoe)を使用します。
### 使用データ（FaltGeobuf形式）
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_convert_add_name.fgb`,1.4GB
### 出力結果（PMTiles形式）
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_convert_add_name.pmtiles`,2.4GB,ズームレベル0-14（精度0.5m）  
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_convert_add_name_Z4_z9_r2.pmtiles`,408MB,ズームレベル4-9（精度20m）

### ベクトルタイル設計情報
- 震源データそのものを可能な限り生かしたデータです。
- tippecanoeによるデータの間引き（自動）は行っていません。

### ズームレベル範囲
- 0-14 or 4-9

### 属性
- 震源データの属性はそのまま生かしています。

### PMTiles Viewer
- PMTilesはPMTiles Viewerで閲覧することができます。
- https://protomaps.github.io/PMTiles/

## デモサイト
- MapLibre GL JSで構築
- [産総研のシームレス標高タイル(統合DEM)](https://tiles.gsj.jp/tiles/elev/tiles.html#h_mixed)（3D地形）に震源データを重ねています。
- https://shi-works.github.io/aist-dem-with-hypocenter-on-maplibre-gl-js
- サンプル画像
![image](https://github.com/shi-works/jma-hypocenter-data-converter/assets/71203808/80f707d0-aa05-4d78-b7c5-bfab5f005142)
### 使用データ
`https://xs489works.xsrv.jp/pmtiles-data/jma-hypocenter/hypocenter_convert_add_name_Z4_z9_r2.pmtiles`,408MB,ズームレベル4-9（精度20m）

## データ使用上の注意
- データを使用するにあたり、下記のデータフォーマットや気象庁の地震カタログの解説を必ずご確認ください。
- データフォーマット  
https://www.data.jma.go.jp/eqev/data/bulletin/data/format/hypfmt_j.html
- 気象庁の地震カタログの解説  
https://www.data.jma.go.jp/svd/eqev/data/bulletin/data/hypo/relocate.html

## ライセンス
本プログラムは[MITライセンス](https://github.com/shi-works/jma-hypocenter-data-converter/blob/main/LICENSE)で提供されます。  
本データセットはCC-BY-4.0で提供されます。使用の際には本レポジトリへのリンクを提示してください。

また、本データセットは、気象庁が公開している、地震月報(カタログ編)の震源データを加工して作成したものです。本データセットの使用・加工にあたっては、[気象庁の利用規約](https://www.jma.go.jp/jma/kishou/info/coment.html)を必ずご確認ください。

## 免責事項
利用者が当該データを用いて行う一切の行為について何ら責任を負うものではありません。
