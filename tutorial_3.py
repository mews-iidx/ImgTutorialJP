import cv2
from modules.functions import *

if __name__ == '__main__':
    読み込んだ画像 =  画像を読み込むやつ('lena.png')
    グレーの画像 = 画像をグレーにするやつ(読み込んだ画像)
    回転した画像 = 画像を回転するやつ(グレーの画像, 角度=45.0)
    画像を表示するやつ(回転した画像)
