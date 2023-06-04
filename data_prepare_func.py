import cv2
import os
import numpy as np

def convert_to_array(data_path,size):
    folders = ['0','1','2','3','4','5','6','7','8','9']
    X, y = [], []
    kernel = np.ones((5, 5), np.uint8)
    for folder in folders:
        folder_path = os.path.join(data_path, folder)
        images = os.listdir(folder_path)
        for image_name in images:
            image_path = os.path.join(folder_path, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.dilate(image, kernel, iterations=1)
            image = cv2.resize(image, (size, size))  # Resize the image to 28x28 pixels
            X.append(image.flatten())  # Flatten the image and add it to the feature matrix
            y.append(int(folder))  # Add the corresponding label

    X_data = np.array(X)
    y_data = np.array(y)
    return X_data,y_data


# data = pickle.load(open("thainumber_{}.pkl".format(size), "rb"))
# X = data['X']
# Y = data['Y']