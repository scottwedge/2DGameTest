# Title: N/A
# Author: Christian A Loizou
# Date created: 31/08/2020

from cocos import layer, scene
from cocos.director import director
from cocos.text import Label

# GLOBALS
WINDOW_CAPTION = 'A promising-looking Cocos2D application - by Christian Loizou'
TITLE_TEXT = 'Main Menu'
TITLE_FONT_NAME = 'Times New Roman'
TITLE_FONT_SIZE = 32

# CLASSES

class Application(layer.Layer):
    def __init__(self):
        super().__init__()
        self.size = director.get_window_size()
        self.title_label = Label(TITLE_TEXT, font_name=TITLE_FONT_NAME, font_size=TITLE_FONT_SIZE,
            anchor_x='center', anchor_y='center')
        self.title_label.position = tuple(map(lambda p: p/2, self.size))
        self.add(self.title_label)

# METHODS

# OUT OF FRAME

if __name__ == '__main__':
    director.init(width=1280, height=720, caption=WINDOW_CAPTION)
    application = Application()
    scene = scene.Scene(application)
    director.run(scene)
