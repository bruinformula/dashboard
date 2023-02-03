from gui.dials.AnalogGaugeWidget import AnalogGaugeWidget
from PyQt5.QtGui import QColor


class AFRDial(AnalogGaugeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setCustomGaugeTheme(
            color1="#242321",  # gray, end color, outer color
            color2="#5e5e5e",  # a lighter gray, just a shine
            color3="#000000"  # black, start color, center color
        )
        super().setNeedleColor(139, 225, 242, 255)
        super().setScaleValueColor(139, 225, 242, 255)
        super().setBigScaleColor(QColor(139, 225, 242, 255))
        super().setFineScaleColor(QColor(139, 225, 242, 255))
        super().setDisplayValueColor(206, 244, 255, 255)
        super().setMinValue(0)
        super().setMaxValue(28)
        super().setScalaCount(7)
        super().setScaleStartAngle(245)
        super().setTotalScaleAngleSize(150)
        super().setEnableValueText(True)
        super().setEnableCenterPoint(True)
        self.units = ""
        self.initial_scale_fontsize = 25
        self.initial_value_fontsize = 52
