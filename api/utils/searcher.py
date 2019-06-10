"""A class for searching protein sequences"""
from random import shuffle
from Bio import SeqIO
from api.models import Protein

class Searcher():
    """Searches for a protein containing a given DNA sequence"""

    def find_sequence(self, dna_sequence):
        """Search for a given DNA sequence"""

        proteins = self.random_protein_list()
        for protein in proteins:
            type = 'genbank' if protein.sequence_file_name.endswith('.gb') else 'fasta'
            for seq_record in SeqIO.parse(f'./data/sequences/{protein.sequence_file_name}', type):
                location = seq_record.seq.find(dna_sequence)
                if location > -1:
                    return {'protein': protein, 'location': location}

        return None

    def random_protein_list(self):
        """Generate a randomized list of all proteins"""
        proteins = list(Protein.objects.all())
        shuffle(proteins)
        return proteins
