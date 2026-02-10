# Passo a Passo de Execução

## Setup do Ollama

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss:20b-cloud

# 3. Testar se funciona
ollama run gpt-oss:20b-cloud "Olá!"
```

## Código Completo

Todo o código-fonte está no arquivo `app.py`.

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar a aplicação
streamlit run .\Desafios\src\app.py
```

## Evidências de Execução

<img width="1916" height="998" alt="image" src="https://github.com/user-attachments/assets/396bca1b-e2fd-48a4-8767-b47c210d47ca" />


