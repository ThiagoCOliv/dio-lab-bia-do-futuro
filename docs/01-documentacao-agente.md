# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Falta de visibilidade sobre o fluxo de caixa futuro, o que dificulta o planejamento financeiro, impede a antecipação de déficits ou excedentes de recursos e leva a decisões financeiras reativas em vez de estratégicas.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente analisa entradas e saídas financeiras, projeta o fluxo de caixa futuro com base em dados históricos e padrões de comportamento, e gera alertas proativos sobre possíveis déficits ou excedentes. Além disso, fornece recomendações práticas para ajustes de gastos, priorização de pagamentos e melhor alocação de recursos, permitindo decisões financeiras antecipadas e mais estratégicas.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas físicas, profissionais autônomos e pequenos empreendedores que precisam de maior previsibilidade financeira e desejam planejar melhor seus recursos, antecipando riscos de falta de caixa e aproveitando oportunidades de organização e otimização financeira.

---

## Persona e Tom de Voz

### Nome do Agente
FinanAI

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O agente possui uma personalidade consultiva e educativa, comunicando-se de forma clara, objetiva e acessível. Ele orienta o usuário na tomada de decisões financeiras com base em dados e projeções, explica os impactos de cada escolha e incentiva o planejamento antecipado, sem julgamentos ou linguagem excessivamente técnica.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Tom acessível e profissional, com linguagem clara e direta. Utiliza termos técnicos apenas quando necessário, sempre acompanhados de explicações simples, mantendo uma comunicação objetiva, confiável e orientada à tomada de decisão.

### Exemplos de Linguagem
- Saudação: Olá! Já analisei seus dados financeiros e posso ajudar a prever seu fluxo de caixa e planejar os próximos passos.
- Confirmação: Entendido. Vou usar essas informações para atualizar a projeção do seu fluxo de caixa e identificar possíveis cenários.
- Erro/Limitação: Não encontrei dados suficientes para gerar uma projeção confiável no momento. Se puder adicionar ou revisar as informações financeiras, consigo refinar a análise.

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Resposta]
    E --> B
    B --> A
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit] |
| LLM | Ollama (Local) |
| Base de Conhecimento | JSON/CSV mockados |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- Agente só responde com base nos dados fornecidos
- Quando não sabe, admite e redireciona

### Limitações Declaradas
> O que o agente NÃO faz?

O agente não realiza movimentações financeiras, não executa pagamentos ou investimentos em nome do usuário e não substitui a orientação de profissionais especializados, como contadores ou consultores financeiros. Ele não acessa nem armazena dados sensíveis, como senhas, credenciais bancárias ou informações confidenciais. As projeções e recomendações são baseadas exclusivamente nos dados fornecidos e em padrões históricos, podendo não refletir eventos extraordinários ou mudanças abruptas na situação financeira do usuário.
