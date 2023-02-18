# Boas-vindas ao repositório do Projeto Job Insights!

## Projeto desenvolvido durante o bloco de Ciência da Computação do curso de Desenvolvimento Web da Trybe.

  Neste projeto foram implementadas análises a partir de um conjunto de dados sobre empregos, utilizando <strong>Python</strong>, e incorporadas a um aplicativo Web desenvolvido com <strong>Flask</strong> (um framework web muito popular na comunidade Python). Os testes foram feitos com <strong>Pytest</strong> como garantia de melhor implementação da aplicação.

# Orientações
 
  1. Clone o repositório

  - Use o comando: `git clone git@github.com:lcsrbr/python-job-insights.git`.
 
  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  4. Rode a aplicação e acesse a partir de `http://localhost:5000`

  - `flask run --host=0.0.0.0`
  
  5. Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  - `python3 -m pytest`

# Implementações feitas


## 1 - Função `read`
> **Implementada em:** `src/insights/jobs.py`

 - Função responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.

- <details>
    <summary>
        <b>📝Exemplo</b>
    </summary>
    Se o conteúdo do arquivo for:
    
    ```
    nome,cidade,telefone
    Ana,Curitiba,1111111
    Bernardo,Santos,999999
    ```

    O retorno da função deverá ser: 
    
    ```python
    [
        {"nome": "Ana", "cidade": "Curitiba", "telefone": "1111111"},
        {"nome": "Bernardo", "cidade": "Santos", "telefone": "999999"}
    ]
    ```
    </details> 

<br>

## 2 - Função `get_unique_job_types`
> **Implementada em:** `src/insights/jobs.py`

- A função retorna uma lista de valores únicos presentes na coluna `job_type`.

<br>

## 3 - Função `get_unique_industries`
> **Implementada em:** `src/insights/industries.py`

- A função retorna uma lista de valores únicos presentes na coluna `industry`.

<br>

## 4 - Função `get_max_salary`
> **Implementada em:** `src/insights/salaries.py`

- A função retorna um valor inteiro com o maior salário presente na coluna `max_salary`.

<br>

## 5 - Função `get_min_salary`
> **Implementada em:** `src/insights/salaries.py`

- A função retorna *um valor inteiro* com o menor salário presente na coluna `min_salary`.

<br>

## 6 - Função `filter_by_job_type`
> **Implementada em:** `src/insights/jobs.py`

- A função retorna uma lista com todos os empregos onde a coluna `job_type` corresponde ao parâmetro `job_type`.

<br>

## 7 - Função `filter_by_industry`
> **Implementada em:** `src/insights/industries.py`

- A função retorna uma lista de dicionários com todos os empregos onde a coluna `industry` corresponde ao parâmetro `industry`.

<br>

## 8 - Função `matches_salary_range`
> **Implementada em:** `src/insights/salaries.py`

- A função retorna `True` se o salário procurado estiver dentro da faixa salarial ou `False` se não estiver.

- <details>
    <summary>
        <b>📝Validações</b>
    </summary>
    
    - A função recebe um dicionário `job` como primeiro parâmetro, com as chaves `min_salary` e `max_salary`, que podem ser números ou strings que representem números.
    - A função recebe um número ou string que represente o número `salary` como segundo parâmetro.
    - A função lança um erro `ValueError` nos seguintes casos:
    - alguma das chaves `min_salary` ou `max_salary` estão *ausentes* no dicionário;
    - alguma das chaves `min_salary` ou `max_salary` tem valores não-numéricos;
    - o valor de `min_salary` é maior que o valor de `max_salary`;
    - o parâmetro `salary` tem valores não numéricos;

    </details> 

<br>

## 9 - Função `filter_by_salary_range`
> **Implementada em:** `src/insights/salaries.py`

- A função retorna uma lista com todos os empregos onde o salário `salary` estiver entre os valores da coluna `min_salary` e `max_salary`.


- <details>
    <summary>
        <b>📝Validações</b>
    </summary>
    
    - A função recebe uma lista de dicionários `jobs` como primeiro parâmetro.
    - A função recebe um número ou string `salary` como segundo parâmetro.
    - A função ignora os empregos com valores inválidos para `min_salary` ou `max_salary`.

    </details> 

<br>

## 10 - Teste para a função `count_ocurrences`
> **Implementada em:** `tests/counter/test_counter.py`

- O teste chama a função `count_ocurrences` passando dois parâmetros:
  - `path` uma string com o caminho do arquivo (`data/jobs.csv`);
  - `word` uma string com a palavra a ser contabilizada.
- Garante que a função retorna corretamente a quantidade de ocorrências da palavra solicitada 

<br>

## 11 - Teste para a função `read_brazilian_file`
> **Implementada em:** `tests/brazilian/test_brazilian_jobs.py`

- O teste chama a função `read_brazilian_file` e ela  recebe um parâmetro:
  - `path` que é uma string com o caminho do arquivo csv em português (`tests/mocks/brazilians_jobs.csv`);
  - Retorna uma lista de dicionários com as chaves em inglês

- <details>
    <summary>
        <b>📝Exemplo</b>
    </summary>
    O dicionário: <code>{"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}</code>

    Deve ser traduzido para: <code>{"title": "Maquinista", "salary": "2000", "type": "trainee"}</code>
    </details>  

<br>

## 12 - Teste para a função `sort_by`
> **Implementada em:** `tests/sorting/test_sorting.py`

- A função `sort_by` recebe dois parâmetros:
  - `jobs` uma lista de dicionários com os detalhes de cada emprego;
  - `criteria` uma string com uma chave para ser usada como critério de ordenação.
- O parâmetro `criteria` deve ter um destes valores: `min_salary`, `max_salary`, `date_posted`
- A ordenação para `min_salary` deve ser crescente, mas para `max_salary` ou `date_posted` devem ser decrescentes.
- Os empregos que não apresentarem um valor válido no campo escolhido para ordenação devem aparecer no final da lista.

<br>

## 13 - Página de job (com flask)
> **Implementada em:** `src/flask_app/routes_and_views.py`

- A função é decorada com a rota `/job/<index>`.
- A função recebe um parâmetro `index`.
- A função chama a `read` para ter uma lista com todos os jobs.
- A função chama a `get_job`, declarada no arquivo `src/flask_app/more_insights.py`, para selecionar um job específico pelo `index`.
- A função renderiza o template `job.jinja2`, passando um parâmetro `job` contendo o job retornado pela `get_job`.

<br>

## [Outros Projetos](https://portfolio-lcsrbr.vercel.app/projects)
