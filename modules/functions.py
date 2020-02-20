import cv2
def 画像を読み込むやつ(画像の名前):
    読み込んだ画像 = cv2.imread(画像の名前)

    return 読み込んだ画像

def 画像を表示するやつ(読み込んだ画像):
    cv2.imshow('画像', 読み込んだ画像)
    cv2.waitKey(0)

def 画像を回転するやつ(読み込んだ画像, 角度=45.0):
    高さ = 読み込んだ画像.shape[0]                         
    幅 = 読み込んだ画像.shape[1]  
    中心の座標 = (int(幅/2), int(高さ/2))
    倍率 = 1.0
    回転行列 = cv2.getRotationMatrix2D(中心の座標, 角度 , 倍率)
    回転した画像 = cv2.warpAffine(読み込んだ画像, 回転行列, (幅,高さ))
    return 回転した画像

def 画像をグレーにするやつ(読み込んだ画像):
    グレーの画像 = cv2.cvtColor(読み込んだ画像, cv2.COLOR_BGR2GRAY)
    return グレーの画像
