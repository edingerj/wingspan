"""
Players have 4 options every turn:
1) Plant a tree
2) Hug a tree
3) Gain nutrients: sun, water, fire, disturbance
4) Draw tree cards
"""
from sys import argv
from typing import List

from gameplay import console


def main(arguments: List[str]) -> None:
    console.main(arguments)


"""
Todo: implement --help : run cli help method instead of main
"""
if __name__ == '__main__':
    main(argv[1:])
