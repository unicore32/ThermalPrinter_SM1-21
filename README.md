# ThermalPrinter_SM1-21

三栄電機 SM1-21用の簡易的なライブラリです。

Python library to manipulate SANEI SM1-21.

結構うろ覚えなのであしからず。気が向いたらライブラリ含め書き直します。

参考までに高専カンファレンスlolのブース発表で使用したプログラム(lol.py)を入れておきました。こちらに関しては、このライブラリは使ってません。tweepyがないと動作しませんのであしからず。

## 使い方

前提条件として、PIL(Pillow)とnumpyとpySerialがインストールされているものとします。

### SM1_21.SM1_21(port, baud)

プリンタの初期設定としてシリアルポートの接続開始及び、Shift-JIS使用のためのコマンドをプリンタに送信します。

* `port` : デバイスファイルの指定（初期：/dev/ttyS0）

* `baud` : ボーレートの指定（初期：115200[bps]）

#### command(text)

プリンタにコマンドを送信します。

コマンドの詳細に関しては以下のページを参考にしてください。

[http://www.sanei-elec.co.jp/downloads/command.html](http://www.sanei-elec.co.jp/downloads/command.html)

* `text` : 送りたいコマンド('\x00\x00'のように指定)

### text(text, flag, bold)

プリンタに文字列を送信します。  

* `text` : 印刷したい文字列

* `flag` : 値が1の場合は印字を行います。0の場合はバッファに記録のみ。

* `bold` : 太字指定です。1の場合のみ太字。

### output()

バッファに保存された文字列の印字を行います。

### tab()

水平タブを挿入します。(動作未確認)

### image(img_path, threshould, pitch)

画像の印刷を行います。PCのスペックによっては時間かかる。

* `img_path` : 画像のパスを指定

* `threshould` : 濃淡の閾値を指定（初期は200、少し濃淡の閾値を変えたいときは適宜変えるといいかも）

* `pitch` : 1回に処理を行う縦方向のドット数（初期は200、変更しないことを推奨します）
