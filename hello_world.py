import cocos

class Application(cocos.layer.Layer):
    def __init__(self, /, title = 'Cocos Application'):
        super(Application, self).__init__()
        self.title = title
        label = cocos.text.Label(self.title, font_size = 32, anchor_x='center', anchor_y='top')
        label.position = (320, 240)
        self.add(label)

def runApplication():
    cocos.director.director.init()
    app_layer = Application()

    main_scene = cocos.scene.Scene(app_layer)
    cocos.director.director.run(main_scene)

if __name__ == '__main__':
    runApplication()
