# Regular Ball Super Ball
# Create a class Ball.

# Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type  #=> "regular"
# ball2.ball_type  #=> "super"
from asserts.Asserts import assert_true


class Ball(object):
    def __init__(self, value='regular'):
        self.ball_type = value


assert_true(Ball().ball_type, "regular")
assert_true(Ball("super").ball_type, "super")
