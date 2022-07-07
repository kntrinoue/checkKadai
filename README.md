# checkKadai
授業の課題で提出された中身を、学生間でどれくらいの類似度があるか、コピーしているものがあるかをチェックする

## ファイルの準備
* kadaiフォルダに、課題別でフォルダを作成する。
* 課題別フォルダにすべての学生の課題ファイル、もしくはフォルダ/課題ファイルを入れる。
* 学生のファイルもしくはフォルダには名前を含めておく。

## 実行方法
* checkKadai.pyの9行目の課題フォルダの名前を入れる。課題がフォルダ名が61,62,63,64の場合は  kadaiNum = [61,62,63,64] と書く。
* PythonでcheckKadai.pyのプログラムを実行する。
* 類似していると判定するthresholdは0.9としているが、課題の内容によって厳しく(課題の文量が多い)もしくは緩く(課題の文量が少ない)する。

## 結果
summary.txtとFig/ooo.pngが出力される。
* summary.txt：課題ごとに類似度が高い学生同士のファイルパス(名前)が書かれる。
* Fig/ooo.png：課題のフォルダ名(ooo)の(類似度に関する)樹形図。一番下でクラスタ化されているものはコピー。summary.txtでsim=1.000と出る。樹形図の番号はsummary.txtのfrom_idとto_idでわかる。
