"""核对原始业务资料之间的引用与记录形式。"""

import unittest

from inspect_samples import read_samples


class SampleTests(unittest.TestCase):
    def setUp(self):
        self.data = read_samples()

    def test_running_day_links(self):
        scheduled = {(row['day'], row['trip']): row for row in self.data['schedules']}
        for fact in self.data['facts']:
            trip = scheduled[fact['day'], fact['trip']]
            if 'stop' in fact:
                self.assertIn(fact['stop'], trip['stops'])
        self.assertGreater(max(trip['start'] for trip in scheduled.values()), 1440)

    def test_revised_position_has_prior_interval(self):
        intervals = {(fact['day'], fact['trip'], fact['stop']): fact for fact in self.data['facts'] if fact['kind'] == '定位待核'}
        revised = [fact for fact in self.data['facts'] if fact['kind'] == '更正定位']
        self.assertTrue(revised)
        for row in revised:
            earlier = intervals[row['day'], row['trip'], row['stop']]
            self.assertLess(earlier['received'], row['received'])
            self.assertLessEqual(earlier['earliest'], row['arrived'])
            self.assertLessEqual(row['arrived'], earlier['latest'])
