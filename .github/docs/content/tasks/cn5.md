# Desafio Agentes de IA (Nível 5)

> Retornar ao [README.md](../../../../README.md)
>
> Acesso ao [conteúdo das aulas](../n5.md)

## Descrição

O objetivo deste desafio é criar um sistema automatizado que gere **roteiros** para vídeos no segmento de videogames. Com base no roteiro, o sistema também deve produzir **três opções de thumbnails** inspiradas no conteúdo do vídeo e escolher uma dessas thumbnails. Para isso, recomendamos a biblioteca **Crew AI**, que permite a colaboração de múltiplos agentes com diferentes funções.

## 🛠 Estrutura do Projeto

### 👨‍💻 Agentes

1. **Roteirista de Vídeo**
    - Responsável por pesquisar e elaborar um **roteiro detalhado para um vídeo completo** no YouTube.
    - Possui acesso a ferramentas de pesquisa para enriquecer seu conhecimento.
    - Especialista em **criação de conteúdo e storytelling** para vídeos de games.
2. **Criador de Thumbnail**
    - Utiliza o roteiro gerado para produzir **três opções de thumbnails**.
    - As thumbnails devem ser inspiradas no **conteúdo do vídeo**, destacando elementos visuais atrativos.
    - Designer gráfico com experiência em **thumbnails chamativas para YouTube**.
3. **Revisor**
    - Revisar o texto do roteiro
    - Escrever a versão contendo roteiro + thumbnails

## 🚀 Execução

O sistema pode ser acionado fornecendo um **tema de vídeo**, como por exemplo:

```python
inputs={'query': 'Melhores jogos de 2020'}

```

[Resolução](https://www.notion.so/Resolu-o-1a8395da57708181b143e646ef6138e3?pvs=21)
