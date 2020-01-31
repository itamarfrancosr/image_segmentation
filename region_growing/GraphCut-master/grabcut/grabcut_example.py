import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('E:\\webpage\\image_segmentation\\region_growing\\GraphCut-master\\resource\\avocado3.jpg')
mask = np.zeros(img.shape[:2], np.uint8)
plt.imshow(img), plt.colorbar(), plt.show()

#
rect = (1, 100, 390, 180)
color = (255, 0, 0) # Blue color in BGR
thickness = 2
img_rect = cv.rectangle(img, rect, color, thickness)
plt.imshow(img_rect), plt.colorbar(), plt.show()


bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img*mask2[:, :, np.newaxis]
plt.imshow(img), plt.colorbar(), plt.show()


# newmask is the mask image I manually labelled
path = "E:\\webpage\\image_segmentation\\region_growing\\GraphCut-master\\resource\\"
newmask = cv.imread(path+'avocado3_mask2.png',0)
# wherever it is marked white (sure foreground), change mask=1
# wherever it is marked black (sure background), change mask=0
mask = np.zeros(img.shape[:2], np.uint8)
mask[newmask == 0] = 0
mask[newmask == 255] = 1
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

mask, bgdModel, fgdModel = cv.grabCut(img, mask, None, bgdModel, fgdModel,1, cv.GC_INIT_WITH_MASK)
mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img*mask[:, :, np.newaxis]
plt.imshow(img), plt.colorbar(), plt.show()
