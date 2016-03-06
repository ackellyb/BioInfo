import pytest
import os
import simple_files
import tempfile
import simple_loops
import simple_squares
import string_splicing
class TestVillage:
    def test_simple_files(self):
        with tempfile.NamedTemporaryFile(mode="r+") as temp:
            expected = """Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat"""
            temp.write("""Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat""")
            temp.flush()
            result = "".join(simple_files.remove_odd_lines(temp.name))
            assert expected == result

    def test_simple_squares(self):
        expected = 34
        a = 3
        b = 5
        result = simple_squares.add_squares(a, b)
        assert expected == result

    def test_string_splicing(self):
        expected = "Humpty Dumpty"
        s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
        a = 22
        b = 27
        c = 97
        d = 102
        result = string_splicing.splice(s, a, b, c, d)
        assert expected == result

    def test_simple_loops(self):
        expected = 7500
        a = 100
        b = 200
        result = simple_loops.sum_odd_integers(a, b)
        assert expected == result
