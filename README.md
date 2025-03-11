# Projeto Algoritmos em Python

## Descrição do Projeto

Este projeto implementa diferentes soluções algorítmicas em Python, incluindo análise de complexidade de algoritmos, manipulação de strings e busca de elementos. O projeto foi desenvolvido como parte do currículo da Trybe, focando em algoritmos e estruturas de dados.

## Funcionalidades Implementadas

- Análise de horários de estudo (study_schedule)
- Criptografia de mensagens (encrypt_message)
- Verificação de palíndromos (recursivo e iterativo)
- Identificação de anagramas
- Busca de números duplicados
- Análise de complexidade de algoritmos

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal
- **Pytest**: Framework de testes
- **Black**: Formatador de código
- **Flake8**: Linter para garantir qualidade do código

## Pré-requisitos

Para rodar este projeto, você precisará ter instalado:

- Python 3.x
- pip (gerenciador de pacotes do Python)

## Instalação e Execução

1. **Clone o repositório**
```bash
git clone git@github.com:seu-usuario/project-algorithms.git
cd project-algorithms
```

2. **Crie e ative o ambiente virtual**
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
python3 -m pip install -r dev-requirements.txt
```

4. **Execute os testes**
```bash
python3 -m pytest
```

## Estrutura do Projeto

```
challenges/
  ├── challenge_anagrams.py           # Algoritmo para verificação de anagramas
  ├── challenge_encrypt_message.py     # Algoritmo de criptografia
  ├── challenge_find_the_duplicate.py  # Busca de números duplicados
  ├── challenge_palindromes_iterative.py # Verificação iterativa de palíndromos
  ├── challenge_palindromes_recursive.py # Verificação recursiva de palíndromos
  └── challenge_study_schedule.py      # Análise de horários de estudo

tests/                                 # Diretório de testes
```

## Detalhamento das Funções

### Study Schedule
- Analisa os horários mais frequentes de acesso de pessoas estudantes

### Palindromes
- Implementações iterativa e recursiva para verificação de palíndromos

### Anagrams
- Verifica se duas strings são anagramas

### Find the Duplicate
- Encontra números duplicados em uma sequência

### Encrypt Message
- Implementa um algoritmo de criptografia de mensagens

## Desenvolvimento

O projeto foi desenvolvido seguindo os princípios de Clean Code e as boas práticas de programação Python. Cada algoritmo foi implementado considerando:

- Eficiência de tempo e espaço
- Legibilidade do código
- Testes unitários robustos
- Documentação clara

## Testes

Para executar os testes específicos:

```bash
python3 -m pytest tests/test_encrypt.py  # testa apenas encrypt
python3 -m pytest -v                     # testa todos com detalhes
```

## Contribuição

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Autor

Marco Fabian - [GitHub](https://github.com/marco-fabian)

## Licença

Este projeto está sob a licença MIT.