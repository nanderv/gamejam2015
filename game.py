#/usr/bin/env python

import pyglet
from json_map import Map

window = pyglet.window.Window()

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

# get the object in coords (5, 3)

@window.event
def update(dt):
    og_keys = m.objectgroups.keys()
    for key in og_keys:
        for object in m.objectgroups[key].objects:
            object["x"] += 11

    m.move_viewport(10, 0)
    window.clear()
    m.draw()

pyglet.clock.schedule_interval(update, 1 / 60.)

pyglet.app.run()