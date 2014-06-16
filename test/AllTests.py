import sys
sys.path.insert(1, "..")

from ADCCalibrateTest import ADCCalibrateTest
from ADCConfFileTest import ADCConfFileTest
from SPITest import SPITest
from GPIBTest import GPIBTest
from OGPTest import OGPTest
from INLTest import INLTest
from MMCMTest import MMCMTest
from ADCCalibrationsTest import ADCCalibrationsTest
import unittest

if __name__ == "__main__":
    unittest.main()

