#/usr/bin/env python

import pyglet
import sys

sys.path.insert(0, '../pyglet-tiled-json-map')
from json_map import Map
import pprint
window = pyglet.window.Window()
window.set_vsync(0)
# load the map
fd = pyglet.resource.file("test.json", 'rt')
m = Map.load_json(fd)

# set the viewport to the window dimensions
m.set_viewport(0, 0, window.width, window.height)

# perform some queries to the map data!
print (m.objectgroups.keys())
# list all the objects
print("listing all the objects:")
for obj in m.objectgroups["object"]:
    print(obj)


# get the object named "Door1"
keyboardhandler = pyglet.window.key.KeyStateHandler()
window.push_handlers(keyboardhandler)
# get the object in coords (5, 3)
@window.event
def update(dt):
    og_keys = m.objectgroups.keys()
    for key in og_keys:
        for object in m.objectgroups[key].objects:
            d_x = 0
            d_y = 0
            if keyboardhandler[pyglet.window.key.D]:
                d_x += 10
            if keyboardhandler[pyglet.window.key.A]:
                d_x += -10
            if keyboardhandler[pyglet.window.key.S]:
                d_y += 10
            if keyboardhandler[pyglet.window.key.W]:
                d_y += -10
            m.objectgroups[key].move(object,d_x,d_y)
            object["rotation"] += 1
    window.clear()
    m.invalidate()
    m.move_focus(1,0)
    m.draw()
pp = pprint.PrettyPrinter()
pp.pprint(m.tilelayers["collision"].sprites.keys())
print(m.tilelayers["collision"][10, 10])
pyglet.clock.schedule_interval(update,1.0/60.0)
pyglet.clock.set_fps_limit(60)
pyglet.app.run()