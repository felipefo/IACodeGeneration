import os
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import re
import google.generativeai as genai

#genai.configure(api_key="...")     
#llm = genai.GenerativeModel("gemini-pro") //codigo mais rapido mas menos preciso

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
    google_api_key=""
)

# Definição do template de prompt
prompt_template_dsl_to_csharp = PromptTemplate(
    input_variables=["dsl" , "codigo_csharp" , "codigo_entity"],
    template="Use o codigo de exempo em csharp: {codigo_csharp} e ao criar a classe extenda a classe {codigo_entity} e import do namespace de {codigo_entity} em todas as classes criadas, deixe os marcadores // para referencia, use o namespace parecido com o que esta la, converta o seguinte diagrama DSL de modelo de domínio em código C#:\n\n{dsl}"
)

prompt_template_code = PromptTemplate(
    input_variables=["dsl", "codigo_csharp"],
    template="Coloque o nome do projeto ConectaFapes no namespace no lugar da palavra MeuProjeto. Resolva as importacoes entre as classe quando e das com a Classe Entity.cs \n\n{codigo_csharp}"
)

# Função para chamar o modelo Gemini
def run_gemini_chain(prompt_template, inputs):
    prompt = prompt_template.format(**inputs)
    return gemini_model.invoke(prompt)
    #return  llm.generate_content(prompt)
   

# Função para ler o conteúdo de um arquivo
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Função para processar o conteúdo do arquivo DSL com a cadeia
def process_file_with_chain(file_path, file_resolucao, file_entity):
    # Ler o conteúdo do arquivo
    dsl_content = read_file(file_path)
    codigo_csharp = read_file(file_resolucao)
    codigo_entity  = read_file(file_entity)
    # Processar o conteúdo com a cadeia
    result = run_gemini_chain(prompt_template_dsl_to_csharp, {"dsl": dsl_content , "codigo_csharp": codigo_csharp, "codigo_entity": codigo_entity})
    codigo = run_gemini_chain(prompt_template_code, {"codigo_csharp": result} )

    
    return codigo

# Testar a função com o arquivo DSL "path_to_your_dsl_file"
dsl_file_path = "./dsl/modelo.dsl"
file_resolucao = "./exemplos/domain/Resolucao.cs"
file_entity = "./exemplos/domain/Entity.cs"
result = process_file_with_chain(dsl_file_path, file_resolucao, file_entity)

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
caminho_arquivo = "./saida/resultado.txt"
escrever_string_em_arquivo(caminho_arquivo, conteudo)


   
