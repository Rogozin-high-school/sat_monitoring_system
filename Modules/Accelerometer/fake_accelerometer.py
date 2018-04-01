class fake_accelerometer:
    """Simulates an accelerometer sensor"""

    @property
    def accel(self):
        """Acceleration tuple of size 3"""
        return (0, 0, 0)
