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


#### c. Uso gratuito do Google Colabs PaaS (Platform as a Service)

* https://colab.research.google.com/


### 3.5. Guia de Estudo

* n/a

#### 3.5.1. Básico da linguagem Python

##### Variables, datatypes and operators

* [lab-01-helloworld-remarks.py](./src/python/lab-01-helloworld-remarks.py)
* [lab-03-primitive-datatype-string.py](./src/python/lab-03-primitive-datatype-string.py)
* [lab-04-primitive-datatype-int-float-bool.py](./src/python/lab-04-primitive-datatype-int-float-bool.py)
* [lab-05-arithmetics-operator.py](./src/python/lab-05-arithmetics-operator.py)
* [lab-06-variables.py](./src/python/lab-06-variables.py)

##### User input, print, format and casting

* [lab-02-print-separator-end.py](./src/python/lab-02-print-separator-end.py)
* [lab-07-formating-string.py](./src/python/lab-07-formating-string.py)
* [lab-08-user-input-casting-datatype.py](./src/python/lab-08-user-input-casting-datatype.py)
* [lab-16-formatting-values.py](./src/python/lab-16-formatting-values.py)

##### if, elif, else and operators

* [lab-09-if-elif-else.py](./src/python/lab-09-if-elif-else.py)
* [lab-10-relational-operator.py](./src/python/lab-10-relational-operator.py)
* [lab-11-logical-operator.py](./src/python/lab-11-logical-operator.py)
* [lab-12-string-functions.py](./src/python/lab-12-string-functions.py)

##### built-in

* [lab-13-built-in-functions-documentation.py](./src/python/lab-13-built-in-functions-documentation.py)

##### try ... except

* [lab-14-try-except.py](./src/python/lab-14-try-except.py)

##### pass, ellipsis and placeholders

* [lab-15-pass-ellipsis-placeholders.py](./src/python/lab-15-pass-ellipsis-placeholders.py)

##### while, for, continue and break

* [lab-18-while-continue-for.py](./src/python/lab-18-while-continue-for.py)

##### String manipulation

* [lab-17-string-index-slice.py](./src/python/lab-17-string-index-slice.py)
* [lab-19-string-iterator.py](./src/python/lab-19-string-iterator.py)

##### Iterators

* [lab-20-for-iterator-range.py](./src/python/lab-20-for-iterator-range.py)

##### List and list functions

* [lab-21-lists-index-slice-append-insert-del-clear-extend.py](src/python/lab-21-lists-index-slice-append-insert-del-clear-extend.py)
* [lab-22-list-for-continue-if-else.py](src/python/lab-22-list-for-continue-if-else.py)
* [lab-23-split-join-enumerate-tuples-unpackage.py](src/python/lab-23-split-join-enumerate-tuples-unpackage.py)
* [lab-24-list-of-list-tuples-enumerate.py](src/python/lab-24-list-of-list-tuples-enumerate.py)
* [lab-25-lists-unpacking.py](src/python/lab-25-lists-unpacking.py)
* [lab-26-swap-value-between-2-variables.py](src/python/lab-26-swap-value-between-2-variables.py)
* [lab-27-conditional-expression-ternary-operation.py](src/python/lab-27-conditional-expression-ternary-operation.py)


#### 3.5.2. Básico da linguagem Python

* [lab-101-def-function-create-use-arguments-default-return.py](src/python/lab-101-def-function-create-use-arguments-default-return.py)
* [lab-102-def-return-no-return-function-return.py](src/python/lab-102-def-return-no-return-function-return.py)
* [lab-103-def-return-list-tuple.py](src/python/lab-103-def-return-list-tuple.py)
* [lab-104-def-functions-args-kwargs.py](src/python/lab-104-def-functions-args-kwargs.py)
* [lab-105-variable-scopes-global-function-local.py](src/python/lab-105-variable-scopes-global-function-local.py)
* [lab-106-lambda-expression-anonymous-function.py](src/python/lab-106-lambda-expression-anonymous-function.py)
* [lab-107-tuple-vs-list.py](src/python/lab-107-tuple-vs-list.py)
* [lab-108-dictionary.py](src/python/lab-108-dictionary.py)
* [lab-109-set-add-update-clear-discard-union-intersection-difference.py](src/python/lab-109-set-add-update-clear-discard-union-intersection-difference.py)
* [lab-110-list-comprehension.py](src/python/lab-110-list-comprehension.py)


## I - Referências

* [Udemmy - Python 3](https://www.udemy.com/course/python-3-do-zero-ao-avancado)
* [Youtube - Felipe Deschamps](https://www.youtube.com/watch?v=Gojqw9BQ5qY)
* [Python 3 - Documentation](https://docs.python.org/3/library/index.html)
* [Python Tutorial - W3School (Online)](https://www.w3schools.com/python/default.asp)
* [Python Tips](https://book.pythontips.com/en/latest)
