# -*- encoding: utf-8 -*-

# Author: Savenko Mike
import json
import logging
import os

from datetime import datetime, timedelta


class Instance:
    def __init__(self, name=""):
        self.__stats = {}
        self.__name = name
        stats_path = os.path.join(os.getcwd(), 'Stats')
        if not os.path.exists(stats_path):
            os.makedirs(stats_path)

    @property
    def stats(self):
        if not self.__stats:
            path = os.path.join(os.getcwd(), 'Stats', self.__name, '.txt')
            with open(path, 'r') as stat:
                self.__stats = json.load(stat)
        return self.__stats

    @stats.setter
    def stats(self, value):
        if self.__stats != value:
            self.__stats = value
            path = os.path.join(os.getcwd(), 'Stats', self.__name, '.txt')
            with open(path, 'w') as stat:
                self.__stats = json.dump(stat)

    def set_stat(self, name, value, updated, duration, fault_detection,
                 change_detection):
        path = os.path.join(os.getcwd(), 'Stats', name, '.txt')
        smallest_value = 1e-20

        try:
            tolerance_min = value
            tolerance_max = value

            if fault_detection:
                tolerance_min = self.stats.get('Week') * (
                        1 - min(max(self.stats.get('Week_Fluctuation') * 2, .1),
                                .9))
                tolerance_max = self.stats.get('Week') * (
                        1 + min(max(self.stats.get('Week_Fluctuation') * 2, .1),
                                .9))

            if change_detection and value == self.stats.get('Live'):
                updated = self.stats.get('Updated', datetime.now())
            else:
                updated = datetime.now()

            if value < tolerance_min or value > tolerance_max:
                logging.warning(
                    "Stat file (%s) was not updated because the value (%s) is "
                    "outside fault tolerance (%s ... %s). " %
                    (name, value, tolerance_min, tolerance_max))
            else:
                isinstance(duration, timedelta)
                Span_Minute = min(duration.seconds * 60 / min(self.stats.get("Duration").get("TotalMinutes"), 1), 1)
                Span_Minute_5 = min((duration.seconds * 60 / 5) / min((self.stats.get("Duration").get("TotalMinutes") / 5), 1), 1)
                Span_Minute_10 = min((duration.seconds * 60 / 10) / min((self.stats.get("Duration").get("TotalMinutes") / 10), 1), 1)
                Span_Hour = min(duration.seconds * 3600 / min(self.stats.get("Duration").get("TotalHours"), 1), 1)
                Span_Day = min(duration.days / min(self.stats.get("Duration").get("TotalDays"), 1), 1)
                Span_Week = min((duration.days / 7) / min((self.stats.get("Duration").get("TotalDays") / 7), 1), 1)
        except Exception as e:
            logging.error(str(e))
