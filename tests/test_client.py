from datetime import datetime

from privex.iota import PrivexIota, IOTANodeInfo
from tests.base import IOTABaseTest
from os import getenv as env
import unittest

IOTA_HOST = env('IOTA_HOST', "https://iota.se1.privex.cc")


class IOTAClientTest(IOTABaseTest):
    def setUp(self):
        self.iota = PrivexIota(adapter=IOTA_HOST)

    def test_get_node_info(self):
        info = self.iota.get_node_info()
        
        self.assertIsInstance(info, IOTANodeInfo)
        self.assertIsInstance(info.latestMilestone, str)
        self.assertIsInstance(info.time, int)
        self.assertIsInstance(info.time_date, datetime)
        
        self.assertTrue(info.isSynced, msg=f"{IOTA_HOST} isSynced is True")

