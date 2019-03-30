## O que é git?

Git é um sistema de versionamento de arquivos. Foi criado por Linus Tovald antes da criação do Kernel do Linux.
Linus viu a necessidade de controlar as versões de seus arquivos que eram distribuídos entre várias pessoas.

Para realizar esse versionamento o Git utiliza uma forma de snapshots(fotos) dos arquivos e assim calcula a diferença entre uma versão antiga e uma versão nova.

Geralmente as funções do git são locais, ou seja, não é necessário a conectividade com a Internet para utilizá-lo.

Para mais informações, clique [aqui](https://git-scm.com/book/pt-br/v1/Primeiros-passos-No%C3%A7%C3%B5es-B%C3%A1sicas-de-Git)

## Como instalar o git no Windows

Git é uma ferramenta nativa do Linux, por isso, está presente nativamente nas distribuições GNU/Linux e MacOS.

Para o Windows, necessitamos de um instalador externo:

Acesse o site oficial e [baixe a versão do Windows](https://git-scm.com/downloads)

Para ver o processo de instalação, veja [esse video](https://www.youtube.com/watch?v=SmbAn2_5uGs)

Caso queira ver uma playlist para treinar suas habilidades com git, clique [aqui](https://www.youtube.com/watch?v=BCQHnlnPusY)

## Comandos básicos de git

1. git init

```git
git init
```
init é um comando para inicializar o git em alguma pasta do seu sistema operacional. Esse comando é essencial para qualquer versionamento usando git, é o primeiro comando que deve ser rodado.

2. git remote

```git
git remote
```

remote é um comando para acessarmos uma pasta remota ao nosso computador, como no github, por exemplo. Apesar do git ser local, ele pode ser usado com plataformas web, como o Github ou Gitlab

3. git add

```git
git add
```

add é um comando para adicionar as mudanas nos arquivos ao buffer de versionamento do git. O add é necessário ao efetuar uma mudanças

4. git commit

```git
git commit
```

commit é o comando para efetuar as mudanças no código, ele vai salvar o snapshot dos arquivos. É **obrigatório** o uso de mensagens ao commitar um código. Você **deve** identificar sobre o quê se trata a alteração.

5. git push

```
git push
```

Um dos comandos que acessa um repositório remoto e faz o upload dos arquivos para a plataforma web.

## Preparando o ambiente com Python, pip e Jupyter

Caso ainda não tenha a versão do Python, baixe [aqui](https://www.python.org/downloads/windows/)

Insale o Python inclusive no Path. Para verificar se isso foi feito, abra o CMD e digite:

```
python3
```

Isso deve abrir o shell do Python, e você deve ser capaz de começar a programar. Para sair do shell, digite:

```
exit()
```

Para verificar a versão do seu Python:

```
python3 -v
```

Agora, veja se o pip está instalado com o seu Python. Pip é um sistema de packaging para o Python.

```
pip3 -V
```

Agora vamos instalar tudo que precisaremos, mesmo que não usaremos hoje, já vamos deixar tudo instalado:

Abra o CMD como Administrador

```
pip3 install pandas
pip3 install matplotlib
pip3 install jupyter-notebook
```

Pandas é uma ferramenta para tratar dados em tabelas.
Matplotlib é para plotar gráficos
		Jupyter Notebook é o nosso ambiente de desenvolvimento.


