🛒 E-Shop Brasil — Banco de Dados NoSQL e Big Data
Repositório oficial do projeto prático desenvolvido para a disciplina de Advanced Databases and Big Data da UniFECAF. O projeto simula a infraestrutura de uma gigante do e-commerce ("E-Shop Brasil") capaz de processar 100 mil pedidos diários para uma base de 5 milhões de clientes, utilizando armazenamento NoSQL em documentos orientados a JSON, arquitetura omnichannel, rastreio logístico e conformidade com a LGPD.

🚀 Arquitetura Tecnológica
Banco de Dados: MongoDB (executado de forma isolada via contentor Docker).

Backend & Interface: Python com Streamlit para o dashboard analítico em tempo real.

Manipulação de Dados: Pandas e Pymongo.

Orquestração: Docker Compose.

⚙️ Guia de Instalação e Execução Local
Siga os passos abaixo para configurar e executar o ambiente completo no seu computador:

1. Pré-requisitos
Ter o Docker Desktop instalado e a executar.

Ter o Python instalado com o gestor de pacotes pip.

2. Clonar ou descarregar o repositório
Abra o terminal na pasta raiz do projeto (eshop-brasil-bigdata).

3. Iniciar o MongoDB via Docker
Execute o seguinte comando no terminal:
docker-compose up -d

4. Instalar as dependências do Python
Execute o seguinte comando no terminal:
python -m pip install -r requirements.txt

5. Executar a Aplicação Streamlit
Execute o seguinte comando no terminal:
python -m streamlit run app.py
O navegador abrirá automaticamente no endereço http://localhost:8501.

📊 Evidências de Funcionamento (Capturas de Ecrã)
O projeto conta com um conjunto de ecrãs funcionais validados:

Dashboard & Métricas em Tempo Real:

Gerador de Carga / Simulação de Pedidos Massivos:

🔒 Conformidade com a LGPD
A aplicação implementa funcionalidades simuladas para atender aos requisitos legais de proteção de dados, incluindo o direito ao esquecimento e a anonimização de registos de clientes diretamente na base NoSQL.

Autor: Pablo (UniFECAF)