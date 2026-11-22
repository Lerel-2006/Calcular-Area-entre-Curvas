# Calculadora de Área entre Curvas

## Sobre o projeto

A **Calculadora de Área entre Curvas** é uma aplicação web desenvolvida para calcular a área compreendida entre duas funções matemáticas por meio de integrais definidas.

O sistema permite que o usuário informe duas funções e visualize suas representações gráficas, além de obter os pontos de interseção e os resultados dos cálculos.

O projeto foi desenvolvido como uma aplicação prática dos conceitos de Cálculo Diferencial e Integral, utilizando ferramentas de desenvolvimento web e computação simbólica.

## Funcionalidades

- Inserção de duas funções matemáticas.
- Identificação automática dos pontos de interseção.
- Cálculo automático da área entre as curvas.
- Modo manual para informar os limites de integração.
- Identificação da função superior e inferior em cada intervalo.
- Visualização gráfica das funções.
- Apresentação dos resultados das integrais.

## Tecnologias utilizadas

### Frontend
- React
- JavaScript
- CSS
- Plotly.js — representação gráfica das funções.

### Backend
- Python
- FastAPI — criação da API.
- SymPy — manipulação de expressões matemáticas, resolução de equações e cálculo de integrais.

## Estrutura do projeto

```text
Calculos/
│
├── Distancia.py
├── Funcoes.py
├── Integral.py
├── main.py
├── teste.py
│
├── frontend/
│   └── src/
│       ├── components/
│       │   └── Grafico.jsx
│       ├── App.jsx
│       └── App.css
│
└── .venv/
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Acessar a pasta do projeto

```bash
cd Calculos
```

### 3. Criar e ativar o ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

Ativar:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências do backend

```bash
pip install fastapi uvicorn sympy
```

### 5. Iniciar o backend

```bash
python -m uvicorn main:app --reload
```

A API ficará disponível em:

http://127.0.0.1:8000

A documentação interativa da API pode ser acessada em:

http://127.0.0.1:8000/docs

### 6. Iniciar o frontend

Abra outro terminal e acesse a pasta:

```bash
cd frontend
```

Instale as dependências:

```bash
npm install
```

Execute a aplicação:

```bash
npm run dev
```

O endereço de acesso será apresentado no terminal pelo Vite.

## Organização dos arquivos Python

| Arquivo | Responsabilidade |
|---|---|
| `Funcoes.py` | Interpretação das expressões matemáticas utilizando SymPy. |
| `Distancia.py` | Identificação dos pontos de interseção entre as funções. |
| `Integral.py` | Cálculo das áreas entre as curvas nos modos automático e manual. |
| `main.py` | Integração dos módulos e disponibilização dos serviços pela API. |
| `teste.py` | Arquivo destinado à realização de testes. |

## Exemplo de utilização

Considere as funções:

```text
f(x) = x**2
g(x) = x
```

O sistema interpreta as expressões, procura os pontos de interseção, identifica qual função está acima da outra em cada intervalo e calcula a integral definida correspondente.

## Objetivo acadêmico

O desenvolvimento deste projeto tem como finalidade demonstrar a aplicação prática dos conceitos de integrais definidas e áreas entre curvas, relacionando os conhecimentos matemáticos com a programação e o desenvolvimento de aplicações web.

---

**Projeto acadêmico — Calculadora de Área entre Curvas.**
