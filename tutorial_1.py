import cv2

def image_read_function(image_name):
    read_image = cv2.imread(image_name)
    return read_image

def image_show_function(read_image):
    cv2.imshow('image', read_image)
    cv2.waitKey(0)

def image_rotate_function(read_image, angle=45.0):
    height = read_image.shape[0]                         
    width = read_image.shape[1]  
    center = (int(width/2), int(height/2))
    scale = 1.0
    trans = cv2.getRotationMatrix2D(center, angle , scale)
    image2 = cv2.warpAffine(read_image, trans, (width,height))
    return image2

def image_gray_function(read_image):
    gray_image = cv2.cvtColor(read_image, cv2.COLOR_BGR2GRAY)
    return gray_image


if __name__ == '__main__':
    read_image  = image_read_function('lena.png')
    gray_image = image_gray_function(read_image)
    rotate_image = image_rotate_function(gray_image)
    image_show_function(rotate_image)
