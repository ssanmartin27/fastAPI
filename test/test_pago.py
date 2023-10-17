import unittest
from logic.patronBuilder.microservice.pago_builder import PagoBuilder

class TestPagoBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = PagoBuilder()

    def test_reset(self):
        self.builder.configRules('Rule 1')
        self.builder.reset()
        self.assertEqual(len(self.builder._Pago.rules), 0)

    def test_configRules(self):
        self.builder.configRules('Rule 1')
        self.builder.configRules('Rule 2')
        self.assertEqual(len(self.builder._Pago.rules), 2)
        self.assertEqual(self.builder._Pago.rules[0], 'Rule 1')
        self.assertEqual(self.builder._Pago.rules[1], 'Rule 2')

if __name__ == '__main__':
    unittest.main()