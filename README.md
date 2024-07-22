# IACodeGenerator


```
python -m venv myenv
myenv\Scripts\activate
pip install requiriments.txt

```

# Configuração do gemini 

Confige a VARIAVEL DE AMBIENTE key do gemini AI_API_KEY="" 
setx AI_API_KEY "SUA_KEY"


```
gemini_model = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-pro-latest",
    verbose=True,
    temperature=0,
    top_p=0.1,
    top_k =2,
    google_api_key=AI_API_KEY
)
```

# Rodando a geracao de codigo 

## Gerando o codigo com a IA

```
python main.py

```

## Formatando codigo com a IA 

python pos_geracao/processa_saida.py


## Resultados 


O resultado é a criação de pastas de arquivos c# dentro do projeto DotNet: MiniApiDotNet


## Pastas

- dsl: pastas com arquivos  
- exemplos: pastas com arquivos de exemplos com código fonte 
- saida: pastas com saida da IA
- MiniApiDotNet: Projeto dot net
- pos_geracao: arquivo python que formata a geração do codigo vindo da IA


## Rodando o pipiline 

Rodando o pipeline com o Luigi 
- 1. Gera classes das entidades 
- 2. Formata as clases geradas
- 3. Gera o arquivo de contextodb
- 4. TODO: Copiar o arquivo para o local correto
- 5. TODO: Gerar o migration e aplicar

```
python pipeline.py 

```