#两张图片拼为一张图片
import PIL.Image as Image
import os,sys
from skimage import io,transform,data_dir
import skimage.io as io
import numpy as np
import cv2
import scipy.io as scio
import os

#stry='C:/rl1/*.jpg'
#colly=io.ImageCollection(stry)
#strl='C:/rl3/*.jpg'
#colll=io.ImageCollection(strl)

file_namey = os.listdir('C:/rl1')
file_namel = os.listdir('C:/rl3')
for i in range(len(file_namey)):
    if(file_namey[i]==file_namel[i])
        toImage=Image.new('RGB',(512,256)，（0,0,0）)  #新建一个图片，第一个大小，第二个颜色
        locy=(0,0)                          #图片左上角坐标
        lochhh=(256,0)
        fromImagey=Image.open('C:/rl1/'+file_namey[i])
        fromImagel=Image.open('C:/rl3/'+file_namel[i])
        toImage.paste(fromImagey,locy)     #粘贴图片到新图片上
        toImage.paste(fromImagel,lochhh)
        io.imsave('c:/rl4/'+np.str(i)+'.jpg',toImage)    #保存图片