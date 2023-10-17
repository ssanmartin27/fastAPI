import unittest
from logic.patronBuilder.microservice.horario_builder import HorarioBuilder, Horario, Ruta

class TestHorarioBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = HorarioBuilder()

    def test_reset(self):
        self.builder.configRules('Rule 1')
        self.builder.configSchedules('Schedule 1')
        self.builder.configRoutes(Ruta())
        self.builder.reset()
        self.assertEqual(len(self.builder._horario.rules), 0)
        self.assertEqual(len(self.builder._horario.Schedules), 0)
        self.assertEqual(len(self.builder._horario.ruta), 0)

    def test_configRules(self):
        self.builder.configRules('Rule 1')
        self.builder.configRules('Rule 2')
        self.assertEqual(len(self.builder._horario.rules), 2)
        self.assertEqual(self.builder._horario.rules[0], 'Rule 1')
        self.assertEqual(self.builder._horario.rules[1], 'Rule 2')

    def test_configSchedules(self):
        self.builder.configSchedules('Schedule 1')
        self.builder.configSchedules('Schedule 2')
        self.assertEqual(len(self.builder._horario.Schedules), 2)
        self.assertEqual(self.builder._horario.Schedules[0], 'Schedule 1')
        self.assertEqual(self.builder._horario.Schedules[1], 'Schedule 2')

    def test_configRoutes(self):
        ruta = Ruta()
        self.builder.configRoutes(ruta)
        self.assertEqual(len(self.builder._horario.ruta), 1)
        self.assertEqual(self.builder._horario.ruta[0], ruta)

if __name__ == '__main__':
    unittest.main()