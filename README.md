# AS05 - Assistente Conversacional

Este projeto implementa um assistente conversacional que responde perguntas baseadas no conteúdo de documentos enviados. Utiliza o modelo **multi-qa-MiniLM-L6-cos-v1** para processar textos, gerar embeddings, e encontrar os trechos mais relevantes como resposta. O modelo dispensa o uso de chaves de API ou custos financeiros, funcionando localmente.

Link: [https://as05-larissa.streamlit.app/](https://as05-larissa.streamlit.app/)

### Instruções para execução local

0. Criação e inicialização de ambiente virtual no Linux (opcional)

   ```
   python3 -m venv as05
   ```
   ```
   source as05/bin/activate
   ```

1. Entre na pasta do projeto

   ```
   cd AS05
   ```

2. Instale as bibliotecas

   ```
   pip install -r requirements.txt
   ```

3. Execute o programa

   ```
   streamlit run streamlit_app.py
   ```

### Captura de Tela do Programa em Funcionamento

<img src="/Exemplo/captura.png" alt="Captura de Tela" />

Nome: Larissa Valadares Silqueira
