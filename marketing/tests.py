from django.test import TestCase

from .spot_times import guess_vehicle
from .models import Vehicle, SpotTime


class TestSpotTime(TestCase):
    def setUp(self):
        self.tv23 = Vehicle.objects.create(name='TV-23')
        self.tv51 = Vehicle.objects.create(name='TV-51')
        self.fm92 = Vehicle.objects.create(name='FM-92.3')

    def test_guess_vehicle(self):
        # test vehicle is None if no spot times
        self.assertIsNone(guess_vehicle())

        first_spot = SpotTime.objects.create(air_time='2015-04-20 10:00', vehicle=self.tv23)
        second_spot = SpotTime.objects.create(air_time='2015-04-20 12:00', vehicle=self.tv51)
        third_spot = SpotTime.objects.create(air_time='2015-04-20 13:00', vehicle=self.fm92)
        # when air time is equal to now it works
        self.assertEquals(guess_vehicle('2015-04-20 10:00'), self.tv23)
        # it gets the first greater than now
        self.assertEquals(guess_vehicle('2015-04-20 10:20'), self.tv23)

        self.assertEquals(guess_vehicle('2015-04-20 12:20'), self.tv51)

        self.assertEquals(guess_vehicle('2015-04-20 12:59'), self.tv51)

        self.assertEquals(guess_vehicle('2015-04-20 13:01'), self.fm92)