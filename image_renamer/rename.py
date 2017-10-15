import os
import glob

def main():
    print('imgフォルダに入れた画像フォルダ名を入力してください')
    f = input('>> ')
    path = './img/'+f+'/'
    print('始めたい番号を入力してください')
    label = int(input('>> '))

    files = glob.glob(path+'*')

    for i, file in enumerate(files, label):
        try:
            os.rename(file, path + str(i) + '.png')
        except Exception as e:
            print(e)
            continue

if __name__ == '__main__':
    main()