from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Point3
from panda3d.core import loadPrcFileData

loadPrcFileData(" " , "win-size 640 480")

class FirstApp(ShowBase):
  
  def __init__(self):
    super().__init__(self)
    base.messenger.toggleVerbose()
    self.taskMgr.add(self.setup, "setup")
    self.taskMgr.add(self.update,"update")
  
  def setup(self,task):
    square = self.loader.loadModel("models/Square")
    square.setPos(0,0,0)
    square.reparent(self.render)
    return Task.done
  
  def update(self,task):
    self.camara.setPos(40,40,0)
    self.camara.lookAt(0,0,0)
    return Task.cont

t = FirstApp()
t.run()
