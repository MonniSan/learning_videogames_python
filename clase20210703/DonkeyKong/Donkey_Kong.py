from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Point3
from panda3d.core import loadPrcFileData
from math import sin, cos

loadPrcFileData('', 'win-size 800 600')
# loadPrcFileData('', 'want-directtools #t')
# loadPrcFileData('', 'want-tk #t')

class DonkeyKong(ShowBase):
    def _init_(self):
        super()._init_(self)
        self.angle = 0
        self.taskMgr.add(self.setup, "setup")
        self.taskMgr.add(self.update, "update")
        
        self.scene = self.loader.loadModel("models/DKset")
        self.scence = self.reparentTo(self.render)

        self.arcadeTexture =self.loader.loadTexture("models/dk-arcade")
        self.scene.setTexture(self.arcadeTexture)
        self.scene.setTransparency(1)

    def setup(self,task):

        return Task.done
  
            
    def update(self, task):
      self.camera.setPos(0,35,0)
      self.camera.lookAt(self.scene)

      return Task.cont  

s = DonkeyKong()
s.run()