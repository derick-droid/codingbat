"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks
(5 inches each). Return True if it is possible to make the goal by choosing from the given bricks.
This is a little harder than it looks and can be done without any loops.

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
"""


def make_bricks(small, big, goal):
    large_brick = goal / 5  # use as many number of large bricks as possible
    if large_brick > big:
        large_brick = big
    new_goal = goal - (large_brick * 5)
    if new_goal <= small:
        return True
    else:
        return False
        
