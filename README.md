# ChatgptAPI
Consumo da API do ChatGPT para analise de sentimentos baseado em feedback.


Este script adota uma abordagem Orientada a Objetos (OO) para calcular o NPS a partir de feedback de usuários.
Duas classes são definidas, onde:
- Feedback representa um único feedback de usuário;
- AnalisadorFeedback é usado para calcular o NPS a partir de uma lista de Feedbacks.
A POO fornece uma abstração mais clara dos dados e comportamentos envolvidos no cálculo do NPS.

Possui uma função para criar um gráfico usando "matplotlib" para visualizar o NPS que calculamos

# Para integrar com o ChatGPT e usá-lo
Documentação Oficial da API OpenAI: https://platform.openai.com/docs/api-reference/introduction
Informações sobre o Período Gratuito: https://help.openai.com/en/articles/4936830

#Para gerar uma API Key:
1. Crie uma conta na OpenAI
2. Acesse a seção "API Keys"
3. Clique em "Create API Key"
Link direto: https://platform.openai.com/account/api-keys

Substitua o texto TODO por sua API Key da OpenAI, ela será salva como uma variável de ambiente.
openai_api_key = 'TODO'

#Seguem alguns links úteis:
1. Endpoint que vamos consumir: https://platform.openai.com/docs/api-reference/chat/create
2. Collection Postman da OpenAI: https://www.postman.com/devrel/workspace/openai/documentation/13183464-90abb798-cb85-43cb-ba3a-ae7941e968da
