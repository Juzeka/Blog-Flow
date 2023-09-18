
# Teste para vaga back-end

Uma API simples de um MVP (Minimum Viable Product) para um Blog Flow a qual permite criar, visualizar, editar e excluir artigos em um blog e dentre outras funcionalidades basicas.

Credenciais pré-existente: username: admin e password: admin
- [**Acesse aqui**](https://blog-flow-production.up.railway.app/)

## Visualização com Swagger
![Visualização](https://github.com/Juzeka/Blog-Flow/blob/master/visualization.png?raw=true)

## Funcionalidades

- Login de conta
- Atualização do Token de Login
- Listagem de Categorias
- Criação de Categorias
- Listagem de Artigos
- Criação de Artigos
- Detalhe de Artigo
- Deleção de Artigo
- Publicação de Artigo
- Criação de Comentários
- Edição de Comentários
- Deleção de Comentários
- Criação de Conta


## Endpoints
Descrição dos endpoints, parâmetros e suas possíveis respostas para o usuário.

#### *Respostas padrões relacionada a autenticação*
```http
  401 -> {"detail": "As credenciais de autenticação não foram fornecidas."}
  401 -> {
    "detail": "O token informado não é válido para qualquer tipo de token",
    "code": "token_not_valid",
    "messages": [
      {
        "token_class": "AccessToken",
        "token_type": "access",
        "message": "O token é inválido ou expirado"
      }
    ]
  }
  401 -> {
    "detail": "Usuário não encontrado",
    "code": "user_not_found"
  }
````

#### *Nova Conta.*

```http
  POST /api/v1/accounts/
```

Parâmetros do corpo da requisição:

| Parâmetro   | Tipo       | Descrição                           | Opções
| :---------- | :--------- | :---------------------------------- | :---------- |
| `username` | `string` | Usuário* | -|
| `password` | `string` | Senha* | -|
| `first_name` | `string` | Nome* | -|
| `last_name` | `string` | Sobrenome | -|
| `email` | `string` | E-mail | -|
| `type` | `string` | Tipo da conta* | author ou user|

Possíveis respostas:
```http
  201 -> {"detail": "Conta criada com sucesso."}
  400 -> {"name_field": ["Este campo é obrigatório."]}
    Ex.: {"type": ["Este campo é obrigatório."]}
```
#### *Login*

```http
  POST /api/v1/accounts/auth/token/
```

Parâmetros do corpo da requisição:

| Parâmetro   | Tipo       | Descrição                           | Opções
| :---------- | :--------- | :---------------------------------- | :---------- |
| `username` | `string` | Usuário* | -|
| `password` | `string` | Senha* | -|

Possíveis respostas:
```http
  200 -> {"access": "token_access", "refresh": "token_refresh"}
  400 -> {"name_field": ["Este campo é obrigatório."]}
    Ex.: {"username": ["Este campo é obrigatório."]}
  401 -> {"detail": "Usuário e/ou senha incorreto(s)"}
```

#### *Atualizar Token de Acesso*

```http
  POST /api/v1/accounts/auth/token/refresh/
```

Parâmetros do corpo da requisição:


| Parâmetro   | Tipo       | Descrição                           | Opções
| :---------- | :--------- | :---------------------------------- | :---------- |
| `refresh` | `string` | Token de atualização* | -|

Possíveis respostas:
```http
  200 -> {"access": "token_access"}
  400 -> {"name_field": ["Este campo é obrigatório."]}
    Ex.: {"username": ["Este campo é obrigatório."]}
  401 -> {"detail": "Token está na blacklist", "code": "token_not_valid"}
```

#### *Retorna Artigos*

```http
  GET /api/v1/articles/?page=1
```
Requer o token de autorização no cabeçalho: *{"Authorization": "Bearer ..."}*

Parâmetros da URL(QueryParams):

| Parâmetro  | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `page` | `int` | paginação |

Possíveis respostas:
```http
  200 -> {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
      {
        "id": 1,
        "title": "Titulo",
        "subtitle": "Subtitulo",
        "content": "Conteudo",
        "status": "waiting_publication",
        "author": 4,
        "category": 1,
        "keywords": [1],
        "is_visible": false,
        "comments": []
      }
    ]
  }
```

#### *Novo Artigo*

```http
  POST /api/v1/articles/
```
Requer o token de autorização no cabeçalho: *{"Authorization": "Bearer ..."}*

Parâmetros do corpo da requisição:

| Parâmetro  | Tipo       | Descrição                           | Opções | Formato |
| :---------- | :--------- | :---------------------------------- | :---------- | :------ |
| `title` | `string` | Título* | -| - |
| `subtitle` | `string` | Subtítulo* | -| - |
| `content` | `string` | Conteúdo* | -| - |
| `category` | `int` | Categoria* | -| - |
| `keywords` | `array` | Palavras-Chave* | -| [{"name": "value"}, ...] |

Possíveis respostas:
```http
  200 -> {
    "id": 2,
    "category": {
      "id": 1,
      "name": "Teste"
    },
    "keywords": [
      {
        "id": 2,
        "updated_at": "2023-09-17T17:12:06.904864-03:00",
        "created_at": "2023-09-17T17:12:06.904914-03:00",
        "name": "key 1",
        "is_active": true
      }
    ],
    "updated_at": "2023-09-17T17:12:06.910033-03:00",
    "created_at": "2023-09-17T17:12:06.910072-03:00",
    "title": "T",
    "subtitle": "S",
    "content": "C",
    "status": "waiting_publication",
    "is_visible": false,
    "author": 5
  }
  400 -> {"detail": "O campo keywords é obrigatório."}
  400 -> {"detail": "Formato do keyword incorreto, tente: {"name": "value"}"}
  400 -> {"name_field": ["Este campo é obrigatório."]}
    Ex.: {"title": ["Este campo é obrigatório."]}
  403 -> {"detail": "Somente um autor pode criar um artigo."}
```

#### *Retorna Artigo*

```http
  GET /api/v1/articles/:id/
```
Requer o token de autorização no cabeçalho: *{"Authorization": "Bearer ..."}*

Parâmetros do corpo da requisição:

| Parâmetro  | Tipo       | Descrição                           | Opções | Formato |
| :---------- | :--------- | :---------------------------------- | :---------- | :------ |
| `title` | `string` | Título* | -| - |
| `subtitle` | `string` | Subtítulo* | -| - |
| `content` | `string` | Conteúdo* | -| - |
| `category` | `int` | Categoria* | -| - |
| `keywords` | `array` | Palavras-Chave* | -| [{"name": "value"}, ...] |

Possíveis respostas:
```http
  200 -> {
    "id": 3,
    "title": "Titulo",
    "subtitle": "Subtitulo",
    "content": "Conteudo",
    "status": "waiting_publication",
    "author": 5,
    "category": 1,
    "keywords": [2, 1],
    "is_visible": false,
    "comments": []
  }
  404 -> {"detail": "Não encontrado."}
```

#### *Publica Artigo*

```http
  POST /api/v1/articles/:id_article/publish/
```
Requer o token de autorização no cabeçalho: *{"Authorization": "Bearer ..."}*

Parâmetros do corpo da requisição:

| Parâmetro  | Tipo       | Descrição                           | Padrão |
| :---------- | :--------- | :---------------------------------- | :------|
| `is_publish` | `bool` | Publicar? | false

Possíveis respostas:
```http
  200 -> {"detail": "Artigo publicado com sucesso."}
  200 -> {"detail": "Artigo não foi aprovado."}
  404 -> {"detail": "Não encontrado."}
```

#### *Deleta Artigo*

```http
  DELETE /api/v1/articles/:id/
```
Requer o token de autorização no cabeçalho: *{"Authorization": "Bearer ..."}*

Possíveis respostas:
```http
  204 -> -
  404 -> {"detail": "Não encontrado."}
```

#### *Novo Comentário*

```http
  POST /api/v1/articles/:id_article/comments/
```
Requer o token de autorização no cabeçalho: *{"Authorization": "Bearer ..."}*

Parâmetros do corpo da requisição:

| Parâmetro  | Tipo       | Descrição
| :---------- | :--------- | :----------------------------------
| `content` | `string` | Comentário*

Possíveis respostas:
```http
  201 -> {"detail": "Comentário enviado com sucesso, sujeito à aprovação."}
  400 -> {"name_field": ["Este campo é obrigatório."]}
    Ex.: {"content": ["Este campo é obrigatório."]}
  404 -> {"detail": "Não encontrado."}
```

#### *Edita Comentário*

```http
  PATCH /api/v1/articles/:id_article/comments/:id_comment/
```
Requer o token de autorização no cabeçalho: *{"Authorization": "Bearer ..."}*

Parâmetros do corpo da requisição:

| Parâmetro  | Tipo       | Descrição
| :---------- | :--------- | :----------------------------------
| `content` | `string` | Comentário

Possíveis respostas:
```http
  200 -> {
    "id": 2,
    "updated_at": "2023-09-17T17:51:13.476999-03:00",
    "created_at": "2023-09-17T17:35:46.957753-03:00",
    "content": "Conteúdo editado",
    "status": "waiting_approved",
    "user": 7,
    "article": 4
  }
  404 -> {"detail": "Não encontrado."}
```

#### *Deleta Comentário*

```http
  DELETE /api/v1/articles/:id_article/comments/:id_comment/
```
Requer o token de autorização no cabeçalho: *{"Authorization": "Bearer ..."}*

Possíveis respostas:
```http
  204 -> -
```

#### *Retorna Categorias*

```http
  GET /api/v1/categories/?page=1
```
Requer o token de autorização no cabeçalho: *{"Authorization": "Bearer ..."}*

Parâmetros da URL(QueryParams):

| Parâmetro  | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `page` | `int` | paginação |

Possíveis respostas:
```http
  200 -> {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
      {
        "id": 1,
        "updated_at": "2023-09-17T16:52:23.680762-03:00",
        "created_at": "2023-09-17T16:52:23.680804-03:00",
        "name": "Teste",
        "is_active": true
      }
    ]
  }
```

#### *Nova Categoria*

```http
  POST /api/v1/categories/
```
Requer o token de autorização no cabeçalho: *{"Authorization": "Bearer ..."}*

Parâmetros do corpo da requisição:

| Parâmetro   | Tipo     | Descrição
| :---------- | :------- | :--------
| `name`      | `string` | Nome*

Possíveis respostas:
```http
  200 -> {
    "id": 2,
    "updated_at": "2023-09-17T17:51:13.476999-03:00",
    "created_at": "2023-09-17T17:35:46.957753-03:00",
    "content": "Conteúdo editado",
    "status": "waiting_approved",
    "user": 7,
    "article": 4
  }
  400 -> {"name_field": ["Este campo é obrigatório."]}
    Ex.: {"name": ["Este campo é obrigatório."]}
```


## Relacionamento

![Relacionamento](https://github.com/Juzeka/Blog-Flow/blob/master/relationship.png?raw=true)


## Distribuição de pastas

- A aquitetura é baseada na Model-View-Controller(MVC).
- A distribuição é constituida no diretório de cada app e seu fluxo de estruturação de arquivos fica assim: factories, migrations, models, serializes, services e views.
- O diretório tests segue a lógica das apps ex: app_name/views.py, app_name/services.py e etc.

![Pastas](https://github.com/Juzeka/Blog-Flow/blob/master/directories.png?raw=true)

## Dependências extras utilizadas

### Visualização dos endpoints
- [**Swagger (drf-yasg)**](https://pypi.org/project/drf-yasg/)
### Autenticação
- [**Json Web Token (JWT)**](https://pypi.org/project/djangorestframework-simplejwt/)
### API
- [**Django REST Framework**](https://www.django-rest-framework.org/#installation)
- [**Python Decouple**](https://pypi.org/project/python-decouple/)
- [**Celery Beat**](https://pypi.org/project/django-celery-beat/)
- [**Celery Results**](https://pypi.org/project/django-celery-results/)
- [**Cors Headers**](https://pypi.org/project/django-cors-headers/)
### Testes
- [**Parameterized**](https://pypi.org/project/parameterized/)
- [**Django Factory Boy**](https://pypi.org/project/django-factory_boy/)
### Depuração
- [**IPython pdb**](https://pypi.org/project/ipdb/)

###

## Instalação

Para a Instalação execute os seguintes comandos no terminal.

- Clone o projeto em:
```bash
git clone https://github.com/Juzeka/Blog-Flow.git
```
Na pasta do projeto:
- Criação do ambiente virtual:
```bash
python3 -m venv venv
```
- Ativando o ambiente:
```bash
. venv/bin/activate
```

- Instalação das dependências:
```bash
pip install -r requirements.txt
```

### Criação das variáveis de ambiente
Crie um arquivo .env baseado no .env.example na pasta do projeto (onde o arquivo manage.py se encontra) e no terminal execute:

- Execute o comando:
```bash
python3
```

- Entre com:
```bash
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```
com a chave exibida pelo print cole no arquivo .env:
```bash
SECRET_KEY = 'chave gerada aqui!'
DEBUG = True
...
```


## Rodando o server

- Rode as makemigrations:
```bash
python3 manage.py makemigrations
```
- Rode as migrations:
```bash
python3 manage.py migrate
```
- Rode o servidor:
```bash
python3 manage.py runserver
```

## Rodando o celery
Caso deseje usar o celery, certifique-se de configurar as seguites variáveis: USE_CELERY pra True e CELERY_BROKER_URL.

- Rode comando para subir o worker:
```bash
celery -A core worker --loglevel=info
```

## Rodando os testes

Para rodar os testes unitários, rode o seguinte comando:

```bash
  python3 manage.py test tests
```
