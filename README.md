# ean-scrapy
um web scrapy para códigos ean-13 com banco dados público

# Projeto: Web Scraping de Códigos EAN-13 com Python

## 📋 Descrição
Projeto de coleta de códigos EAN-13 de produtos através de web scraping em fontes públicas, utilizando Python.

---

## 🛠️ Task List

### 1. Planejamento
- [x] Definir o(s) site(s) públicos de onde serão extraídos os dados.
- [x] Conferir se o scraping é permitido (verificar o `robots.txt`).
- [ ] Identificar quais campos além do EAN-13 serão coletados (ex: nome do produto, categoria, fabricante, etc).

### 2. Ambiente de Desenvolvimento
- [ ] Criar ambiente virtual com `venv` ou `poetry`.
- [ ] Instalar bibliotecas necessárias:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `sqlalchemy` (para integração com banco de dados)
  - `scrapy` (opcional, para projetos maiores)

### 3. Desenvolvimento do Scraper
- [ ] Implementar função para obter o HTML da página.
- [ ] Implementar função para extrair os dados desejados (parser).
- [ ] Criar lógica para navegar por múltiplas páginas (paginação).

### 4. Banco de Dados
- [ ] Escolher banco de dados (ex: `SQLite` para início rápido).
- [ ] Modelar a tabela (campos: EAN, Nome do Produto, Categoria, Fonte, Data de Coleta).
- [ ] Criar a conexão e funções de inserção dos dados via Python.

### 5. Tratamento de Dados
- [ ] Limpar e validar os códigos EAN-13 coletados.
- [ ] Evitar duplicidade de registros no banco de dados.

### 6. Automatização
- [ ] Programar o scraper para rodar de forma automatizada (usando `schedule` ou `cron`).

### 7. Documentação
- [ ] Criar `README.md` com:
  - Descrição do projeto
  - Instruções de instalação
  - Como rodar o scraper
- [ ] Comentar o código adequadamente.

### 8. Testes
- [ ] Implementar testes básicos com `pytest` para funções principais.

### 9. Versão Final
- [ ] Organizar estrutura de pastas (`src/`, `data/`, `tests/`, etc.).
- [ ] Gerar arquivo `requirements.txt` com dependências do projeto.

---

