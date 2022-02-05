from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIXML
import sys
import os
import pandas as pd

cepas = input('Digite a cepa: ')
out = 'Blast'+cepas+'.xml'
Cepas = cepas+'.fasta'

cline = NcbiblastnCommandline(cmd = 'blastn', query = "C:/Users/raulS/Desktop/programas/Programa_Tobias/Regioes/All_regions.fasta", subject = Cepas,outfmt = 5, out = out,reward = 1, penalty =-2, gapopen = 5, gapextend = 2)

os.system((str(cline)))
print(cline)

out = out.removeprefix('xml')

tabela = pd.read_excel('DATABASE.xlsx')

lista_final = []

with open(out,'r') as resultado:
    Regiao = 1
    for region, record in enumerate(NCBIXML.parse(resultado)):
        lista = []
        R = ('Region ' + str(region + 1) + '\n')
        print(R)
        Alig = 0
        for alignment in record.alignments:
            for hsp in alignment.hsps:
                align_len = hsp.align_length
                Subj_FROM = hsp.sbjct_start
                Subj_TO = hsp.sbjct_end
                Query_FROM = hsp.query_start
                Query_TO = hsp.query_end
                if align_len > 1000 or hsp.align_length >= 450 and hsp.expec == 0:
                    Alig += 1
                    #lista = (f'AL{Alig}(Query:{Query_FROM}...{Query_TO},Subject:{Subj_FROM}...{Subj_TO})'+'\n')
                    lista = (f'{Subj_FROM}...{Subj_TO}')
                    tabela.loc[f'Alinhamento: {Alig}', R] = lista
                    print(lista)
                    input()
            tabela.to_excel('DATABASE.xlsx')
        Regiao += 1
        lista_final.append(lista)

print(lista_final)
