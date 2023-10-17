import unittest
from logic.patronBuilder.microservice.mantenimiento_builder import MantenimientoBuilder

class TestMantenimientoBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = MantenimientoBuilder()

    def test_reset(self):
        self.builder.configRules('Rule 1')
        self.builder.reset()
        self.assertEqual(len(self.builder._mantenimiento.rules), 0)

    def test_configRules(self):
        self.builder.configRules('Rule 1')
        self.builder.configRules('Rule 2')
        self.assertEqual(len(self.builder._mantenimiento.rules), 2)
        self.assertEqual(self.builder._mantenimiento.rules[0], 'Rule 1')
        self.assertEqual(self.builder._mantenimiento.rules[1], 'Rule 2')

if __name__ == '__main__':
    unittest.main()