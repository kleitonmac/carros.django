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

No seu código Python, utilize o dotenv para carregar a chave:

python
Copiar
Editar
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
Pronto! Agora você pode chamar a API da OpenAI para processar requisições com IA.

💻 Como rodar o projeto localmente
1. Clone o repositório
bash
Copiar
Editar
git clone https://github.com/kleitonmac/carros-dev.git
cd carros-dev
2. Crie um ambiente virtual
bash
Copiar
Editar
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Configure o ambiente
Crie um arquivo .env com suas variáveis (como a chave da OpenAI).

5. Execute as migrações
bash
Copiar
Editar
python manage.py migrate
6. Inicie o servidor de desenvolvimento
bash
Copiar
Editar
python manage.py runserver
Acesse http://127.0.0.1:8000 no navegador para ver o projeto em funcionamento.

🚀 Em desenvolvimento
Área administrativa personalizada

Melhorias no sistema de financiamento

Dashboard de vendas

Login com autenticação social (Google, Facebook)

📫 Contato
Caso tenha dúvidas, sugestões ou queira colaborar com o projeto, entre em contato comigo:

GitHub: kleitonmac

Email: seuemail@exemplo.com

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

yaml
Copiar
Editar

---

Se quiser, posso gerar esse arquivo para você em `.md` ou adicionar instruções para incluir um badge, imagem, ou GIF demonstrando o sistema. Deseja algum desses extras?
