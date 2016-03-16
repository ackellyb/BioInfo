from Classes.nucleic_acid import _NucleicAcid, RNA, DNA


class TestDNA:
    def test_create_string_mixed_case_no_format(self):
        pn = _NucleicAcid('aCGta')
        assert pn.string == 'ACGTA'

    def test_nucleic_acid_equal_success(self):
        pn1 = _NucleicAcid('ACG')
        pn2 = _NucleicAcid('ACG')
        assert pn1 == pn2

    def test_nucleic_acid_not_equal_success(self):
        pn1 = _NucleicAcid('ACG')
        pn2 = _NucleicAcid('ACGT')
        assert pn1 != pn2

    def test_nucleic_acid_different_type(self):
        dna = DNA("ACG")
        rna = RNA("ACG")
        assert dna != rna

    def test_find_substring_locations_no_substring(self):
        expected = list()
        pn1 = _NucleicAcid('ACG')
        pn2 = _NucleicAcid('TC')
        result = pn1.find_substring_locations(pn2)
        assert expected == result

    def test_find_substring_locations_matching_substring_larger(self):
        expected = list()
        pn1 = _NucleicAcid('TC')
        pn2 = _NucleicAcid('ACG')
        result = pn1.find_substring_locations(pn2)
        assert expected == result

    def test_find_substring_locations_success(self):
        expected = [2, 4, 10]
        pn1 = _NucleicAcid('GATATATGCATATACTT')
        pn2 = _NucleicAcid('ATAT')
        result = pn1.find_substring_locations(pn2)
        assert expected == result
