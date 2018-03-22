class fake_gyro:
    """Simulates a gyro sensor"""

    @property
    def gyro(self):
        return (0, 0, 0)
