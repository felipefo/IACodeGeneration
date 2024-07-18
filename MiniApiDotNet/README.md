# IACodeGenerator

```
python -m venv myenv
myenv\Scripts\activate
pip install requiriments.txt

```

# Configuração do gemini 

Confige a key do gemini google_api_key="" 

```
gemini_model = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-pro-latest",
    verbose=True,
    temperature=0,
    top_p=0.1,
    top_k =2,
    google_api_key=""
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


- dsl: pastas com arquivos  
- exemplos: pastas com arquivos de exemplos com código fonte 
- saida: pastas com saida da IA
- MiniApiDotNet: Projeto dot net
- pos_geracao: arquivo python que formata a geração do codigo vindo da IA