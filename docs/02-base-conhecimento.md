# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados foram alterados e expandidos para enriquecer os cenários de teste do agente.

> ⚠️ As novas informações, incluindo transações, atendimentos e produtos financeiros, foram geradas por Inteligência Artificial exclusivamente para fins de teste e validação, podendo não representar a realidade de forma totalmente fiel ou refletir com precisão comportamentos e cenários financeiros reais.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON/CSV são carregados em um código python e incluídos no contexto do prompt.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados contidos nos arquivos são armazenados em variáveis no código em Python e inseridos diretamente no prompt no momento da execução do agente. Essas variáveis fornecem o contexto necessário para simular cenários financeiros, realizar análises, gerar projeções e produzir recomendações alinhadas às informações disponíveis. O system prompt permanece responsável por definir o comportamento, o tom de comunicação e as limitações do agente, enquanto os dados passados via prompt servem como base para o raciocínio do modelo.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: Carlos Mendes
- Perfil: conservador
- Saldo disponível: R$ 4.784,30

Últimas transações:
- 12/01: Conta de Água - R$ 90
- 10/01: Uber - R$ 40
...
```
