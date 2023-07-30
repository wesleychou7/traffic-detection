import random
import math
import matplotlib.pyplot as plt

label_map = {
    0: '20_speed',
    1: '30_speed',
    2: '50_speed',
    3: '60_speed',
    4: '70_speed',
    5: '80_speed',
    6: '80_lifted',
    7: '100_speed',
    8: '120_speed',
    9: 'no_overtaking_general',
    10: 'no_overtaking_trucks',
    11: 'right_of_way_crossing',
    12: 'right_of_way_general',
    13: 'give_way',
    14: 'stop',
    15: 'no_way_general',
    16: 'no_way_trucks',
    17: 'no_way_one_way',
    18: 'attention_general',
    19: 'attention_left_turn',
    20: 'attention_right_turn',
    21: 'attention_curvy',
    22: 'attention_bumpers',
    23: 'attention_slippery',
    24: 'attention_bottleneck',
    25: 'attention_construction',
    26: 'attention_traffic_light',
    27: 'attention_pedestrian',
    28: 'attention_children',
    29: 'attention_bikes',
    30: 'attention_snowflake',
    31: 'attention_deer',
    32: 'lifted_general',
    33: 'turn_right',
    34: 'turn_left',
    35: 'turn_straight',
    36: 'turn_straight_right',
    37: 'turn_straight_left',
    38: 'turn_right_down',
    39: 'turn_left_down',
    40: 'turn_circle',
    41: 'lifted_no_overtaking_general',
    42: 'lifted_no_overtaking_trucks'
}

def show_random_images(source, n, seed=42):
    """Show random images in an ImageFolder

    Args:
        source (ImageFolder): image source
        n (int): number of images to show
        seed (int, optional): specify seed 
    """
    random.seed(seed)
    
    rand_indices = random.sample(range(0, len(source)), n)
    images = [source[i] for i in rand_indices]
    
    fig, axes = plt.subplots(nrows=math.ceil(n/5), ncols=5, figsize=(10,4))
    for i, ax in enumerate(axes.flat):
        if i < len(images):
            ax.axis("off")
            ax.imshow(images[i][0].permute(1, 2, 0))
            ax.set_title(label_map[images[i][1]])
        else:
            ax.axis("off")
    
    # for index in rand_indices:
    #     plt.imshow(source[index][0].permute(1, 2, 0))
    #     plt.title(label_map[source[index][1]], fontsize=10)
    #     plt.axis("off")