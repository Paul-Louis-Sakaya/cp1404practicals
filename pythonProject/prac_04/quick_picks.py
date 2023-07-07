

import random

NUM_QUICK_PICKS = 5  # Number of quick picks to generate
MIN_NUM = 1  # Minimum number for each quick pick
MAX_NUM = 45  # Maximum number for each quick pick
NUM_NUMBERS_PER_LINE = 6  # Number of numbers per quick pick line

num_quick_picks = int(input("How many quick picks do you want to generate? "))

for _ in range(num_quick_picks):
    quick_pick = sorted(random.sample(range(MIN_NUM, MAX_NUM + 1), NUM_NUMBERS_PER_LINE))
    print(" ".join("{:2d}".format(num) for num in quick_pick))