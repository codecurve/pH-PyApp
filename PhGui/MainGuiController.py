from MvcModel.MathModelController import MathModelController


class MainGuiController(object):
    '''
    Gui logic for main UI of pH app
    '''


    def __init__(self, mainWindowFrame):
      self.mathModelController = MathModelController()
      self.mainWindowFrame = mainWindowFrame

      
    def simulateButtonPushed(self):
      self.mathModelController.solve()
      self.mainWindowFrame.plot1(self.mathModelController.voiHistory, self.mathModelController.statesHistory, self.mathModelController.algebraicsHistory)
       

    def co2sinkValueChanged(self, value):
      co2sinkSliderScaleFactor = 0.01
      self.mathModelController.setCo2sinkValue(value * co2sinkSliderScaleFactor)
