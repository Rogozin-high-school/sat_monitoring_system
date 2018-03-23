class fake_accelerometer:
    """Simulates an accelerometer sensor"""

    @property
    def accel(self):
        return (0, 0, 0)
