ここに課題ごとのフォルダを作成する。
そして、その課題ごとのフォルダに、学生ごとの課題ファイル、もしくはフォルダ/課題のファイルを置く。
例1はMoodleからダウンロードすることを想定している。

例1)

kadai1/学生A/ex1.c

kadai1/学生B/ex1.c

kadai1/学生C/ex1.c

例2)   この場合はcheckKadai.pyの13行目　filenames = glob.glob("./kadai/"+str(kadaiN)+"/*")　に修正する

kadai1/学生A.c

kadai1/学生B.c

kadai1/学生C.c
