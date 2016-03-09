import pytest
from rosalind_library import DNA

class TestDNA:

    def test_create_dna_wrong_values(self):
        with pytest.raises(ValueError) as ve_info:
            dna = DNA('AUGCT')

    def test_create_dna_success(self):
        dna = DNA('ACGT')
        assert dna.dna == 'ACGT'

    def test_count_nucleotides_empty(self):
        expected = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        dna = DNA('')
        result = dna.nucleotide_counts()
        assert expected == result

    def test_count_nucleotides_success(self):
        expected = {'A': 20, 'C': 12, 'G': 17, 'T': 21}
        dna = DNA('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
        result = dna.nucleotide_counts()
        assert expected == result