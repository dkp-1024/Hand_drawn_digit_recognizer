# it is expected to convert the csv file to an image
# worked 
import csv
import numpy
import cv2
import matplotlib.pyplot as plt

reader = csv.reader(open('train1.csv'))
header = reader.__next__()
data=[]


for row in reader:
   data.append(row)

data=numpy.array(data)
ro=numpy.zeros((28,28,3))


for i in range(0,27):
   for j in range(0,27): 

     ro[i,j,0]=data[3,j+i*28]
     ro[i,j,1]=data[3,j+i*28]
     ro[i,j,2]=data[3,j+i*28]


cv2.imwrite('image.png',ro)
