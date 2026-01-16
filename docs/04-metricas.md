# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** R$ 2815,00 baseado no `transacoes.csv`
- **Resultado:** [ ] Correto [ ] Parcialmente Correto [X] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente (conservador)
- **Resultado:** [ ] Correto [X] Parcialmente Correto [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [ ] Correto [ ] Parcialmente Correto [X] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto ITUB4?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [ ] Correto [ ] Parcialmente Correto [X] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente entendeu bem o perfil de investidor do usuário e consegue parcialmente dar boas respostas quando usa os dados mockados.

**O que pode melhorar:**
- Independente do que for passado no prompt, o agente sempre pensa no próximo passo, mesmo quando não é necessário.
- Em pedidos que exijam um pouco de processamento para analise ou calculo, o agente começa a dar respostas equivocadas as vezes com informações parcialmente corretas.