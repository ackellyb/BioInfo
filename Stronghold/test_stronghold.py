import pytest
from rosalind_library import DNA
import dna_count_nucleotides


class TestStronghold:

    def test_dna_count_nucleotides_format(self):
        expected = '2 1 0 3'
        dna = DNA('ACTTAT')
        result = dna_count_nucleotides.create_nucleotide_count_string(dna)
        assert expected == result
