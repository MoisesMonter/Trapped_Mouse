
# Rato no Labirinto

Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte | Campus Pau dos Ferros |


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherineoelsner.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)


## Document to execute this project

#### Para manipular projeto em questão precisará utilizar Ferramenta Django e Python

```
  pip install django
```

| Dependencias | Plataforma      | how to use                          |
| :---------- | :--------- | :---------------------------------- |
| `django-admin` | `Windows` | **python manage.py runserver**. run to windows |
| `django-admin` | `Linuxs` | **sudo python3 manage.py runserver**. run to linux |

#### Retorna um Link

```
  Link: http://localhost:8000
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Select Wall`      | `Multi-Choice` | **Não é Obrigatório**. As paredes do teu labirinto |
| `Select-Rat-Position`      | `Choies` | **Obrigatório**. Retorna uma posição da Matriz |
| `Select-Cheese-Position`      | `Choices` | **Obrigatório**. Retorna uma posição da Matriz |
| `Run Code`      | `Start` | **Obrigatório**. Buscar Pilha de sequência do caminho para desempilhar |

#### Rato[Line, Column]
#### Queijo[Line, Column]
### MAP Matriz[L=7][C=7]

Manipula posiçoes do mapa e atualizando posição do rato
#### End

```
  Rato == Queijo
```
