# 🚗 Concessionária Web

Bem-vindo(a) ao repositório da **Concessionária Web**, um projeto pessoal desenvolvido para simular um site moderno e funcional de uma concessionária de veículos. Este projeto faz parte do meu portfólio e tem como objetivo demonstrar minhas habilidades com desenvolvimento web, design responsivo e integração com APIs modernas, como a da OpenAI.

---

## 🛠️ Tecnologias Utilizadas

**Frontend:**
- HTML5  
- CSS3  
- JavaScript  
- Django (Templates)

**Backend:**
- Python  
- Django

**Banco de Dados:**
- SQLite (padrão, simples de configurar localmente)

**Integrações:**
- OpenAI API (para recursos com inteligência artificial)

---

## ✅ Funcionalidades

- Página inicial com destaques e promoções de veículos  
- Lista de veículos com filtros por categoria, marca e faixa de preço  
- Página detalhada para cada veículo  
- Formulário de contato e simulação de financiamento  
- Área administrativa (em desenvolvimento)  
- Design totalmente responsivo, adaptado para dispositivos móveis  
- CRUD completo de veículos com autenticação  
- Uso de **signals** do Django para lógica de banco de dados  
- Integração com **OpenAI API** para recursos inteligentes:
  - Chatbot para tirar dúvidas
  - Sugestões de veículos conforme o perfil do usuário
  - Explicações automáticas sobre modelos, financiamento e processos

---

## 🤖 Integração com OpenAI

A IA é utilizada no projeto para melhorar a experiência do usuário por meio de respostas inteligentes e automatizadas.

### Como configurar a chave da OpenAI

1. Crie uma conta em: [https://platform.openai.com](https://platform.openai.com)
2. Gere uma **API Key** na aba **API Keys**
3. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
```

4. No seu código Python, use o seguinte padrão para carregar a chave:

```python
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
```

---

## 💻 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/kleitonmac/carros-dev.git
cd carros-dev
```

### 2. Crie um ambiente virtual

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Se ainda não estiver no `requirements.txt`, instale também:

```bash
pip install django
pip install pillow
pip install python-dotenv
```

> 💡 Para visualizar o banco de dados SQLite de forma amigável, recomendamos a extensão gratuita do VS Code: **SQLite Viewer**.

### 4. Configure o ambiente

Crie um arquivo `.env` com sua variável `OPENAI_API_KEY`.

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Inicie o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse o projeto em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/login) para iniciar o login e navegar no repositorios pelas urls de new_car , cars,

---

## 🚀 Em desenvolvimento

- Área administrativa personalizada  
- Melhorias no sistema de financiamento  
- Dashboard de vendas  
- Login com autenticação social (Google, Facebook)

---

## 📫 Contato

Caso tenha dúvidas, sugestões ou queira colaborar com o projeto, entre em contato comigo:

- GitHub: [kleitonmac](https://github.com/kleitonmac)
- Email: seuemail@exemplo.com

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.