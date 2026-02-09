# Base de Conhecimento

> [!TIP]
>  **Prompt sugerido para esta etapa:**
> ```
> Preciso organizar a base de conhecimento do meu agente financeiro.
>
> Tenho estes arquivos de dados: [Liste os arquivos de dados].
> 
> Me ajude a:
> (1) Entender o que cada arquivo contém,
> (2) Decidir como usar cada um,
> (3) Criar um exemplo de contexto formatado para incluir no prompt.

## Dados Utilizados

Foram utilizados os arquivos que estão em `data`, adicionando apenas a data de vencimento ao arquivo `produtos_financeiros.json`.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores. |
| `perfil_investidor.json` | JSON | Personalizar recomendações. |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados foram expandidos apenas no arquivo `produtos_financeiros.json`, adicionando a data de vencimento do produto.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos serão carregados via código:

```python
import pandas as pd
import json

perfil = json.load(open('data/perfil_investidor.json'))
transacoes = pd.read_csv('data/transacoes.csv')
historico = pd.read_csv('data/historico_atendimento.csv')
produtos = json.load(open('data/produtos_financeiros.json'))
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para fins de simplificação, podemos "injetar" os dados no prompt, garantindo que o Agente tenha o melhor contexto possível. Vale ressaltar que, em solução mais robustas, o ideal é que estas informações sejam carregadas dinamicamente para que possamos obter flexibilidade.

```text
- Dados do Cliente e Perfil (data/perfil_investidor.json):

{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

- Transações do Cliente (data/transacoes.csv):

data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

- Histórico de Atendimento do Cliente (data/historico_atendimento.csv):

data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

- Produtos disponíveis para (Re)Investimento (data/produtos_financeiros.json):

[
  {
    "nome": "Tesouro Selic 2026",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes",
    "data_vencimento": "01/03/2026"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário",
    "data_vencimento": "01/09/2026"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)",
    "data_vencimento": "01/06/2026"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação",
    "data_vencimento": "01/10/2026"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo",
    "data_vencimento": "01/12/2026"
  }
]
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo abaixo baseia-se nos dados originais da base de conhecimentos fornecida, mas de forma sintetizada, deixando apenas as informações mais relevantes, otimizando assim o consumo de tokens, mas sem perder o contexto.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Resumo de Gastos:
- Moradia: R$ 1.380,00
- Alimentação: R$ 570,00
- Transporte: R$ 295,00
- Saúde: R$ 188,00
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90

Produtos Disponíveis para Re(Investimento):
- Tesouro Selic 2026 (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Multimercado (risco médio)
- Fundo de Ações (risco alto)
```
