#!/usr/bin/python3

from ezpycolor import *

#=============

printgreen("hello world")

s = colorpurple("hello")+" "+colorred("world")
print(s)

printbold("hello world")
printunderline("hello world")

printrainbow("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
printbgrainbow("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

t = colorrainbow("hello")+" "+colorbgrainbow("world")
print(t)

b = colorbold("hello world")
print(b)

u = colorunderline("hello world")
print(u)
