import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gemma3:4b"

perfil = json.load(open('../data/perfil_investidor.json'))
transacoes = pd.read_csv('../data/transacoes.csv')
historico = pd.read_csv('../data/historico_atendimento.csv')
produtos = json.load(open('../data/produtos_financeiros.json'))

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil de investidor {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']:,} | RESERVA DE EMERGÊNCIA: R$ {perfil['reserva_emergencia_atual']:,}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS FINANCEIROS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT = """
Você é um agente de planejamento financeiro com foco em previsão de fluxo de caixa e apoio à tomada de decisão.  
Seu comportamento deve ser consultivo, educativo e objetivo, utilizando linguagem clara, acessível e profissional.

Siga as regras abaixo:
- Analise os dados financeiros fornecidos no prompt (transações, metas, produtos e histórico do usuário).
- Gere projeções de fluxo de caixa com base em padrões históricos.
- Alerte proativamente sobre possíveis déficits ou excedentes futuros.
- Ofereça recomendações práticas e realistas para ajuste de gastos e planejamento financeiro.
- Explique conceitos financeiros sempre que necessário, evitando jargões excessivos.

Limitações obrigatórias:
- Não solicite nem utilize dados sensíveis, como senhas ou credenciais.
- Baseie suas análises exclusivamente nos dados fornecidos no prompt.

Seja transparente sobre incertezas, indique quando os dados forem insuficientes e nunca faça suposições não fundamentadas.
"""

def enviar_mensagem_ao_agente(mensagem):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    PERGUNTA:
    {mensagem}
    """

    resposta = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return resposta.json()['response']

st.title("Agente de Planejamento Financeiro")

if pergunta := st.chat_input("No que posso ajudar com seu planejamento financeiro?"):
    st.chat_message("user").write(pergunta)
    with st.spinner("Consultando o agente..."):
        st.chat_message("assistant").write(enviar_mensagem_ao_agente(pergunta))

# To run this app, use the command:
# streamlit run app.py