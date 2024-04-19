import subprocess

def iniciarServico(nome):
    cmd = f'sc queryex "{nome}"'
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)

    if 'RUNNING' in result.stdout:
        print(f'O serviço {nome} já está em execução.')
    else:
        cmd = f'net start "{nome}"'
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)

        if 'was started successfully' in result.stdout:
            print(f'O serviço {nome} foi iniciado com sucesso.')
        else:
            print(f'Não foi possível iniciar o serviço {nome}.')

iniciarServico('NomeDoServico')
