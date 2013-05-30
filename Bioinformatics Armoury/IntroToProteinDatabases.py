from Bio import ExPASy
from Bio import SwissProt

#file = open(r"C;\Users\Aaron\Downloads\rosalind_dbpr.txt","r")
#for x in file.readline():
handle = ExPASy.get_sprot_raw("H3SRW3")
record = SwissProt.read(handle)
print record.molecule_type
