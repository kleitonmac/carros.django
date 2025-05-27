🚗 Concessionária Web
Bem-vindo(a) ao repositório da Concessionária Web , um projeto pessoal desenvolvido para simular um site moderno e funcional de uma entrega de veículos. Este projeto faz parte do meu portfólio e tem como objetivo demonstrar minhas habilidades com desenvolvimento web, design responsivo e integração com APIs modernas, como a da OpenAI.

🛠️ Tecnologias Utilizadas
Front-end:

HTML5
CSS3
JavaScript
Django (Modelos)
Backend:

Pitão
Django
Banco de Dados:

SQLite (padrão, simples de configurar localmente)
Integrações:

API OpenAI (para recursos com inteligência artificial)
✅ Funcionalidades
Página inicial com destaques e promoções de veículos
Lista de veículos com filtros por categoria, marca e faixa de preço
Página detalhada para cada veículo
Formulário de contato e simulação de financiamento
Área administrativa (em desenvolvimento)
Design totalmente responsivo, adaptado para dispositivos móveis
CRUD completo de veículos com autenticação
Uso de sinais do Django para lógica de banco de dados
Integração com OpenAI API para recursos inteligentes:
Chatbot para tirar dúvidas
Sugestões de veículos conforme o perfil do usuário
Explicações automáticas sobre modelos, financiamento e processos
🤖 Integração com OpenAI
A IA é utilizada no projeto para melhorar a experiência do usuário por meio de respostas inteligentes e automatizadas.

Como configurar a chave do OpenAI
Crie uma conta em: https://platform.openai.com
Gere uma chave de API e aba API Keys
Crie um arquivo .envna raiz do projeto com o seguinte conteúdo:
OPENAI_API_KEY=sk-sua-chave-aqui
No seu código Python, use o seguinte padrão para carregar a chave:
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
💻 Como rodar o projeto localmente
1. Clonar ou repositório
git clone https://github.com/kleitonmac/carros-dev.git
cd carros-dev
2. Crie um ambiente virtual
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
3. Instalar as dependências
pip install -r requirements.txt
💡 Para visualizar o banco de dados Postgres faça as próximas alterações. BANCO DE DADOS = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'carros', 'USER': 'User_name_Postgres', 'PASSWORD': 'Sua_senha', 'HOST': 'localhost', 'PORT': '5432', } }

4. Configurar o ambiente
Crie um arquivo .envcom sua variável OPENAI_API_KEY.

5. Executar as migrações
python manage.py migrate
6. Iniciar o servidor de desenvolvimento
python manage.py runserver
Acesse o projeto em: http://127.0.0.1:8000/ para iniciar o login e navegar no repositório pelas URLs de new_car, cars.

🔽 Instalação rápida (linha direta)
Caso deseje instalar todas as dependências de uma vez, use o comando:

pip install -r .\requirements.txt
🚀 Em desenvolvimento
Área administrativa personalizada
Melhorias no sistema de financiamento
Painel de vendas
Login com autenticação social (Google, Facebook)
📫 Contato
Caso tenha dúvidas, sugestões ou queira colaborar com o projeto, entre em contato comigo:

GitHub: kleitonmac
E-mail: kdevprofissional@gmail.com
📝 Licença
Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.