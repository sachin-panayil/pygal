#!/usr/bin/env python
from pygal import (
    Line, Bar, XY, Pie, StackedBar, Config,
    HorizontalBar, HorizontalStackedBar)
from pygal.style import NeonStyle
from math import cos, sin

bar = Bar()
rng = [-6, -19, 0, -1, 2]
bar.add('test1', rng)
bar.add('test2', map(abs, rng))
bar.x_labels = map(str, rng)
bar.title = "Bar test"
with open('out-bar.svg', 'w') as f:
    f.write(bar.render())

hbar = HorizontalBar()
rng = [18, 9, 7, 3, 1, 0, -5]
hbar.add('test1', rng)
rng2 = [16, 14, 10, 9, 7, 3, -1]
hbar.add('test2', rng2)
hbar.x_labels = map(
    lambda x: '%s / %s' % x, zip(map(str, rng), map(str, rng2)))
hbar.title = "Horizontal Bar test"
with open('out-horizontalbar.svg', 'w') as f:
    f.write(hbar.render())


rng = [3, -32, 39, 12]
rng2 = [24, -8, 18, 12]
rng3 = [6, 1, -10, 0]
config = Config()
config.x_label_rotation = 35
config.x_labels = map(lambda x: '%s  / %s / %s' % x,
                        zip(map(str, rng),
                            map(str, rng2),
                            map(str, rng3)))
config.title = "Stacked Bar test"
config.style = NeonStyle
config.horizontal = True

stackedbar = StackedBar(config)
stackedbar.add('@@@@@@@', rng)
stackedbar.add('++++++', rng2)
stackedbar.add('--->', rng3)
with open('out-stackedbar.svg', 'w') as f:
    f.write(stackedbar.render())

config.title = "Horizontal Stacked Bar test"
hstackedbar = HorizontalStackedBar(config)
hstackedbar.add('@@@@@@@', rng)
hstackedbar.add('++++++', rng2)
hstackedbar.add('--->', rng3)
with open('out-horizontalstackedbar.svg', 'w') as f:
    f.write(hstackedbar.render())

line = Line(Config(y_scale=.0005))
rng = range(-30, 31, 5)
line.add('test1', [cos(x / 10.) for x in rng])
line.add('test2', [sin(x / 10.) for x in rng])
line.add('test3', [cos(x / 10.) - sin(x / 10.) for x in rng])
line.x_labels = map(str, rng)
line.title = "Line test"
with open('out-line.svg', 'w') as f:
    f.write(line.render())

xy = XY(Config(x_scale=1))
xy.add('test1', [(1981, 1), (2004, 2), (2003, 10), (2012, 8), (1999, -4)])
xy.add('test2', [(1988, -1), (1986, 12), (2007, 7), (2010, 4), (1999, 2)])
xy.title = "XY test"
with open('out-xy.svg', 'w') as f:
    f.write(xy.render())

pie = Pie()
pie.add('test', 121)
pie.add('test2', 29)
# pie.add('test3', 242)
# pie.add('test4', 90)
# pie.add('test5', 175)
pie.title = "Pie test"
with open('out-pie.svg', 'w') as f:
    f.write(pie.render())