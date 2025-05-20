Loja de Programação
Estrutura do Site

Loja: Página principal com produtos, filtros por categoria e preço, e opção de adicionar ao carrinho.
Login/Registro: Sistema de autenticação para usuários.
Carrinho: Permite adicionar e remover produtos.
Fundamentos: Seção educativa sobre estruturas de seleção, repetição, vetores/matrizes, funções e tratamento de exceção.
Tire Dúvidas: Formulário para perguntas (simulação da API do Gemini).
Dicionário: Gerenciamento de termos de programação em arquivo de texto.
Equipe: Informações sobre os desenvolvedores.

Tecnologias

Linguagem: Python (Flask)
Frontend: HTML, CSS, JavaScript
Banco de Dados: SQLite (produtos, usuários, carrinho)
Persistência de Termos: Arquivo de texto (terms.txt)
Outros: Jinja2 para templates, Werkzeug para segurança.

Integração com a API do Gemini
A integração com a API do Gemini foi simulada, retornando respostas fictícias para perguntas enviadas via formulário.
Como Executar

Instale Python 3.8+.
Instale dependências: pip install flask.
Crie a estrutura de pastas e coloque os arquivos fornecidos.
Execute: python app.py.
Acesse http://localhost:5000 no navegador.

Principais Partes do Código

app.py: Configura o Flask, rotas, banco de dados SQLite e gerenciamento do dicionário.
templates/: Arquivos HTML com Jinja2 para renderização dinâmica.
static/css/style.css: Estilização da interface.
static/js/script.js: Interatividade para filtros.
terms.txt: Armazena termos e definições do dicionário.

Notas

As imagens dos produtos devem ser colocadas em static/images/.
O arquivo terms.txt é criado automaticamente ao adicionar termos.
Substitua 'chave_secreta' em app.py por uma chave segura.

