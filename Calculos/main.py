import sympy as sp

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from Funcoes import interpretar_funcao
from Distancia import distancia
from Integral import calcular_areas, calcular_area_intervalo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class FuncoesEntrada(BaseModel):
    fx: str
    gx: str
    modo: str = "automatico"
    inicio: str | None = None
    fim: str | None = None


def gerar_pontos(f, g, intersecoes, limites=None):
    x = sp.Symbol("x")

    pontos = []

    for ponto in intersecoes:
        if ponto.is_real:
            pontos.append(float(sp.N(ponto)))

    if limites is not None:
        inicio = min(float(sp.N(limites[0])) - 5, -10)
        fim = max(float(sp.N(limites[1])) + 5, 10)

    elif pontos:
        inicio = min(pontos) - 1
        fim = max(pontos) + 1

    else:
        inicio = -10
        fim = 10

    valores_x = []
    valores_f = []
    valores_g = []

    for i in range(201):
        valor_x = inicio + (fim - inicio) * i / 200

        valores_x.append(valor_x)

        try:
            resultado_f = sp.N(f.subs(x, valor_x))
            resultado_g = sp.N(g.subs(x, valor_x))

            if resultado_f.is_real and resultado_f.is_finite:
                valores_f.append(float(resultado_f))
            else:
                valores_f.append(None)

            if resultado_g.is_real and resultado_g.is_finite:
                valores_g.append(float(resultado_g))
            else:
                valores_g.append(None)

        except (TypeError, ValueError):
            valores_f.append(None)
            valores_g.append(None)

    return {
        "x": valores_x,
        "fx": valores_f,
        "gx": valores_g
    }


@app.post("/calcular")
def calcular(dados: FuncoesEntrada):

    try:
        f = interpretar_funcao(dados.fx)
        g = interpretar_funcao(dados.gx)

        intersecoes = distancia(f, g)

        limites = None

        if dados.modo == "manual":

            if dados.inicio is None or dados.fim is None:
                raise HTTPException(
                    status_code=400,
                    detail="Informe os dois limites do intervalo."
                )

            try:
                limites = (
                    sp.sympify(dados.inicio),
                    sp.sympify(dados.fim)
                )

                areas = calcular_area_intervalo(
                    f,
                    g,
                    limites[0],
                    limites[1]
                )

                # Filtra as interseções pelo intervalo manual
                intersecoes = [
                    ponto for ponto in (intersecoes or [])
                    if (
                        ponto.is_real
                        and float(sp.N(ponto)) >= float(sp.N(limites[0]))
                        and float(sp.N(ponto)) <= float(sp.N(limites[1]))
                    )
                ]

            except (ValueError, TypeError) as erro:
                raise HTTPException(
                    status_code=400,
                    detail=str(erro)
                )

        elif dados.modo == "automatico":

            if intersecoes is None:
                grafico = gerar_pontos(f, g, [])

                return {
                    "mensagem": "As duas funções são iguais. Existem infinitos pontos de interseção.",
                    "intersecoes": [],
                    "pontos_intersecao": [],
                    "areas": [],
                    "area_total": "0",
                    "unidade": "u.a.",
                    "grafico": grafico
                }

            areas = calcular_areas(f, g, intersecoes)

        else:
            raise HTTPException(
                status_code=400,
                detail="Modo de cálculo inválido."
            )

        # Gera os pontos do gráfico
        grafico = gerar_pontos(
            f,
            g,
            intersecoes if intersecoes is not None else [],
            limites
        )

        # Calcula as coordenadas dos pontos de interseção
        pontos_intersecao = []

        x = sp.Symbol("x")

        for ponto in (intersecoes or []):

            if ponto.is_real:
                valor_x = float(sp.N(ponto))
                valor_y = sp.N(f.subs(x, ponto))

                if valor_y.is_real and valor_y.is_finite:
                    pontos_intersecao.append({
                        "x": valor_x,
                        "y": float(valor_y)
                    })

        # Soma todas as áreas encontradas
        area_total = sp.simplify(
            sum(area["area"] for area in areas)
        )

        return {
            "intersecoes": [
                str(ponto) for ponto in (intersecoes or [])
            ],

            "pontos_intersecao": pontos_intersecao,

            "areas": [
                {
                    "inicio": str(area["inicio"]),
                    "fim": str(area["fim"]),
                    "superior": str(area["superior"]),
                    "inferior": str(area["inferior"]),
                    "area": str(area["area"])
                }
                for area in areas
            ],

            "area_total": str(area_total),
            "unidade": "u.a.",

            "grafico": grafico
        }

    except HTTPException:
        raise

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=str(erro)
        )
