# Desafio Otimizando LLMs com Fine Tuning (Nível 4)

> Retornar ao [README.md](../../../../README.md)
>
> Acesso ao [conteúdo das aulas](../n4.md)

## Contexto

Uma grande rede varejista que vende produtos domésticos deseja melhorar o atendimento ao cliente automatizando a classificação das mensagens enviadas ao seu Bot de Atendimento. Para isso, você deve realizar o fine-tuning de um **modelo de linguagem (SLM)**, como **BERT ou outro de sua preferência**, utilizando os datasets fornecidos.

## Objetivo

Seu desafio é treinar um modelo capaz de classificar mensagens de clientes em **duas categorias**:

- **"venda"**: Quando a mensagem está relacionada à intenção de compra de um produto.
- **"suporte"**: Quando a mensagem está relacionada a dúvidas ou problemas com um produto.

## Dados

Você utilizará dois arquivos JSONL contendo exemplos reais de mensagens de clientes:

- **treino.jsonl**: Conjunto maior para um treinamento mais robusto.
- **teste.jsonl**: Conjunto menor, útil para testes rápidos ou validação.

`{"prompt": "Olá, gostaria de fazer a aquisição do novo produto", "completion": "venda"}
{"prompt": "tudo bom, queria verificar como funciona a TV Smart x0912", "completion": "suporte"}`

*obs: O banco de dados fornecido foi gerado de forma **sintética**, exclusivamente para este desafio. Ele não representa interações reais de clientes, sendo idealizado apenas para fins didáticos e de desenvolvimento.*

### Arquivos a serem utilizados

[treino.jsonl](../../../../n4/task/data/treino.jsonl)

[teste.jsonl](../../../../n4/task/data/teste.jsonl)

## Recomendação de Ambiente

Para facilitar a execução do desafio, **recomenda-se utilizar o Google Colab**. Ele oferece um ambiente pronto para machine learning, com suporte a GPUs gratuitas e integração com bibliotecas como **Hugging Face Transformers, TensorFlow e PyTorch**. Além disso, o Google Colab permite carregar diretamente os datasets e compartilhar notebooks facilmente.

## Solução

Nós disponibilizamos também uma possível solução para esse desafio. Porém, tente se desafiar e resolver o exercício antes de olhar a solução.

[Resolução](https://www.notion.so/Resolu-o-195395da5770819a8890ee2fd8411f7f?pvs=21)
