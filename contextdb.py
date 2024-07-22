import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import re
import google.generativeai as genai

# eu sei, to repetindo codigo! coisa feia, nao facam isso.. :D
IA_API_KEY = os.getenv('IA_API_KEY')

if IA_API_KEY:
    print(f'O valor da variável IA_API_KEY é: {IA_API_KEY}')
else:
    print('A variável IA_API_KEY não está definida')


def extrair_codigo_python(content):
    padrao = r'```python\n(.*?)```'
    resultado = re.search(padrao, content, re.DOTALL)
    if resultado:
        return resultado.group(1)
    return ""


# Configuração do modelo Google GenAI
gemini_model = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-pro-latest",
    verbose=True,
    temperature=0,
    top_p=0.1,
    top_k =2,
    google_api_key=IA_API_KEY
)

# Definição do template de prompt
prompt_template_dsl_to_csharp = PromptTemplate(
    input_variables=["entidades" , "context_db"],
    template="Alere a classe {context_db} para ter as novas entidades presentes em {entidades}"
)

# Função para chamar o modelo Gemini
def run_gemini_chain(prompt_template, inputs):
    prompt = prompt_template.format(**inputs)
    return gemini_model.invoke(prompt)
    #return  llm.generate_content(prompt)
   

# Função para ler o conteúdo de um arquivo
def read_file(file_path):
    with open(file_path, 'r', encoding='cp1252') as file:
        return file.read()

# Função para processar o conteúdo do arquivo DSL com a cadeia
def process_file_with_chain(file_contextdb, entidades):
    # Ler o conteúdo do arquivo
    codigo_contextdb = read_file(file_contextdb)
    codigo_entity  = read_file(entidades)
    
    # Processar o conteúdo com a cadeia
    result = run_gemini_chain(prompt_template_dsl_to_csharp, {"entidades": codigo_entity, "context_db": codigo_contextdb})
    
    return result

file_novas_entidades = "./saida/resultado.txt"
file_contextdb = "./MiniApiDotNet/TodoDb.cs"
result = process_file_with_chain( file_novas_entidades, file_contextdb)

# Imprimir o resultado
print(result.pretty_repr(False))

def escrever_string_em_arquivo(caminho_arquivo, conteudo):
    try:
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)
        print(f"Conteúdo escrito com sucesso no arquivo: {caminho_arquivo}")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo: {e}")

# Exemplo de uso
conteudo = result.pretty_repr(False)
caminho_arquivo = "./saida/contextdb.txt"
escrever_string_em_arquivo(caminho_arquivo, conteudo)


   
