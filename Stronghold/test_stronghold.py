import pytest
from rosalind_library import DNA
import dna_count_nucleotides
import rna_dna_transcription


class TestStronghold:

    def test_dna_count_nucleotides_format(self):
        expected = '20 12 17 21'
        dna = DNA('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
        result = dna_count_nucleotides.format_string(dna)
        assert expected == result

    def test_rna_dna_transcription_format(self):
        expected = 'GAUGGAACUUGACUACGUAAAUU'
        dna = DNA('GATGGAACTTGACTACGTAAATT')
        result = rna_dna_transcription.format_string(dna)
        assert expected == result
