import os
import re

def criar_diretorio(caminho):
    caminho = caminho.replace("\\", "/")
    if not os.path.exists(caminho):
        os.makedirs(caminho)

def salvar_arquivo(caminho, conteudo):
    caminho = caminho.replace("\\", "/")
    with open(caminho, 'w', encoding='cp1252') as arquivo:
        arquivo.write(conteudo)

def processar_arquivo(arquivo_entrada):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as file:
            linhas = file.readlines()
    except UnicodeDecodeError:
        try:
            with open(arquivo_entrada, 'r', encoding='latin-1') as file:
                linhas = file.readlines()
        except UnicodeDecodeError:
            with open(arquivo_entrada, 'r', encoding='cp1252') as file:
                linhas = file.readlines()

    dentro_bloco = False
    nome_arquivo = ""
    conteudo_bloco = []
    namespace = ""

    for linha in linhas:
        if linha.startswith("//Inicio:"):
            dentro_bloco = True
            nome_arquivo = linha.split(":")[1].strip()
            conteudo_bloco = []
        elif linha.startswith("//Fim:") and dentro_bloco:
            dentro_bloco = False

            # Crie diretório e arquivo com base no namespace e nome do arquivo
            if namespace:
                caminho_diretorio =  diretorio_projeto + "/" + os.path.join(*namespace.split('.'))
                criar_diretorio(caminho_diretorio)
                caminho_arquivo_completo = os.path.join(caminho_diretorio, nome_arquivo)
                salvar_arquivo(caminho_arquivo_completo, "".join(conteudo_bloco))

            namespace = ""
        elif dentro_bloco:
            conteudo_bloco.append(linha)
            # Captura o namespace
            if "namespace" in linha:
                match = re.search(r'namespace\s+([a-zA-Z0-9_.]+)', linha)
                if match:
                    namespace = match.group(1)

# Exemplo de uso
arquivo_entrada = './saida/resultado.txt'
diretorio_projeto = "./MiniApiDotNet"
processar_arquivo(arquivo_entrada)
