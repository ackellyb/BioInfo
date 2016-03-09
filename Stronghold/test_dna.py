import pytest
from rosalind_library import DNA
from rosalind_library import RNA


class TestDNA:

    def test_create_dna_wrong_values(self):
        with pytest.raises(ValueError) as ve_info:
            dna = DNA('AUGCT')

    def test_create_dna_success(self):
        dna = DNA('ACGT')
        assert dna.dna == 'ACGT'

    def test_create_dna_mixed_case(self):
        dna = DNA('aCGta')
        assert dna.dna == 'ACGTA'

    def test_dna_equal_success(self):
        dna1 = DNA('ACG')
        dna2 = DNA('ACG')
        assert dna1 == dna2

    def test_dna_not_equal_success(self):
        dna1 = DNA('ACG')
        dna2 = DNA('ACGT')
        assert dna1 != dna2

    def test_count_nucleotides_empty(self):
        expected = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        dna = DNA('')
        result = dna.nucleotide_counts()
        assert expected == result

    def test_count_nucleotides_success(self):
        expected = {'A': 2, 'C': 1, 'G': 0, 'T': 3}
        dna = DNA('ACTTAT')
        result = dna.nucleotide_counts()
        assert expected == result

    def test_dna_to_rna_success(self):
        expected = RNA('ACGU')
        dna = DNA('ACGT')
        result = dna.to_rna()
        assert expected == result

    def test_dna_reverse_complement_success(self):
        expected = 'CGTA'
        dna = DNA('TACG')
        result = dna.reverse_complement()
        assert result == expected
