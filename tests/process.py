"""Test process
"""

import os
import unittest
import sys

pywpsPath = os.path.abspath(
    os.path.join(
        os.path.split(os.path.abspath(__file__))[0],
        ".."
    )
)
sys.path.insert(0, pywpsPath)
sys.path.append(pywpsPath)

from pywps import Process
from pywps.inout import LiteralInput
from pywps.inout import BoundingBoxInput
from pywps.inout import ComplexInput


class ProcessTestCase(unittest.TestCase):

    def test_get_input_title(self):
        """Test returning the proper input title"""

        # configure
        def donothing(*args, **kwargs):
            pass
        process = Process(donothing, "process",
                          title="Process",
                          inputs=[
                              LiteralInput("length", title="Length"),
                              BoundingBoxInput("bbox", title="BBox", crss=[]),
                              ComplexInput("vector", title="Vector")
                          ],
                          outputs=[])
        inputs = {
            input.identifier: input.title
            for input
            in process.inputs
        }
        self.assertEquals("Length", inputs['length'])
        self.assertEquals("BBox", inputs["bbox"])
        self.assertEquals("Vector", inputs["vector"])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ProcessTestCase)
    unittest.TextTestRunner(verbosity=4).run(suite)
