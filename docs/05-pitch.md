# Pitch (3 minutos)

## Roteiro

### 1. O Problema (30 seg)
> Qual dor do cliente você resolve?

Para muitos profissionais autônomos, a dor é dupla: cash flow irregular e ausência de um plano prático para completar a reserva de emergência. Apesar de ter um patrimônio total de R$ 12.000,00 e uma reserva parcial de R$ 6.000,00, Carlos não sabe exatamente se suas despesas recorrentes e metas vão se compatibilizar com sua renda mensal e seus gastos. Ele precisa de previsões acionáveis, alertas sobre déficits futuros e recomendações seguras e fáceis de implementar, sem jargões técnicos.

### 2. A Solução (1 min)
> Como seu agente resolve esse problema?

Apresentamos um agente de planejamento financeiro baseado em um pequeno app Streamlit que combina dados reais do usuário (perfil, transações e histórico de atendimentos) com um modelo LLM local (via Ollama). O agente:

- Consolida e interpreta transações históricas para gerar projeções de fluxo de caixa.
- Identifica risco de déficit e calcula quanto falta para atingir metas.
- Gera recomendações práticas e alinhadas ao perfil conservador do cliente.
- Explica, em linguagem acessível, o porquê das recomendações e os trade-offs (liquidez, impostos, prazos).

Tudo isso em um fluxo de chat simples: o usuário pergunta e recebe uma resposta contextualizada, num formato consultivo e educativo.

### 3. Demonstração (1 min)
> Mostre o agente funcionando

O vídeo mostra uma gravação de tela com estes passos rápidos:

1. Início do app (`streamlit run src/app.py`) e visualização do título "Agente de Planejamento Financeiro".
2. Exibição dos dados carregados: perfil do cliente (Carlos Mendes — 29 anos, conservador), patrimônio (R$ 12.000), reserva atual (R$ 6.000) e metas (ex.: completar reserva até 2026-03).
3. Entrada no chat: o usuário digita Ex: "Preciso saber se vou completar minha reserva de emergência até 2026-03 e o que devo fazer".
4. O agente analisa as transações recentes, gera uma projeção de fluxo de caixa e responde com:
	- Situação atual em números (saldo esperado, lacunas para a meta).
	- Ações recomendadas (ex.: aumentar aporte mensal X, cortar despesa Y, direcionar economia para Tesouro Selic ou CDB de liquidez diária).
	- Sugestão de um plano para atingir a meta no prazo, com estimativas de impacto.
5. Demonstração de explicação educativa: o agente descreve por que Tesouro Selic é indicado para reserva de emergência e compara com alternativas (LCI/LCA, CDB) no contexto de um perfil conservador.

A gravação ressalta a velocidade da resposta, a personalização (usa transações e histórico do próprio cliente) e a clareza das recomendações.

### 4. Diferencial e Impacto (30 seg)
> Por que essa solução é inovadora e qual é o impacto dela na sociedade?
Diferenciais:

- Integra dados transacionais reais com um modelo de linguagem para produzir planejamento financeiro prático — não apenas teoria.
- Foco em explicações acessíveis e recomendações acionáveis, desenhadas para perfis conservadores que priorizam segurança e liquidez.
- Arquitetura pensada para privacidade e autonomia, facilitando adoção em ambientes sensíveis a dados.

Impacto:

Ao automatizar projeções e oferecer intervenções simples e mensuráveis, o agente ajuda usuários como Carlos a completar reservas de emergência, evitar déficits e tomar decisões financeiras mais informadas. Isso aumenta a resiliência financeira de trabalhadores autônomos e melhora a saúde financeira em escala, reduzindo vulnerabilidade a choques e promovendo inclusão financeira.

---

## Link do Vídeo

[Link do vídeo]
