
from mvcmodel.mathmodelcontroller import MathModelController


co2SinkSliderScaleFactor = 0.0002
co2SourceSliderScaleFactor = 0.0002
protonSourceSliderScaleFactor = 0.0002

co2SinkResetValue = 0 
co2SourceResetValue = 0 
protonSourceResetValue = 0


class MainGuiController(object):
    '''
    Gui logic for main UI of pH app
    '''


    def __init__(self, mainWindowFrame):
        self.mathModelController = MathModelController()
        self.mainWindowFrame = mainWindowFrame
        self.running = False

      
    def playPauseButtonPushed(self):
        self.running = not self.running
        self.mainWindowFrame.playPauseLabelToggle(self.running)

      
    def resetButtonPushed(self):
        self.mathModelController.reset()
        self.mainWindowFrame.reset(co2SinkResetValue, co2SourceResetValue, protonSourceResetValue)
       

    def co2SinkValueChanged(self, value):
        self.mathModelController.setCo2SinkValue(value * co2SinkSliderScaleFactor)
        self.mainWindowFrame.setCo2SinkValue(value * co2SinkSliderScaleFactor)


    def co2SourceValueChanged(self, value):
        self.mathModelController.setCo2SourceValue(value * co2SourceSliderScaleFactor)
        self.mainWindowFrame.setCo2SourceValue(value * co2SourceSliderScaleFactor)
       

    def protonSourceValueChanged(self, value):
        self.mathModelController.setProtonSourceValue(value * protonSourceSliderScaleFactor)
        self.mainWindowFrame.setProtonSourceValue(value * protonSourceSliderScaleFactor)

      
    def timerEvent(self):
        if (self.running):
            self.mathModelController.solve()
            self.mainWindowFrame.plot1(self.mathModelController.voiHistory, self.mathModelController.statesHistory, self.mathModelController.algebraicsHistory)
      
