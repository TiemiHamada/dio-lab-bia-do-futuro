import json
import pandas as pd
import requests
import streamlit as st

# ========== CONFIGURAÇÃO ========== #
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b-cloud"

# ========== CARREGAR DADOS ========== #
perfil = json.load(open('Desafios/data/perfil_investidor.json'))
transacoes = pd.read_csv('Desafios/data/transacoes.csv')
historico = pd.read_csv('Desafios/data/historico_atendimento.csv')
produtos = json.load(open('Desafios/data/produtos_financeiros.json'))

# ========== MONTAR CONTEXTO ========== #
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ========== SYSTEM PROMPT ========== #
SYSTEM_PROMPT = """Você é o InvestAI, um agente financeiro inteligente especializado em Investimentos.
Seu objetivo é propor reinvestimento de saldo a vencer, através de sugestões de investimentos personalizados por cliente.

REGRAS:
- Sempre baseie suas respostas nos dados fornecidos
- Nunca invente informações financeiras
- Quando não sabe alguma informação, admita e ofereça alternativas
- Utiliza linguagem simples
"""

# ========== CHAMAR OLLAMA ========== #
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    Pergunta: {msg}"""
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ========== INTERFACE ========== #
st.title("💰 InvestAI, um agente financeiro inteligente especializado em Investimentos")

if pergunta := st.chat_input("Sua solicitação sobre re(investimentos)..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
