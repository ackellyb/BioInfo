import pytest
from Classes.nucleic_acid import RNA


class TestRNA:

    def test_create_rna_wrong_values(self):
        with pytest.raises(ValueError) as ve_info:
            RNA('AUGCT')

    def test_create_rna_success(self):
        rna = RNA('ACGU')
        assert rna.string == 'ACGU'

    def test_transcribe_to_protein_success(self):
        expected = 'MAMAPRTEINSTRING'
        rna = RNA('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')
        result = rna.transcribe_to_protein()
        assert expected == result

    def test_transcribe_to_protein_early_stop(self):
        expected = 'MAMA'
        rna = RNA('AUGGCCAUGGCGUGACCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGG')
        result = rna.transcribe_to_protein()
        assert expected == result
