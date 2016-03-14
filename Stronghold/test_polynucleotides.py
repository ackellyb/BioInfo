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
