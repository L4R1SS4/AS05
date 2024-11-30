# AS05 - Assistente Conversacional

Este projeto implementa um assistente conversacional que responde perguntas baseadas no conteúdo de documentos enviados. Utiliza o modelo **multi-qa-MiniLM-L6-cos-v1** para processar textos, gerar embeddings, e encontrar os trechos mais relevantes como resposta. O modelo dispensa o uso de chaves de API ou custos financeiros, funcionando localmente.

### Instruções para execução local

0. Criação e inicialização de ambiente virtual no Linux (opcional)

   ```
   python3 -m venv as05
   source as05/bin/activate
   ```

1. Instale as bibliotecas

   ```
   $ pip install -r requirements.txt
   ```

2. Execute o programa

   ```
   $ streamlit run streamlit_app.py
   ```

Nome: Larissa Valadares Silqueira

Link: [https://as05-larissa.streamlit.app/](https://as05-larissa.streamlit.app/)
