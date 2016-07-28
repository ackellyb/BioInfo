import pytest
from rosalind_library import DNA
from rosalind_library import RNA


class TestDNA:
    def test_create_dna_wrong_values(self):
        with pytest.raises(ValueError) as ve_info:
            DNA('AUGCT')

    def test_create_dna_success(self):
        dna = DNA('ACGT')
        assert dna.string == 'ACGT'

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

    def test_dna_gc_content_success(self):
        expected = 66.666
        dna = DNA("CCGGTA")
        result = dna.gc_content()
        assert abs(expected-result) < 0.001

    def test_hamming_distance_no_diff(self):
        expected = 0
        dna = DNA("CCC")
        dna2 = DNA("CCC")
        result = dna.get_hamming_distance(dna2)
        assert expected == result

    def test_hamming_distance_diff(self):
        expected = 7
        dna = DNA("GAGCCTACTAACGGGAT")
        dna2 = DNA("CATCGTAATGACGGCCT")
        result = dna.get_hamming_distance(dna2)
        assert expected == result
