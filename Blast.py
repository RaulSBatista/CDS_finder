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
    for region, record in enumerate(NCBIXML.parse(resultado)):
        print('REGION ' + str(region + 1) + '\n')
        for alignment in record.alignments:
            for hsp in alignment.hsps:
                print(hsp)
                input()

'''
def Blasteia():
    input_BLAST = input('Digite o nome do arquivo: \n')#Pega o arquivo resultado do BLAST
    fasta_seq = SeqIO.parse(open(input_BLAST),'fasta')
    segmento_genoma = []#Cria a variável que armazena os segmentos
    n = 100

    for V1 in fasta_seq:#Para cada alinhamento ele vai abrir um for
        print (V1.seq)

        while V4:
            fs_lstrip = str("".join(V4))
            print(fs_lstrip)
            V2 = input('Digite: ')

            with open('meu_blast.xml','w+') as V3:
                print('blating.....\n')
                resultado_BLAST = NCBIWWW.qblast('blasntn','nt','fs_lstrip[:n]', hitlist_size= 10)
                print('escrevendo.....\n')
                V3.write(resultado_BLAST.read())
                del fs_lstrip[:n]

        print(len(segmento_genoma))
        input_BLAST = input('Digite o nome do arquivo: \n')

    with open('meu_blast.xml','w') as V3:
        print('blasting.....\n')
        resultado_BLAST = NCBIWWW.qblast('blastn','nt',segmento_genoma,hitlist_size= 10)
        print('escrevendo..... \n')
        V3.write(resultado_BLAST.read())

def reg_list():
    resutado = open('meu_blast.xml','r')
    blast_record = NCBIXML.read(resutado)
    lista_cepas = []

    for V5 in blast_record.alignments:
        for hsp in V5.hsp:
            titulo_alinhamento = str(V5.title)
            seq_cabecalhos = titulo_alinhamento.split('>')[0].replace(' ','_')
            seq_acess = V5.acession
            seq_lenth = V5.lenth
            seq_score = V5.score

            with open('Resultado_BLAST.txt','a') as r_BLAST:
                r_BLAST.write("="*100)
                r_BLAST.write("ID = %s\n\n" %seq_cabecalhos)
                r_BLAST.write("Código de acesso = %s \n" %seq_acess)
                r_BLAST.write("Tamanho da seq = %s \n" %seq_lenth)
                r_BLAST.write("Pontuação = %s \n" %seq_score)

Blasteia()
reg_list()
'''
