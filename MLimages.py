# 10/20/2017
# Created by Ajinkya Bobade
#program to detect corrupt jpg images


import os
from os import listdir
from PIL import Image
count=0


for filename in os.listdir('/Users/ajinkyabobade/Downloads/2/'):# mention your file path here for example in my case i have all the images in folder named "2" which is inside in downloads
    if filename.upper().endswith('.JPG'):
     try:   # These next functions may produce an exception
         img = Image.open('/Users/ajinkyabobade/Downloads/2/' + filename)# mention your file path here for example in my case i have all the images in folder named "2" which is inside in downloads
         img.verify()


     except(IOError,SyntaxError)as e:# These are the exceptions we're looking for
         print('Bad file  :  '+filename) # print out the names of corrupt files
         count=count+1
         print(count)

print('Im done')