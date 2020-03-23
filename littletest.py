import numpy as np
import cv2

RGBout_path = './test.png'

RGBout_img = cv2.imread(RGBout_path, -1)

in_img = cv2.cvtColor(RGBout_img, cv2.COLOR_RGB2GRAY)

in_img = in_img.astype(np.float) / 255.0

RGBout_img = RGBout_img.astype(np.float) / 255.0

noise = np.random.normal(loc = 0.0, scale = 0.05, size = in_img.shape)
in_img += noise
in_img = np.clip(in_img, 0, 1)
cv2.imshow("haha",in_img)
cv2.waitKey()
cv2.destroyAllWindows()