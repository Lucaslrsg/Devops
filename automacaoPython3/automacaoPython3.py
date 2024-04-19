import os
import shutil


pasta_origem = '/caminho/'
pasta_destino = '/caminho/'


arquivos = os.listdir(pasta_origem)

for arquivo in arquivos:
    extensao = os.path.splitext(arquivo)[1]

    if extensao == '.txt':
        sub_pasta = 'Textos'
    elif extensao in ['.jpg', '.png', '.gif']:
        sub_pasta = 'Imagens'
    elif extensao == '.pdf':
        sub_pasta = 'PDFs'
    else:
        sub_pasta = 'Outros'

    if not os.path.exists(os.path.join(pasta_destino, sub_pasta)):
        os.makedirs(os.path.join(pasta_destino, sub_pasta))

    shutil.move(os.path.join(pasta_origem, arquivo), os.path.join(pasta_destino, sub_pasta, arquivo))
