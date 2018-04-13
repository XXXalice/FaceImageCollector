import os
import glob

def main():
    print('教師データのフォルダ名を入力してください')
    tpath = './img/' + input('>> ') + '/'
    print('逆教師データのフォルダ名を入力してください')
    dpath = './img/' + input('>> ') + '/'
    print('テキストファイルの名前を入力してください　ex:train test')
    fname = input('>> ')

    tfiles = glob.glob(tpath+'*')
    dfiles = glob.glob(dpath+'*')

    with open('./txt/'+fname+'.txt','w') as f:
        for file in tfiles:
            f.write(file.split('/')[3]+ ' 0')
            f.write('\n')

    with open('./txt/'+fname+'.txt','a') as f:
        for file in dfiles:
            f.write(file.split('/')[3]+ ' 1')
            f.write('\n')

if __name__ == '__main__':
    main()