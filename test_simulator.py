import unittest
from simulator import Simulator
from lessons import LESSONS
class SimulatorTests(unittest.TestCase):
    def test_lessons(self):
        for title, _, example, _, answers in LESSONS:
            with self.subTest(title=title):
                self.assertIn(example, answers.split('|'))
                for command in answers.split('|'):
                    self.assertTrue(Simulator().run(command)[1])
    def test_virtual_files(self):
        s=Simulator()
        for command in ['mkdir Labor','cd Labor','touch test','cp test kopie','rm test']:
            self.assertTrue(s.run(command)[1])
        self.assertEqual(s.run('ls')[0], 'kopie')
    def test_unsupported(self):
        for command in ['sudo reboot','rm -rf /','bash','curl example.org','ls; reboot']:
            self.assertFalse(Simulator().run(command)[1])
if __name__=='__main__': unittest.main()

class EnglishTests(unittest.TestCase):
    def test_english_lessons(self):
        from lessons import LESSONS_EN
        self.assertEqual(len(LESSONS_EN), len(LESSONS))
        for lesson in LESSONS_EN:
            for command in lesson[4].split('|'):
                self.assertTrue(Simulator('en').run(command)[1], command)
