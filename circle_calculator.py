#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: Feb 2022
# This is a Area and perimeter calculator for a circle with the radius of 15mm

import math


def main():
    print("If your circle radius is")
    print("15mm")
    print("")
    print("The area of your circle is {}cm².".format(math.pi * 15**2))
    print("The perimeter of your circle is {}cm".format(2 * (math.pi + 15)))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
