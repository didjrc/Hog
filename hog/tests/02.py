test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> take_turn(2, 0, make_test_dice(4, 6, 1))
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(3, 0, make_test_dice(4, 6, 1))
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 35)
          327b19ffebddf93982e1ad2a4a6486f4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> take_turn(0, 71)
          2aef307e1e3d3bb468f74013a49eb977
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> take_turn(0, 7)
          2aef307e1e3d3bb468f74013a49eb977
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> take_turn(0, 0)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> take_turn(2, 0, make_test_dice(6))
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(1, 0, make_test_dice(3))
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> take_turn(2, 0, make_test_dice(2, 3, 5))
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> take_turn(0, 60)
          11
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> hog.take_turn(5, 0) # Make sure you call roll_dice!
          9002
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import hog
      >>> def roll_dice(num_rolls, dice):
      ...     return 9002
      ...
      >>> hog.roll_dice, old_roll_dice = roll_dice, hog.roll_dice
      """,
      'teardown': r"""
      >>> hog.roll_dice = old_roll_dice
      """,
      'type': 'doctest'
    }
  ]
}