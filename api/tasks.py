from django_rq import job
from random import shuffle
from Bio import SeqIO
from api.models import Protein, Search

@job
def perform_search(search_id):
    search = Search.objects.get(pk=search_id)
    dna_sequence = search.query
    proteins = list(Protein.objects.all())
    shuffle(proteins)

    for protein in proteins:
        type = 'genbank' if protein.sequence_file_name.endswith('.gb') else 'fasta'
        for seq_record in SeqIO.parse(f'./data/sequences/{protein.sequence_file_name}', type):
            # print(repr(seq_record.seq))
            location = seq_record.seq.find(dna_sequence)
            # print(f'Location: {location}')
