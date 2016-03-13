import pytest
from rosalind_library import RNA


class TestRNA:

    def test_create_rna_wrong_values(self):
        with pytest.raises(ValueError) as ve_info:
            rna = RNA('AUGCT')

    def test_create_rna_success(self):
        rna = RNA('ACGU')
        assert rna.string == 'ACGU'

    def test_rna_equal_success(self):
        rna1 = RNA('ACG')
        rna2 = RNA('ACG')
        assert rna1 == rna2

    def test_rna_not_equal_success(self):
        rna1 = RNA('ACG')
        rna2 = RNA('ACGU')
        assert rna1 != rna2
