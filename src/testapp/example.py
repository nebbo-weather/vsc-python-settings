from typing import Dict

from testapp.auxiliary import Client


class InnerLongClass:
    def __init__(self):
        self.client = Client()
        self.really_long_dict: Dict[str, int] = {
            "really_long_long_key": 1,
            "short_key": 2,
        }
