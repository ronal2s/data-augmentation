import matplotlib.pyplot as plt
import os


def show_image(original_image, augmented_image, title):
    fig = plt.figure()
    fig.suptitle(title)

    original_plt = fig.add_subplot(1, 2, 1)

    original_plt.set_title('original image')
    original_plt.imshow(original_image)

    augmented_plt = fig.add_subplot(1, 2, 2)
    augmented_plt.set_title('augmented image')
    augmented_plt.imshow(augmented_image)
    plt.show(block=True)


def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
