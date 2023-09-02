# <img src = "https://i.imgur.com/saCuWe2.png" alt="bandeira americana" width="28" height="20"> Workshop - Fábrica de Software

Projeto desenvolvido como desafio para o processo seletivo da Fábrica de Software da UNIPE, o sistema foi feito utilizando o framework do Django REST, a aplicação consiste de um processo para a realização de uma matrícula em uma universidade.

## Tecnologias Utilizadas:

* [Python](https://www.python.org/): linguagem de programação
* [Django REST](https://www.django-rest-framework.org/): framework web
* [PostgreSQL](https://www.postgresql.org/): banco de dados

## Como executar:

### **1. Instale `Python` na sua máquina, por meio [deste link](https://www.python.org/)**

### **2. Faça um clone [desse repositório](https://github.com/jnicklr/WorkshopFabrica.git) na sua máquina:**

* Crie uma pasta no seu computador para esse programa
* Abra o `git bash` ou `terminal` dentro dessa pasta
* Copie a [URL](https://github.com/jnicklr/WorkshopFabrica.git) do repositório
* Digite `git clone <URL copiada>` e pressione `enter`

### **3. Crie um ambiente virtual:**

* Abra o terminal do seu editor de código e digite `python -m venv "nome-da-venv"`
* Ative o seu ambiente virtual `nome-da-venv\Scripts\activate` (Windows)
* Ative o seu ambiente virtual `source nome-da-venv/bin/activate` (Unix/MacOS)
* Caso você não consiga ativar, primeiro permita os scripts de serem executados no projeto, digite no terminal `Set-executionPolicy -Scope Process -ExecutionPolicy Bypass`, depois tente ativar novamente.

### **4. Instale os requisitos do projeto pelo terminal:**

* Abra o terminal do seu editor de código e digite `pip install -r requirements.txt`

### **5. Configutre seu banco de dados e depois faça as migrações:**
* Digite `python manage.py migrate`

### **6. Execute o programa pelo terminal:**
* Digite `python manage.py runserver`

## Sobre as APIs e como acessá-las:

Você pode acessar a API colocando no final da URL (após iniciar o servidor) alguma das rotas que deixei listadas a baixo, como exemplo `http://127.0.0.1:8000/aluno/` que vai dar acesso a API de aluno. Através da URL é possível realizar todos os métodos HTTP como: GET, POST, PUT e DELETE. Para realizer os métodos PUT e DELETE é necessário indicar ao final da URL o indíce/id do dado a ser manipulado, `http://127.0.0.1:8000/aluno/1/`. Os aplicativos possuem uma paginação para defininir a quantidade de dados que irão aparecer na página, caso queira mudar isso basta colocar o limite desejável ao final da URL do jeito que irei mostrar `http://127.0.0.1:8000/aluno/?limite=x` no qual x indica quantos podem aparecer. Além disso temos o `http://127.0.0.1:8000/aluno/?offset=x`, o número que colocarmos no x vai indicar a partir de qual elemento vai começar a exibir os dados.

**Rotas APIs:**
* `/professor/`
* `/materia/`
* `/conteudo/`
* `/curso/`
* `/aluno/`
* `/matricula/` 

**Relacionamento das Entidades:**

![image](https://github.com/jnicklr/WorkshopFabrica/assets/102833896/4b0ab933-d76e-45d9-be74-3c01d2a2b93e)
