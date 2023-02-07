import unittest
import egg_dropper as ed


class MyTestCase(unittest.TestCase):
    """
    Test case for egg_dropper
    """

    """
    Test
    1 egg
    10 floors
    """

    def test_one_egg(self):
        floors = 10
        eggs = 1
        self.assertEqual(0, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=-10))
        self.assertEqual(0, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=1))
        self.assertEqual(1, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=2))
        self.assertEqual(4, ed.egg_dropper(floors=10,
                                           eggs=1,
                                           breaks_at_floor=5))
        self.assertEqual(9, ed.egg_dropper(floors=10,
                                           eggs=1,
                                           breaks_at_floor=10))
        self.assertEqual(10, ed.egg_dropper(floors=10,
                                            eggs=1,
                                            breaks_at_floor=11))
        self.assertEqual(10, ed.egg_dropper(floors=10,
                                            eggs=1,
                                            breaks_at_floor=20))

    """
    Test
    2 egg
    10 floors
    """

    def test_two_eggs(self):
        eggs = 2
        floors = 100
        self.assertEqual(0, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=-100))
        self.assertEqual(0, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=0))
        self.assertEqual(1, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=2))
        self.assertEqual(49, ed.egg_dropper(floors=floors,
                                            eggs=eggs,
                                            breaks_at_floor=50))
        self.assertEqual(99, ed.egg_dropper(floors=floors,
                                            eggs=eggs,
                                            breaks_at_floor=100))
        self.assertEqual(100, ed.egg_dropper(floors=floors,
                                             eggs=eggs,
                                             breaks_at_floor=101))
        self.assertEqual(100, ed.egg_dropper(floors=floors,
                                             eggs=eggs,
                                             breaks_at_floor=200))

    """
    Test binary search
    """
    def test_x_eggs(self, floors = 10, eggs = 10):
        self.assertEqual(0, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=-100))
        self.assertEqual(0, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=0))
        self.assertEqual(1, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=2))
        self.assertEqual(4, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=5))
        self.assertEqual(9, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=10))
        self.assertEqual(10, ed.egg_dropper(floors=floors,
                                            eggs=eggs,
                                            breaks_at_floor=11))
        self.assertEqual(10, ed.egg_dropper(floors=floors,
                                            eggs=eggs,
                                            breaks_at_floor=20))

    """
    Test binary search
    """
    def test_all_methods(self, floors = 100, eggs = 3):
        self.assertEqual(0, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=-100))
        self.assertEqual(0, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=0))
        self.assertEqual(1, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=2))
        self.assertEqual(55, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=56))
        self.assertEqual(99, ed.egg_dropper(floors=floors,
                                           eggs=eggs,
                                           breaks_at_floor=100))
        self.assertEqual(100, ed.egg_dropper(floors=floors,
                                            eggs=eggs,
                                            breaks_at_floor=101))
        self.assertEqual(100, ed.egg_dropper(floors=floors,
                                            eggs=eggs,
                                            breaks_at_floor=200))


if __name__ == '__main__':
    unittest.main()
