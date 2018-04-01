class fake_gyro:
    """Simulates a gyro sensor"""

    @property
    def gyro(self):
        """Angular velocity tuple of size 3"""
        return (0, 0, 0)
