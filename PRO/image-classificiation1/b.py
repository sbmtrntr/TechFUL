import numpy as np
import cv2

train_label = np.loadtxt('train.csv', delimiter=',', dtype='uint8', skiprows=1,usecols=[0])
train_data = np.loadtxt('train.csv', delimiter=',', dtype='uint8', skiprows=1)[:,1:]

print(train_label)
print(train_data)
print(train_label.shape)
print(train_data.shape)

# img_chimpanzee_sample = train_data[0].reshape(32,32,3)
# img_monkey_sample = train_data[30].reshape(32,32,3)

# cv2.imshow("chimpanzee",img_chimpanzee_sample)
# cv2.imshow("monkey",img_monkey_sample)
# cv2.waitKey(0)
# cv2.destroyAllWindows()