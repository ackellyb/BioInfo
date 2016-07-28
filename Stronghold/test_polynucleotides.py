import pytest
from rosalind_library import _PolyNucleotides
from rosalind_library import DNA
from rosalind_library import RNA

class TestDNA:
    def test_create_string_mixed_case_no_format(self):
        pn = _PolyNucleotides('aCGta')
        assert pn.string == 'ACGTA'

    def test_polynucleotides_equal_success(self):
        pn1 = _PolyNucleotides('ACG')
        pn2 = _PolyNucleotides('ACG')
        assert pn1 == pn2

    def test_polynucleotides_not_equal_success(self):
        pn1 = _PolyNucleotides('ACG')
        pn2 = _PolyNucleotides('ACGT')
        assert pn1 != pn2

    def test_polynucleotides_different_type(self):
        dna = DNA("ACG")
        rna = RNA("ACG")
        assert dna != rna

    def test_find_substring_locations_no_substring(self):
        expected = list()
        pn1 = _PolyNucleotides('ACG')
        pn2 = _PolyNucleotides('TC')
        result = pn1.find_substring_locations(pn2)
        assert expected == result

    def test_find_substring_locations_matching_substring_larger(self):
        expected = list()
        pn1 = _PolyNucleotides('TC')
        pn2 = _PolyNucleotides('ACG')
        result = pn1.find_substring_locations(pn2)
        assert expected == result

    def test_find_substring_locations_success(self):
        expected = [2, 4, 10]
        pn1 = _PolyNucleotides('GATATATGCATATACTT')
        pn2 = _PolyNucleotides('ATAT')
        result = pn1.find_substring_locations(pn2)
        assert expected == result
