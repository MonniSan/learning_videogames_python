from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Point3
from panda3d.core import loadPrcFileData
from math import sin, cos

loadPrcFileData(" " , "win-size 640 480")

class FirstApp(ShowBase):
  
  def __init__(self):
    super().__init__(self)
    base.messenger.toggleVerbose()
    self.taskMgr.add(self.setup, "setup")
    self.taskMgr.add(self.update,"update")
    #self.angle = 0
    self.time = 0


  def setup(self,task):
    self.square = self.loader.loadModel("models/Square")
    texture = self.loader.loadTexture("models/logo_VGA.png")
    self.square.setPos(0,0,0)
    self.square.setTransparency(1)
    self.square.setTexture(texture)
    self.square.reparentTo(self.render)
    return Task.done
  
  def update(self,task):
    self.time += 0.2
    xp = sin(self.time)*10
    yp = cos(self.time)*10
    self.camera.setPos(xp,10,0)
    self.camera.lookAt(0,0,0)
    #self.square.setHpr(self.angle,0,0)
    #self.angle += 1
    return Task.cont

t = FirstApp()
t.run()
