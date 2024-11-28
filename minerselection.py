#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 00:18:49 2024

@author: sauravdas
"""
import random

class Home:
    def __init__(self, el, rl):
        self.el = el
        self.rl = rl

class Building:
    def __init__(self, el, rl):
        self.el = el
        self.rl = rl

class Industry:
    def __init__(self, el, rl):
        self.el = el
        self.rl = rl

class EV:
    def __init__(self, el, rl, tos):
        self.el = el
        self.rl = rl
        self.tos = tos

def main():
    g = 5
    k = 10

    hn = int(input("Number of Home: "))
    homes = [Home(random.randint(1, 10), random.randint(1, 10)) for _ in range(hn)]

    bn = int(input("Number of Building: "))
    buildings = [Building(random.randint(1, 10), random.randint(1, 10)) for _ in range(bn)]

    in_ = int(input("Number of Industry: "))
    industries = [Industry(random.randint(1, 10), random.randint(1, 10)) for _ in range(in_)]

    en = int(input("Number of EVs: "))
    evs = [EV(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)) for _ in range(en)]

    lst = []

    th1, th2 = map(int, input("Enter Home thresholds: ").split())
    for i, home in enumerate(homes, start=1):
        if home.el >= th1 and home.rl >= th2:
            lst.append((1, i))

    th1, th2 = map(int, input("Enter Building thresholds: ").split())
    for i, building in enumerate(buildings, start=1):
        if building.el >= th1 and building.rl >= th2:
            lst.append((2, i))

    th1, th2 = map(int, input("Enter Industry thresholds: ").split())
    for i, industry in enumerate(industries, start=1):
        if industry.el >= th1 and industry.rl >= th2:
            lst.append((3, i))

    th1, th2, th3 = map(int, input("Enter EV thresholds: ").split())
    for i, ev in enumerate(evs, start=1):
        if ev.el >= th1 and ev.rl >= th2 and ev.tos >= th3:
            lst.append((4, i))

    val = -1
    ans = None

    print("Miner Nodes: ")
    for item in lst:
        print(item[0], item[1])

    for x in lst:
        category, idx = x
        if category == 1:
            el = homes[idx - 1].el
            rl = homes[idx - 1].rl
        elif category == 2:
            el = buildings[idx - 1].el
            rl = buildings[idx - 1].rl
        elif category == 3:
            el = industries[idx - 1].el
            rl = industries[idx - 1].rl
        else:
            el = evs[idx - 1].el
            rl = evs[idx - 1].rl

        score = el * g + rl * k
        if score > val:
            val = score
            ans = (category, idx)

    print("Leader Node:")
    print(ans[0], ans[1])

if __name__ == "__main__":
    main()
