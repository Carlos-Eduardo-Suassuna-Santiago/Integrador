# Sistema de Gerenciamento de Biblioteca Online (SGBO)

## Visão Geral:

O Sistema de Gerenciamento de Biblioteca Online (SGBO) é um projeto desenvolvido para proporcionar uma gestão eficiente do cadastro, empréstimo e devolução de livros em uma biblioteca. Este sistema foi projetado para atender às necessidades específicas do Programa Nacional do Livro Didático (PNLD), abrangendo todas as operações relacionadas aos livros desse programa.

## Funcionalidades Principais:

1. **Autenticação e Autorização:**
   - Foco na emissão de livros, registros e visão completa dos alunos cadastrados.
   
2. **Administração da Coleção:**
   - Inserção e gestão de informações sobre os livros, incluindo título, autor, ISBN e categoria.

3. **Controle de Empréstimo e Devolução:**
   - Gerenciamento abrangente de todo o processo de empréstimo, desde a solicitação até a devolução.

4. **Restrições de Acesso:**
   - Implementação de restrições de acesso para garantir a segurança e a integridade dos dados.

## Requisitos Funcionais:

- **Autenticação de Usuários:** O sistema deve permitir que usuários se autentiquem para acessar as funcionalidades específicas.
- **Administração de Livros:** Cadastro, atualização e exclusão de informações sobre livros.
- **Controle de Empréstimo:** Registro de empréstimos de livros para os alunos cadastrados.
- **Devolução de Livros:** Registro e controle do processo de devolução de livros.

## Requisitos Não Funcionais:

1. **Compatibilidade:**
   - O sistema deve ser compatível com os principais navegadores web.
   
2. **Responsividade:**
   - A interface do sistema deve se adaptar a diferentes dispositivos, proporcionando uma experiência consistente.

3. **Usabilidade:**
   - O sistema deve ser intuitivo e de fácil utilização, garantindo uma curva de aprendizado mínima para os usuários.

4. **Tecnologia Django:**
   - O SGBO é desenvolvido utilizando a tecnologia Django, garantindo robustez, segurança e escalabilidade.

## Como Executar o Projeto:

1. **Instalação das Dependências:**
   - Certifique-se de ter o Python e o Django instalados.
   - Execute `pip install -r requirements.txt` para instalar as dependências.

2. **Configuração do Banco de Dados:**
   - Execute `python manage.py migrate` para aplicar as migrações.

3. **Iniciar o Servidor:**
   - Execute `python manage.py runserver` para iniciar o servidor local.

4. **Acesso ao Sistema:**
   - Abra o navegador e acesse [http://localhost:8000](http://localhost:8000) para utilizar o SGBO.

## Contribuições:

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

## Autores:

- Carlos Eduardo Suassuna 
- Gustavo Alves Pimenta 

---

