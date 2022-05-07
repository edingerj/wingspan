"""
Players have 4 options every turn:
1) Plant a tree
2) Hug a tree
3) Gain nutrients: sun, water, fire, disturbance
4) Draw tree cards
"""

import console


def main() -> None:
    console.main()


"""
Todo: implement cli parameters:
  --help : run cli help method instead of main
  --experimental : enables experimental bonuses
  --no-sleep : disables console.sleep_enabled
"""
if __name__ == '__main__':
    main()
