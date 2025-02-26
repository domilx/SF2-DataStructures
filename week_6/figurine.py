"""
    we are given n unopened boxes, with k number of figurines in each box
    the boxes cannot be opened and hence, the order of the figurines that
    are in the boxes cannot be changed
    a box cannot be rotated, so the figurines are in a fixed order
    each figurine has a specified height
    eg. in a given box, the figurines are from left to right 4,5,7
    the number in each box of figurines might vary
    we want to organize the toybox s.t. they are arranged in a
    non-decreasing order of height from left to right
    howver, this may not be possible with the given boxes
    we want to write a prgram that determienes if
    we ca have such an arrangement or not
    INPUTS
    n: the number of boxes
    k: the number of figurines in each box
    k integers: the heights of the figurines in each box left to right seperated by a space
    
    eg:
    2
    3 [4 5 7]
    2 [8 8]
    this is a yes because we can arrange the figurines in the following order
    4 5 7
    8 8
    
    2
    3 [4 5 7]
    2 [6 8]
    this is a no because we cannot arrange the figurines in a non-decreasing order
    4 5 7
    6 8
"""

# TODO: read input
# TODO: check if all the boxes are OK and in order
# TODO: 

def toybox(n, k, boxes):
    for box in boxes:
        if box != sorted(box):
            return False
    return True

def main():
    n = int(input())
    for _ in range(n):
        k, *boxes = input().split()
        k = int(k)
        boxes = list(map(int, boxes))
        print(toybox(n, k, boxes))