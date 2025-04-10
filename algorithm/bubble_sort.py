#!/usr/bin/env python3

import random

MAX = 10

unsorted = []
for x in range(MAX):
    random_number = random.randint(1, MAX)
    unsorted.append(random_number)

print(f"We are going to sort this list: {unsorted}")

i = 0 

while True:
    for y in range(len(unsorted) - 1):
        if unsorted[y] > unsorted[y+1]:
            unsorted[y], unsorted[y+1] = unsorted[y+1], unsorted[y]
    i += 1
    if i == len(unsorted) - 1:
        break

print(f"Here is the sorted list: {unsorted}")
         
