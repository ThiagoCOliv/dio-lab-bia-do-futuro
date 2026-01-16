# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura

```
# Código da Aplicação

Esta pasta contém o código do agente de planejamento financeiro implementado em `src/app.py`.

O aplicativo é um front-end simples em Streamlit que carrega dados locais (perfil, transações e histórico) e envia prompts para um modelo LLM local via Ollama para gerar recomendações financeiras.

## Arquivos importantes

- `app.py` - Aplicação principal (Streamlit). Carrega os dados em `./data`, monta um contexto e envia perguntas ao agente via HTTP para o servidor Ollama.
- `../data/perfil_investidor.json` - Perfil do cliente (nome, idade, patrimônio, metas, etc.).
- `../data/transacoes.csv` - Histórico de transações usado para projeção de fluxo de caixa.
- `../data/historico_atendimento.csv` - Histórico de atendimentos que entra no contexto do agente.
- `../data/produtos_financeiros.json` - Catálogo de produtos financeiros que o agente pode referenciar.

## Dependências

As dependências usadas diretamente por `app.py` são:

- streamlit
- pandas
- requests

Você pode instalar rapidamente com:

```powershell
python -m pip install pandas requests streamlit
```

É recomendado usar um ambiente virtual. No PowerShell (Windows):

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas requests streamlit
```

Se preferir um `requirements.txt`, crie um arquivo com as dependências acima e instale com `python -m pip install -r requirements.txt`.

## Pré-requisitos adicionais

- Servidor Ollama rodando localmente e acessível em `http://localhost:11434` (ou ajustar `OLLAMA_URL` em `app.py`).
- Modelo compatível carregado em Ollama (o código default usa `MODELO = "gemma3:4b"`).

Sem o servidor Ollama ativo, o app tentará fazer uma requisição HTTP e falhará — você pode testar o restante das funcionalidades (leitura de dados) isoladamente, mas o chat depende do endpoint.

## Como rodar (PowerShell)

No diretório `src` (ou na raiz do projeto, ajustando caminhos relativos):

```powershell
# ativar ambiente (opcional)
. .\.venv\Scripts\Activate.ps1

# rodar app streamlit (executar a partir da pasta src)
streamlit run app.py
```

Observação: se você executar o comando a partir da raiz do repositório, use `streamlit run src/app.py`.

## Uso / Demonstração rápida

1. Abra o app no navegador (Streamlit mostrará a URL, normalmente `http://localhost:8501`).
2. No campo de chat, pergunte algo como:

```
Vou completar minha reserva de emergência até 2026-03? O que devo fazer?
```

3. O app enviará o contexto (perfil, transações e histórico) ao modelo via Ollama e exibirá a resposta do agente.

## Customização

- Para mudar o endpoint ou o modelo, edite as constantes `OLLAMA_URL` e `MODELO` no topo de `app.py`.
- Para adaptar o catálogo de produtos, edite `data/produtos_financeiros.json`.

## Observações e próximos passos sugeridos

- Adicionar um `requirements.txt` no repositório.
- Tratar erros de conexão com Ollama no `app.py` (capturar exceções de `requests` e mostrar mensagem amigável no Streamlit).
- Implementar testes simples que validem a leitura dos arquivos de dados e a criação do contexto.
