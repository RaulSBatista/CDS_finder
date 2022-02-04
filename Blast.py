from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import sys
import os

cepas = input('Digite a cepa: ')
out = 'Blast'+cepas+'.xml'
cepas = cepas+'.fasta'

cline = NcbiblastnCommandline(cmd = 'blastn', query = "C:/Users/raulS/Desktop/programas/Programa_Tobias/Regioes/All_regions.fasta", subject = cepas, outfmt = 5, out = out, reward = 1, penalty =-1, gapopen = 5, gapextend = 2)

os.system((str(cline)))
print(cline)

out = out.removeprefix('xml')

with open(out,'r') as resultado:
    Regiao = 1
    for region, record in enumerate(NCBIXML.parse(resultado)):
        lista = []
        print('REGION ' + str(region + 1) + '\n')
        for alignment in record.alignments:
            Alig = 1
            for hsp in alignment.hsps:
                align_len = hsp.align_length
                FROM = hsp.sbjct_start
                TO = hsp.sbjct_end
                if align_len >= 1000:
                    lista.append(f' Região: {Regiao}, Número alinhamento: {Alig} começa: {FROM}, termina: {TO}')
                    print(lista)
                    input()
                Alig += 1
        Regiao += 1
        lista_final.append(lista)

print(lista_final)

