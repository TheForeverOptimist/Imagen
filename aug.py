import imgaug.augmenters as iaa
import cv2
import glob


# 1.) Load Dataset
images = []
images_path = glob.glob("images/*.jpeg")
for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img)

#2.) Image Augmentation

augmentation = iaa.Sequential([
    #1. Rotate
    # iaa.Rotate((-30, 30))
    #2. Flip
    iaa.Fliplr(1)
])

augmentated_images = augmentation(images=images)

#3.) show images
for img in augmentated_images:
    cv2.imshow("Image", img)
    cv2.waitKey(0)