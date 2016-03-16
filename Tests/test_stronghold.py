import tempfile
from Stronghold import *
from Classes.nucleic_acid import FASTADNA, DNA


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

    def test_recv_dna_strand_complement_format(self):
        expected = 'ACCGGGTTTT'
        dna = DNA('AAAACCCGGT')
        result = recv_dna_strand_complement.format_string(dna)
        assert expected == result

    def test_fib_recurrence_rabbits_month_one(self):
        expected = 1
        result = fib_recurrence_rabbits.fibonacci_sequence(1, 1)
        assert expected == result

    def test_fib_recurrence_rabbits_month_two(self):
        expected = 1
        result = fib_recurrence_rabbits.fibonacci_sequence(2, 1)
        assert expected == result

    def test_fib_recurrence_rabbits_success(self):
        expected = 19
        result = fib_recurrence_rabbits.fibonacci_sequence(5, 3)
        assert expected == result

    def test_gc_content_computation(self):
        with tempfile.NamedTemporaryFile(mode="r+") as temp:
            expected = (60.919540, "Rosalind_0808")
            temp.write(""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT""")
            temp.flush()
            dna_list = FASTADNA.read_list_from_file(temp.name)
            result = gc_content_computation.compute(dna_list)
            assert abs(expected[0] - result[0]) < 0.001
            assert expected[1] == result[1]

    def test_mendels_first_law_computation_simple(self):
        expected = 0.78333
        result = iprb_mendels_first_law.compute(2, 2, 2)
        assert abs(expected - result) < 0.001

    def test_mendels_first_law_computation_complex(self):
        expected = 0.781772953415
        result = iprb_mendels_first_law.compute(27, 17, 23)
        assert abs(expected - result) < 0.001

