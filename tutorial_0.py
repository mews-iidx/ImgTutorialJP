import cv2

if __name__ == '__main__':
    read_image = cv2.imread('lena.png')
    gray_image = cv2.cvtColor(read_image, cv2.COLOR_BGR2GRAY)
    height = read_image.shape[0]                         
    width = read_image.shape[1]  
    center = (int(width/2), int(height/2))
    scale = 1.0
    angle = 45.0
    trans = cv2.getRotationMatrix2D(center, angle , scale)
    rotate_image = cv2.warpAffine(gray_image, trans, (width,height))
    cv2.imshow('image', rotate_image)
    cv2.waitKey(0)
