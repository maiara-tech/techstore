# Documentação do Projeto - TechStore

## Tecnologias Utilizadas
O projeto **TechStore** é um sistema de gerenciamento de produtos para uma loja virtual, desenvolvido com as seguintes tecnologias:

- **Linguagem de Programação:** Python
- **Framework Web:** Django
- **Banco de Dados:** SQLite (padrão), mas pode ser alterado para PostgreSQL ou MySQL
- **Front-end:** HTML, CSS, Bootstrap
- **Gráficos e Visualização de Dados:** Chart.js
- **Ambiente de Desenvolvimento:** PyCharm

---

## Como Executar o Projeto
### 1. Clonar o Repositório
```sh
    git clone https://github.com/seu-repositorio.git
    cd techstore
```

### 2. Criar um Ambiente Virtual
Crie e ative um ambiente virtual Python:
```sh
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
```

### 3. Instalar os Arquivos necessários
```sh
    pip install -r requirements.txt
```

### 4. Aplicar Migrações ao Banco de Dados
```sh
    python manage.py migrate
```

### 5. Criar um Superusuário
```sh
    python manage.py createsuperuser
```

### 6. Executar o Servidor Local
Inicie o servidor do Django:
```sh
    python manage.py runserver
```
Acesse o sistema no navegador: **http://127.0.0.1:8000/**

---

## Funcionalidades do Sistema
- **CRUD de Produtos**: Cadastro, edição, listagem e remoção de produtos.
- **Dashboard**: Exibe relatórios e gráficos dinâmicos sobre produtos, estoque e vendas.
- **Autenticação**: Permite login e gerenciamento de usuários.
- **Interface Responsiva**: Design adaptável para dispositivos móveis.

---

## Possíveis Melhorias Futuras
- Integração com um gateway de pagamento.
- Implementação de API REST para acesso externo.
- Mais opções de gráficos. 
- Suporte a múltiplos idiomas.
- Imagens dos produtos
- Vendas pelo site

**Dúvidas ou sugestões? Entre em contato!**

**Para adicionar produtos ou editar e excluir**
usuário - admin
senha - 12345678
