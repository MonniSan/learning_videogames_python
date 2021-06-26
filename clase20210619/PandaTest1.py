from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Point3
from panda3d.core import loadPrcFileData

loadPrcFileData(" " , "win-size 800 600")

class FirstApp(ShowBase):
  def __init__(self):
    super().__init__(self)

t = FirstApp()
t.run()
