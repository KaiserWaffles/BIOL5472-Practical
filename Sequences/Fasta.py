import typing
from . import Sequences as Sequences
from . import Fasta as Fasta
from .Sequences import BioSequence 
from typing import Iterator,Type

# class to parse a fasta file    
class FastaFile:

    # constructor - only attribute is string containing a file name
    # None as __init__ doesnt return anything
    def __init__(self, file: str) -> None:
        self._file = file

    # getter for file name
    @property
    def file(self) -> str:
        return self._file

    # method to get DNASequence records out from a fasta file
    # yields so we can iterate all the way over the file
    # and return a DNASequence for every pair of lines
    # this function now takes the sequence class as a parameter
    
    def get_seq_record(self, sequence_class: type[BioSequence]) -> Iterator[BioSequence]:
        with open(self.file) as filehandle:
            for line in filehandle:
                if line.startswith('>'):
                    id = line.rstrip().lstrip('>')
                    seq = next(filehandle).rstrip()
                yield sequence_class(id, seq)    

