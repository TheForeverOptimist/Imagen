import imgaug.augmenters as iaa
import cv2
import glob


# 1.) Load Dataset
images_path = glob.glob("images/*.jpeg")
for img_path in images_path:
    img = cv2.imread(img_path)


cv2.imshow("Image", img)
cv2.waitKey(0)