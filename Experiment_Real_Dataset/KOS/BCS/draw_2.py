import numpy as np
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt


def plotaccuracy(dimsaftercompression,accuracy):    
	setof = [0.1,0.2,.3,0.4,0.5,0.6,0.7,0.8,0.9]
	plt.figure(figsize=(3,3))
	lst=[]
	for name, hex in matplotlib.colors.cnames.items():
		lst.append(hex)
	#plt.gca().set_color_cycle(lst[0:9])
	for i in range(accuracy.shape[0]):
		plt.plot(dimsaftercompression, accuracy[i], label = setof[i] )
	plt.xticks([50,500,1000, 1500, 2000])
	plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1])
	plt.xlabel('Compression Length')
	plt.ylabel('Accuracy')
	plt.legend(prop={'size':8},loc = 4)
	plt.savefig('1.jpg', bbox_inches='tight')
	plt.show()

def plotcompressiontime(dimsaftercompression,timetaken):
	plt.figure(figsize=(3,3))
	plt.plot(dimsaftercompression, timetaken)
	plt.xticks([50,500,1000, 1500, 2000])
	plt.yticks([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140])
	plt.xlabel('Compression Length')
	plt.ylabel('Compression Time (s)')
	plt.savefig('2.jpg', bbox_inches='tight')
	plt.show()


dimsaftercompression=[50, 100, 500, 1000, 1500, 2000]

b=np.load('thisis.npy')
#print (b.shape)
#print (b[0:10][4:10])
#c=b[0:10][4:10]
#print (c.shape)
#print (c.shape[0])
plotaccuracy([10,20,30,40,50,100, 500, 1000, 1500, 2000],b)

a=np.load('compression.npy')
print (a[4:])
plotcompressiontime(dimsaftercompression,a[4:])


