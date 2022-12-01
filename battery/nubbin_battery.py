from abc import ABC
from datetime import datetime

from car import Car


class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = datetime.today().date()

    def battery_should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False