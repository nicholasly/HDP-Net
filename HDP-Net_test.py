import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
sys.path.append('/usr/local/lib/')
sys.path.append('/home/lyh/caffe/python')
import caffe
import numpy as np
import math
import time
import cv2
from skimage import transform

def GenerateOutput(im_path, height, width):
	caffe.set_mode_cpu()
	net = caffe.Net('deploy/test_NightDehaze.prototxt', 'model/Dehaze_iter_30000.caffemodel', caffe.TEST)
	net.blobs['data'].reshape(1,3,height,width)
	transformers = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
	transformers.set_transpose('data', (2,0,1))
	transformers.set_channel_swap('data', (2,1,0))
	im = caffe.io.load_image(im_path)
	transformed_image = transformers.preprocess('data', im)
	net.blobs['data'].data[...] = transformed_image
	out = net.forward()
	images = np.array(out['eltwise_g'])
	channel_swap = (0, 2, 3, 1)
	images = images.transpose(channel_swap)
	return images[0]

if __name__ == '__main__':
	if not len(sys.argv) == 2:
                print 'Usage: python DeHazeNet.py haze_img_path'
		exit()
	else:
		im_path = sys.argv[1]
	src = cv2.imread(im_path)
        height = src.shape[0]
	width = src.shape[1]
        height = height//2//2*2*2
        width = width//2//2*2*2
        if(width!= src.shape[1] or height != src.shape[0]):
             src = transform.resize(src, (height,width))
        start = time.clock()
	output = GenerateOutput(im_path, height, width)
        end = time.clock()
        print "read:%f s" % (end - start)
        I = src/255.0
	cv2.imwrite('result/Dehaze_01.jpg', output*255)
