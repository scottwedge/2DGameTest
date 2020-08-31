from cocos import layer, scene
from cocos.director import director
from cocos.text import Label


class Application(layer.Layer):
    def __init__(self, width, height, /):
        super().__init__()
        self.title_label = Label('Main Menu', font_name='Times New Roman', font_size=32, anchor_x='center', anchor_y='center')
        self.title_label.position = (width/2, height/2)
        self.add(self.title_label)

if __name__ == '__main__':
    director.init(width=1280, height=720, caption='Hello, World!')
    application = Application(1280, 720,)
    scene = scene.Scene(application)
    director.run(scene)
