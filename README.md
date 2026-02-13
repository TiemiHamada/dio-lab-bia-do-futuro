# 💰 InvestAI - Agente Financeiro Inteligente

Um agente de IA Generativa especializado em propor reinvestimentos personalizados de produtos financeiros a vencer.

## 🎯 O Problema

Milhões de brasileiros possuem investimentos vencidos sem saber, resultando em perda de rentabilidade. O InvestAI atua proativamente no momento crítico do vencimento, evitando que o saldo fique parado e sugerindo as melhores opções de reinvestimento.

## 💡 A Solução

Agente consultivo que:
- 🔍 Monitora produtos a vencer
- 📊 Analisa o perfil do investidor
- 💼 Sugere reinvestimentos personalizados
- 🛡️ Garante respostas seguras (sem alucinações)

## 🏗️ Arquitetura

```mermaid
flowchart LR
    A[Cliente] --> B[Streamlit]
    B --> C[Ollama/LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> B
    B --> A
```

## 🚀 Como Executar

### 1. Instalar Ollama
```bash
# Baixe em ollama.com
ollama pull gpt-oss:20b-cloud
ollama serve
```

### 2. Instalar dependências
```bash
pip install streamlit pandas requests
```

### 3. Rodar a aplicação
```bash
streamlit run src/app.py
```

## 📁 Estrutura do Projeto

```
📁 lab-agente-financeiro/
├── 📁 data/                     # Base de conhecimento (JSON/CSV)
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   ├── transacoes.csv
│   └── historico_atendimento.csv
├── 📁 docs/                     # Documentação completa
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
├── 📁 src/
│   └── app.py                   # Aplicação Streamlit
└── README.md
```

## 🎬 Demonstração

[Assista ao pitch de 3 minutos](https://drive.google.com/file/d/1nJn3yPchm_1LAXIe8W6KvNa7yVEqtFbK/view?usp=drive_link)

## 🎯 Funcionalidades

**Perguntas que o InvestAI responde:**
- "Como vão as minhas finanças?"
- "Poderia me falar sobre meu saldo a vencer?"
- "Onde estou gastando mais?"
- "Me recomenda investir em CDB?"

**O que ele NÃO faz:**
- ❌ Não acessa dados bancários reais
- ❌ Não substitui assessor de investimentos
- ❌ Não responde sobre assuntos fora do escopo financeiro

## ✅ Métricas de Qualidade

| Métrica | Resultado |
|---------|-----------|
| **Assertividade** | ✅ Responde corretamente às perguntas |
| **Segurança** | ✅ Não inventa informações |
| **Coerência** | ✅ Respeita o perfil do cliente |

## 🛠️ Tecnologias

- **LLM:** Ollama (gpt-oss:20b-cloud)
- **Interface:** Streamlit
- **Base de Dados:** JSON + CSV
- **Linguagem:** Python 3.x

## 📖 Documentação Detalhada

Toda a documentação do projeto está em [`docs/`](./docs/):
- Caso de uso e arquitetura
- Estratégia de base de conhecimento
- Engenharia de prompts
- Métricas de avaliação
- Roteiro do Pitch

## 🔐 Segurança e Anti-Alucinação

- ✅ Respostas baseadas apenas em dados fornecidos
- ✅ Admite quando não sabe algo
- ✅ Não faz recomendações sem contexto do perfil

## 🎓 Desenvolvido por

Tiemi Hamada - Desafio DIO - Construa seu Assistente Virtual com IA Generativa

---

⭐ **Diferencial:** Transforma o vencimento de investimentos em uma oportunidade ativa de decisão financeira, com custo zero e sem exposição de dados sensíveis.
