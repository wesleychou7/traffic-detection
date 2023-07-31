import random
import math
import matplotlib.pyplot as plt


def show_random_images(source, class_names, n, seed=42):
    """Show random images in an ImageFolder

    Args:
        source (ImageFolder): image source
        class_names (list): class names corresponding to image indices
        n (int): number of images to show
        seed (int, optional): specify seed 
    """
    random.seed(seed)
    
    rand_indices = random.sample(range(0, len(source)), n)
    images = [source[i] for i in rand_indices]
    
    fig, axes = plt.subplots(nrows=math.ceil(n/5), ncols=5, figsize=(12,5))
    for i, ax in enumerate(axes.flat):
        if i < len(images):
            ax.axis("off")
            ax.imshow(images[i][0].permute(1, 2, 0))
            ax.set_title(class_names[images[i][1]])
        else:
            ax.axis("off")