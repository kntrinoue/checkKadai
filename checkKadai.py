#演習のカンニング・コピーチェック
#Moodleから課題すべてをダウンロードを想定。フォルダの扱いが分かれば、他のシステムで課題を集めていても、12行目を修正して利用できる
import glob
from difflib import SequenceMatcher
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt #プログラムと同じフォルダにFigフォルダを作成する.課題ごとの樹形図が入る
threshold = 0.9 # 0-1の範囲で1に近いほど似ている。thresholdより大きい組み合わせを出力する


def checkCopy(kadaiN, fo, fig):
    #ある課題のファイルをフォルダからすべて取り出す
    filenames = glob.glob("./kadai/"+str(kadaiN)+"/*/*") #プログラムと同じフォルダにkadaiフォルダを作成.その下に/学生ごとのフォルダ/課題ファイル
    #for file in filenames:
    #    print(file)

    docs=[]
    for filename in filenames:
        # テキストファイルを読み出しdocsに代入 
        with open(filename,mode='r',encoding = 'utf-8-sig') as f:
            docs.append(f.read())

    #類似度計算
    sim= [[0 for i in range(len(docs))] for j in range(len(docs))]
    sim2=[[0 for i in range(len(docs))] for j in range(len(docs))]
    for from_id in range(len(docs)):
        for to_id in range(len(docs)):
            sim[from_id][to_id] = SequenceMatcher(None, docs[from_id], docs[to_id]).ratio() # 0-1
            sim2[from_id][to_id] = 1 - SequenceMatcher(None, docs[from_id], docs[to_id]).ratio()
            #sim2[from_id][to_id] = sim2[to_id][from_id]
            if sim[from_id][to_id] > threshold and from_id>to_id: #0.9くらいから怪しい
                #print('doc_id:', from_id)
                fo.write('from_id:'+str(from_id)+', to_id:'+str(to_id)+'\n')
                print('from_name:', filenames[from_id])
                fo.write('from_name:'+filenames[from_id]+'\n')
                
                fo.write('to_name:'+filenames[to_id]+'\n')
                print('to_name:', filenames[to_id])
                fo.write('\tsim[{0}][{1}] = {2:f}'.format(
                    from_id, to_id, sim[from_id][to_id])+'\n')
                print('\tsim[{0}][{1}] = {2:f}'.format(
                    from_id, to_id, sim[from_id][to_id]))

    Z = linkage(sim2, method='ward')
    def draw_dendrogram(Z):
        # デンドログラムの作成
        #fig=plt.figure(figsize=(14, 5))
        plt.ylabel('Distance')
        dendrogram(
            Z,
            leaf_rotation=90.,
            leaf_font_size=8.
        )
        #plt.show()
        fig.savefig("./Fig/"+str(kadaiN)+".png")
        plt.cla()

    draw_dendrogram(Z) #樹形図で一番下に並んでるものは完全コピー
    fo.write("***********\n")


#main
#課題のフォルダ名のリストを書く
kadaiNum = [61,62,63,64,71,72,73,81,82,83,84,91,92,93,101,102,111,112,113,121,122,123]

fo = open('summary.txt','w')
fig=plt.figure(figsize=(14, 5))
for i in kadaiNum:
    print(i)
    fo.write(str(i)+"\n")
    checkCopy(i, fo, fig)

fo.close()
