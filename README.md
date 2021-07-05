# README - study-python

## 1. Introdução

Este repositório contém os artefatos do laboratório de estudo da linguagem de programação Python 3 **study-python**.


## 2. Documentação

### 2.4. Diagrama de Mapa Mental (Mind Map Diagram)

![MindMapDiagram-Context.png](./doc/mind-maps/MindMapDiagram-Context.png) 


### 2.5. Estratégia de Branches (Branch Strategy Workflow)

Sugestão de [estratégia de branches e workflow](https://github.com/josemarsilva/eval-git#38-estrat%C3%A9gia-de-gerenciamento-de-branches) :
* `master`: pronto para produção
* `develop`: último desenvolvimento pronto para produção


## 3. Projeto

### 3.1. Pré-Requisitos, Pré-Condições e Premissas

#### a. Tecnologias e ferramentas

* Python 3 - Windows ou Linux
* [Google Colab](https://colab.research.google.com/)


#### b. Ferramental de apoio

* Ferramenta: [Draw.IO](https://app.diagrams.net/) (_apoio_: necessário para editar os diagramas UML)
* Pycharm community (_produtividade_: IDE facilita programação)
* venv - administrador de múltiplos ambientes Python para evitar bagunçar as bibliotecas
* [Jupyter Notebook - ambiente de programação e documentação Python na nuvem](https://jupyter.org/try)
* [Colab Research Google - ambiente de programação Python na nuvem](https://colab.research.google.com/)


### 3.2. Guia do Desenvolvedor e Administrador

* Faça um clone do projeto `git clone`. Use o _branch_ `master` se o _branch_ `develop` não estiver disponível
* Leia as documentações disponíves em "2. Documentação"  and "3.x. Design Patterns, Standard, Conventions and Best Practices"


### 3.3. Guia de Implantação, Configuração e Instalação

#### a. Download and Install Python for Windows

* https://www.python.org/downloads/

#### b. Download and Install Pycharm Community

* https://www.jetbrains.com/pycharm/download/#section=linux

#### c. Uso gratuito da Jupyter Notebook (Platform as a Service)

* https://jupyter.org/
  * Clique `Try in your Browser`
  * Clique `Try Classic Notebook`

#### d. Uso gratuito do Google Colabs PaaS (Platform as a Service)

* https://colab.research.google.com/

#### e. Uso gratuito do W3School Python Online Interpreter Demo

* https://www.w3schools.com/python/trypython.asp?filename=demo_default

### 3.5. Guia de Estudo

#### 3.5.1. Básico da linguagem Python

##### [Comments](https://www.w3schools.com/python/python_comments.asp)

* [`lab-01-helloworld-remarks.py`](./src/python/lab-01-helloworld-remarks.py)
* [`lab-02-print-separator-end.py`](./src/python/lab-02-print-separator-end.py)

##### [Datatypes](https://www.w3schools.com/python/python_datatypes.asp)
* [`lab-03-primitive-datatype-string.py`](./src/python/lab-03-primitive-datatype-string.py)
* [`lab-04-primitive-datatype-int-float-bool.py`](./src/python/lab-04-primitive-datatype-int-float-bool.py)

##### [Operators](https://www.w3schools.com/python/python_operators.asp)
* [`lab-05-arithmetics-operator.py`](./src/python/lab-05-arithmetics-operator.py)

##### [Variables](https://www.w3schools.com/python/python_variables.asp) and [Datatypes](https://www.w3schools.com/python/python_datatypes.asp)
* [`lab-06-variables.py`](./src/python/lab-06-variables.py)

##### [String Formatting](https://www.w3schools.com/python/python_string_formatting.asp)
* [`lab-07-formating-string.py`](./src/python/lab-07-formating-string.py)
* [`lab-08-user-input-casting-datatype.py`](./src/python/lab-08-user-input-casting-datatype.py)
* [`lab-16-formatting-values.py`](./src/python/lab-16-formatting-values.py)

##### [If, elif, else](https://www.w3schools.com/python/python_conditions.asp)
* [`lab-09-if-elif-else.py`](./src/python/lab-09-if-elif-else.py)
* [`lab-10-relational-operator.py`](./src/python/lab-10-relational-operator.py)
* [`lab-11-logical-operator.py`](./src/python/lab-11-logical-operator.py)

##### String [methods](https://www.w3schools.com/python/python_ref_string.asp) and index
* [`lab-12-string-functions.py`](./src/python/lab-12-string-functions.py)
* [`lab-17-string-index-slice.py`](./src/python/lab-17-string-index-slice.py)

##### [Python Built-in function](https://www.w3schools.com/python/python_ref_functions.asp)
* [`lab-13-built-in-functions-documentation.py`](./src/python/lab-13-built-in-functions-documentation.py)

##### [try .. except](https://www.w3schools.com/python/python_try_except.asp)
* [`lab-14-try-except.py`](./src/python/lab-14-try-except.py)

##### Loop: [while](https://www.w3schools.com/python/python_while_loops.asp), [for](https://www.w3schools.com/python/python_for_loops.asp), range and [iterators](https://www.w3schools.com/python/python_iterators.asp)
* [`lab-18-while-continue-for.py`](./src/python/lab-18-while-continue-for.py)
* [`lab-19-string-iterator.py`](./src/python/lab-19-string-iterator.py)
* [`lab-20-for-iterator-range.py`](./src/python/lab-20-for-iterator-range.py)
* [`lab-15-pass-ellipsis-placeholders.py`](./src/python/lab-15-pass-ellipsis-placeholders.py)

##### List, index, slice, enumerate, tuples, packing, unpacking, etc
* [`lab-21-lists-index-slice-append-insert-del-clear-extend.py`](./src/python/lab-21-lists-index-slice-append-insert-del-clear-extend.py)
* [`lab-22-list-for-continue-if-else.py`](./src/python/lab-22-list-for-continue-if-else.py)
* [`lab-23-split-join-enumerate-tuples-unpackage.py`](./src/python/lab-23-split-join-enumerate-tuples-unpackage.py)
* [`lab-24-list-of-list-tuples-enumerate.py`](./src/python/lab-24-list-of-list-tuples-enumerate.py)
* [`lab-25-lists-unpacking.py`](./src/python/lab-25-lists-unpacking.py)

##### Others basic
* [`lab-26-swap-value-between-2-variables.py`](./src/python/lab-26-swap-value-between-2-variables.py)
* [`lab-27-conditional-expression-ternary-operation.py`](./src/python/lab-27-conditional-expression-ternary-operation.py)


#### 3.5.2. Intermediário da linguagem Python

##### [Functions](https://www.w3schools.com/python/python_functions.asp)
* [`lab-101-def-function-create-use-arguments-default-return.py`](./src/python/lab-101-def-function-create-use-arguments-default-return.py)
* [`lab-102-def-return-no-return-function-return.py`](./src/python/lab-102-def-return-no-return-function-return.py)
* [`lab-103-def-return-list-tuple.py`](./src/python/lab-103-def-return-list-tuple.py)
* [`lab-104-def-functions-args-kwargs.py`](./src/python/lab-104-def-functions-args-kwargs.py)
* [`lab-105-variable-scopes-global-function-local.py`](./src/python/lab-105-variable-scopes-global-function-local.py)

##### [Lambda](https://www.w3schools.com/python/python_lambda.asp)
* [`lab-106-lambda-expression-anonymous-function.py`](./src/python/lab-106-lambda-expression-anonymous-function.py)

#### [Tuples](https://www.w3schools.com/python/python_tuples.asp)
* [`lab-107-tuple-vs-list.py`](./src/python/lab-107-tuple-vs-list.py)

##### [Dictionary](https://www.w3schools.com/python/python_dictionaries.asp)
* [`lab-108-dictionary.py`](./src/python/lab-108-dictionary.py)
* [`lab-111-dictionary-set-comprehension.py`](./src/python/lab-111-dictionary-set-comprehension.py)

##### [Set](https://www.w3schools.com/python/python_sets.asp)
* [`lab-109-set-add-update-clear-discard-union-intersection-difference.py`](./src/python/lab-109-set-add-update-clear-discard-union-intersection-difference.py)

##### [List](https://www.w3schools.com/python/python_lists.asp)
* [`lab-110-list-comprehension.py`](./src/python/lab-110-list-comprehension.py)

##### Iterable, iterator, generator, groupby, map, filter, reduce
* [`lab-112-iterable-iterator-generator-yield.py`](./src/python/lab-112-iterable-iterator-generator-yield.py)
* [`lab-114-iterable-zip-itertools-zip-longest.py`](./src/python/lab-114-iterable-zip-itertools-zip-longest.py)
* [`lab-115-itertools-combinations-permutations-products.py`](./src/python/lab-115-itertools-combinations-permutations-products.py)
* [`lab-116-groupby.py`](./src/python/lab-116-groupby.py)
* [`lab-117-map-data.py`](./src/python/lab-117-map-data.py)
* [`lab-118-map-lambda-function-as-parameter.py`](./src/python/lab-118-map-lambda-function-as-parameter.py)
* [`lab-119-filter-lambda-function-as-parameter.py`](./src/python/lab-119-filter-lambda-function-as-parameter.py)
* [`lab-120-reduce-lambda-function-as-parameter.py`](./src/python/lab-120-reduce-lambda-function-as-parameter.py)
* [`lab-121-exception-handling-try-except-raise-exception.py`](./src/python/lab-121-exception-handling-try-except-raise-exception.py)


##### [Module](https://www.w3schools.com/python/python_modules.asp)
* [`lab-113-module-datetime-math-random-sys-time.py`](./src/python/lab-113-module-datetime-math-random-sys-time.py)
* [`lab-122-module-import-library-usercustom-pip-install-venv-activate.py`](./src/python/lab-122-module-import-library-usercustom-pip-install-venv-activate.py)
  * [`moduleusercustom.py`](./src/python/moduleusercustom.py)
* [`lab-123-package-usercustom.py`](./src/python/lab-123-package-usercustom.py)
  * [`usercustompackage`](./src/python/usercustompackage)
    * [`__init__.py`](./src/python/usercustompackage/__init__.py)
    * [`calculate.py`](./src/python/usercustompackage/calculate.py)
    * [`subpackage`](./src/python/usercustompackage/subpackage)
      * [`__init__.py`](./src/python/usercustompackage/subpackage/__init__.py)
      * [`fmt.py`](./src/python/usercustompackage/subpackage/fmt.py)
* [`lab-124-file-open-write-read-seek-with-close.py`](./src/python/lab-124-file-open-write-read-seek-with-close.py)
* [`lab-125-json-write-to-read-from-file.py`](./src/python/lab-125-json-write-to-read-from-file.py)
* [`lab-126-file-read-write-csv-tsv-comma-positional-utf7-utf8-unicode.py`](./src/python/lab-126-file-read-write-csv-tsv-comma-positional-utf7-utf8-unicode.py)


#### 3.5.3. Avançado da linguagem Python

##### 3.5.3.1. Python language advanced issues

* [`lab-201-package-module-relative-reference-sys-path.py`](src/python/lab-201-package-module-relative-reference-sys-path.py)
  * [`package1`](./src/python/package1):  [`module1`](./src/python/package1/module1.py),  [`module2`](./src/python/package1/module1.py)
  * [`package2`](./src/python/package2): [`module1`](./src/python/package2/module1.py)
  * [`package3`](./src/python/package3): [`subpackage31`](./src/python/package3/subpackage31), [`module1`](./src/python/package3/subpackage31/module1.py)
* [`lab-202-decorators.py`](src/python/lab-202-decorators.py)
* [`lab-203-solving-mutable-arguments-function.py`](src/python/lab-203-solving-mutable-arguments-function.py)

##### 3.5.3.2. Python & AI - Artificial Intelligence

##### 3.5.3.2.1 Dataset
**Dataset** é o conjunto que possibilita o treinamento e validação do modelo de _ML_. Na internet há uma infinidade de sites que disponibilizam informações que podem ser processadas como Dataset:

* https://simple.nama.ai/post/uma-lista-com-15-datasets-interessantes-que-vimos-por-ai
* https://archive.ics.uci.edu/ml/datasets.php
* https://www.kaggle.com/datasets
* https://developer.ibm.com/technologies/artificial-intelligence/data/

##### 3.5.3.2.2 Numpy

##### 3.5.3.2.3 Pandas

##### 3.5.3.2.4 Matplotlib

##### 3.5.3.2.5 Seaborn

#### 3.5.4. Exercício de aproveitamento

##### 3.5.3.1. Exercício 01: Programa Python para calcular os dois valores de uma equação do 2o grau por Bhaskara

* Requisitos de negócio:
  * https://mundoeducacao.uol.com.br/matematica/formula-bhaskara.htm
* Requisitos técnico funcional:
  * Faça um programa Python para calcular uma equação do 2o grau pelo método de Bhaskara
  * O programa deve pedir como entrada cada um dos valores: `a`, `b` e `c`
  * O programa deve consistir os valores de entradas e apresentar mensagens de erros específicas
  * O programa deve calcular e apresentar o valor de _Delta_
  * O programa deve dizer se a equação tem solução, calcular e apresentar os dois valores da equação: `x1` e `x2`
* Requisitos técnico não funcional:
  * O programa deve ter pelo menos uma função
  * O programa deve funcionar como um módulo, isto é se executado diretamente deve pedir as variáveis de entrada, porém se carregado por outro programa pode ser chamado por uma função `bhaskara(a,b,c)` 
  * O programa deverá fazer uso dos seguintes recursos de programação em linguagem Python:
    * variables, datatypes(integer, float, string), operations (+, -, *, /), user input, format (integers numbers, float always 3 decimal place), casting, operators (if, then, else, else if), exception manipulation (try, catch), define functions, module import


##### 3.5.3.2. Exercício 02: Programa Python para apresentar as 10 palavras que mais aparecem em um texto

* Requisitos de negócio:
  * Programa que leia o texto de um arquivo e apresente um resumo das top 10 palavras mais utilizadas no texto e as linhas correspondentes onde a palavara apareceu
* Requisitos técnico funcional:
  * Faça um programa Python para identificar e apresentar como saída as top 10 palavras utilizadas no texto
  * O texto encontra-se nos arquivos anexos `file-06-trecho-livro-filosofia` e `file-07-trecho-livro-literatura`
  * As palavras compostas unidas por um traço devem ser consideradas em separado: Ex: lírio-do-vale serão 3 palavaras
  * Algumas palavras devem ser desconsideradas por se tratarem de artigos ou preposições. Lista de palavras a serem desconsideradas: `a(s)`, `o(s)`, `um(s)`, `uma(s)`, `de`, `do` e `da`
  * As palavras maiúsculas e minúsculas devem ser consideradas como a mesma palavra. Ex: Batata, batata.
  * As separações silábicas de palavras no final da linha não podem comprometer a palavra. Ex: Se a palavra `batata` precisar ser quebrada de linha então fica: 
    * L-n:     `... plantando bata-`
    * L-(n+1): `ta na horta` 
  * As palavras são formadas por letras vogais e consoantes, incluindo as acentuações. Os demais caracteres não podem ser confundidos com palavras. Ex: `,`, `.`, `;`, `:`, `?`, `|`, `[`, `]`, `{`, `}`, `/`, `\`, `0123456789`, `'`, `"`, `+`, `-`, `=`, `*`, `!`, `@`, `#`, `$`, `%`, `&`
  * O resumo apresentado deve conter: o nome do arquivo, a lista das 10 palavras mais utilizadas com a relação das linhas de cada ocorrência

```txt
Arquivo analisado: file-06-trecho-livro-filosofia.txt
Lista das top 10 palavras mais utilizadas e as respectivas linhas onde aparecem:
* 10 x palavra: - L-1, L-2, L-2, L3, ..
* 10 x outra: - L-1, L-2, L3, ..
```

* Requisitos técnico não funcional:
  * O programa deverá fazer uso dos seguintes recursos de programação em linguagem Python:
    * string, iterators, list, tuple, dictionary, set, list comprehension,


## I - Referências

* [Udemmy - Python 3](https://www.udemy.com/course/python-3-do-zero-ao-avancado)
* [Youtube - Felipe Deschamps](https://www.youtube.com/playlist?list=PLMdYygf53DP7YZiFUtGTWJJlvynRyrna-)
* [Python 3 - Documentation](https://docs.python.org/3/library/index.html)
* [Python Tutorial - W3School (Online)](https://www.w3schools.com/python/default.asp)
* [Python Tips](https://book.pythontips.com/en/latest)
