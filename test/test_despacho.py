import unittest
from logic.patronBuilder.microservice.despacho_builder import DespachoBuilder

class TestDespachoBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = DespachoBuilder()

    def test_reset(self):
        self.builder.configRules('Rule 1')
        self.builder.configSchedules('Schedule 1')
        self.builder.reset()
        self.assertEqual(len(self.builder._despacho.rules), 0)
        self.assertEqual(len(self.builder._despacho.schedules), 0)

    def test_configRules(self):
        self.builder.configRules('Rule 1')
        self.builder.configRules('Rule 2')
        self.assertEqual(len(self.builder._despacho.rules), 2)
        self.assertEqual(self.builder._despacho.rules[0], 'Rule 1')
        self.assertEqual(self.builder._despacho.rules[1], 'Rule 2')

    def test_configSchedules(self):
        self.builder.configSchedules('Schedule 1')
        self.builder.configSchedules('Schedule 2')
        self.assertEqual(len(self.builder._despacho.schedules), 2)
        self.assertEqual(self.builder._despacho.schedules[0], 'Schedule 1')
        self.assertEqual(self.builder._despacho.schedules[1], 'Schedule 2')

if __name__ == '__main__':
    unittest.main()