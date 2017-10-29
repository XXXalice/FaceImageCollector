import os
import glob
import random

def main():
    print('imgフォルダに入れた画像フォルダ名を入力してください')
    f = input('>> ')
    path = './img/'+f+'/'
    print('始めたい番号を入力してください')
    label1 = int(input('>> '))
    print('ラベル番号を入力してください（教師:0　逆教師:1）')
    label2 = input('>> ')

    files = glob.glob(path+'*')
    print(files)
    for i, file in enumerate(files, label1):
        try:
            os.rename(file, os.path.join(path + label2 + '_' + '{0:03d}'.format(i) + '.png'))
        except Exception as e:
            print(e)
            continue

if __name__ == '__main__':
    main()