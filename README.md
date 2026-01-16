# 🤖 Agente de Planejamento Financeiro — Projeto

Este repositório contém um protótipo de um agente de planejamento financeiro que combina dados locais (perfil, transações e histórico) com um modelo de linguagem (LLM) — no projeto atual, a integração é feita via um servidor Ollama local. O front-end é uma app simples em Streamlit (`src/app.py`) que oferece uma interface de chat para perguntas financeiras contextualizadas.

O README a seguir explica como executar o projeto, dependências, arquivos de dados e pontos importantes para testar e estender o agente.

## Conteúdo principal

- `src/app.py` — Aplicação principal em Streamlit. Carrega dados da pasta `data/`, monta um contexto e envia prompts ao modelo via HTTP (configurado por `OLLAMA_URL`).
- `data/` — Dados mockados usados pelo agente: perfil do cliente, transações, histórico de atendimento e catálogo de produtos.
- `docs/` — Documentação e templates (documentação do agente, prompts, métricas, pitch).
- `examples/` — Referências e exemplos auxiliares.

## Dependências

Bibliotecas usadas diretamente pelo código:

- streamlit
- pandas
- requests

Recomendação: use um ambiente virtual. Para instalar rapidamente as dependências (PowerShell):

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas requests streamlit
```

Se preferir travar versões, crie `requirements.txt` com essas dependências e instale com `python -m pip install -r requirements.txt`.

## Pré-requisitos importantes

- Servidor Ollama local rodando e acessível em `http://localhost:11434` (ou ajuste `OLLAMA_URL` em `src/app.py`).
- Um modelo compatível carregado no Ollama. O código usa por padrão `MODELO = "gemma3:4b"` — verifique se esse modelo ou outro equivalente está disponível no seu Ollama.

Sem o Ollama ativo, o app fará a requisição HTTP e terá erro ao tentar obter respostas do agente. É possível usar o Streamlit apenas para visualizar que os dados foram carregados, mas o chat depende do endpoint.

## Como rodar (PowerShell)

1. Abra um terminal PowerShell na raiz do repositório.
2. (Opcional) Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

3. Instale dependências (se ainda não tiver instalado):

```powershell
python -m pip install pandas requests streamlit
```

4. Inicie o Ollama e carregue o modelo desejado (veja documentação do Ollama).
5. Execute o app (a partir da pasta `src`):

```powershell
cd src
streamlit run app.py
```

Observação: se preferir rodar direto da raiz, use `streamlit run src/app.py`.

## Dados usados pelo agente

Os arquivos em `data/` já contêm exemplos para um cliente fictício (Carlos Mendes). São eles:

- `perfil_investidor.json` — nome, idade, renda, metas e perfil de risco.
- `transacoes.csv` — histórico de entradas/saídas usado para projeções de fluxo de caixa.
- `historico_atendimento.csv` — registro de interações anteriores que entram no contexto.
- `produtos_financeiros.json` — catálogo de produtos que o agente pode recomendar.

Sinta-se livre para editar ou ampliar esses arquivos para testar cenários diferentes.

## Estrutura do projeto (resumida)

```
dio-lab-bia-do-futuro/
├── README.md                # este arquivo
├── data/                    # dados mockados (perfil, transações, produtos, histórico)
├── docs/                    # documentação e templates (prompts, métricas, pitch)
├── examples/                # exemplos e guias rápidos
└── src/
    ├── app.py               # app Streamlit que monta contexto e consulta o modelo via Ollama
    └── README.md            # instruções específicas da pasta src
```

## Recomendações de melhorias (próximos passos)

- Criar `src/requirements.txt` com versões pinadas.
- Tratar exceções em `src/app.py` para capturar erros de conexão com o Ollama e exibir mensagens amigáveis no Streamlit.
- Adicionar testes unitários simples que validem a leitura dos arquivos em `data/` e a montagem do `contexto`.
- Implementar logs e/ou modo de debug para inspecionar o prompt enviado ao modelo.