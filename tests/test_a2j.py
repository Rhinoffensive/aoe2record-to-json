"""
Testing aoe2record-to-json core functionality.
"""
import json
import unittest

from a2j.commands import get_commands
from tests.util import execute


class test_a2j(unittest.TestCase):
    parsed = execute([
        "curl",
        "http://localhost:8080/a2j/v1/parse/" + "/".join(get_commands().keys()) + "/?record=test.mgz"
    ])

    with open("tests/data/test.json", "r") as file:
        read = json.loads(file.read())
        file.close()

    def test_completed(self):
        assert self.parsed["completed"] == self.read["completed"]

    def test_dataset(self):
        assert self.parsed["dataset"] == self.read["dataset"]

    def test_encoding(self):
        assert self.parsed["encoding"] == self.read["encoding"]

    def test_file_hash(self):
        assert self.parsed["file_hash"] == self.read["file_hash"]

    def test_hash(self):
        assert self.parsed["hash"] == self.read["hash"]

    def test_language(self):
        assert self.parsed["language"] == self.read["language"]

    def test_mirror(self):
        assert self.parsed["mirror"] == self.read["mirror"]

    def test_owner(self):
        assert self.parsed["owner"] == self.read["owner"]

    def test_platform(self):
        assert self.parsed["platform"] == self.read["platform"]

    def test_restored(self):
        assert self.parsed["restored"] == self.read["restored"]

    def test_version(self):
        assert self.parsed["version"] == self.read["version"]

    def test_chat(self):
        assert self.parsed["chat"] == self.read["chat"]

    def test_diplomacy(self):
        assert self.parsed["diplomacy"] == self.read["diplomacy"]

    def test_players(self):
        assert self.parsed["players"] == self.read["players"]

    def test_profiles(self):
        assert self.parsed["profiles"] == self.read["profiles"]

    def test_ratings(self):
        assert self.parsed["ratings"] == self.read["ratings"]

    def test_teams(self):
        assert self.parsed["teams"] == self.read["teams"]

    def test_achievements(self):
        assert self.parsed["achievements"] == self.read["achievements"]

    def test_duration(self):
        assert self.parsed["duration"] == self.read["duration"]

    def test_map(self):
        assert self.parsed["map"] == self.read["map"]

    def test_objects(self):
        assert self.parsed["objects"] == self.read["objects"]

    def test_postgame(self):
        assert self.parsed["postgame"] == self.read["postgame"]

    def test_settings(self):
        assert self.parsed["settings"] == self.read["settings"]

    def test_start_time(self):
        assert self.parsed["start_time"] == self.read["start_time"]
