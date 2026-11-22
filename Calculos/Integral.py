import sympy as sp


def calcular_areas(fx, gx, distancia):
    x = sp.Symbol("x")

    pontos = []

    for ponto in distancia:
        if ponto.is_real:
            pontos.append(ponto)

    pontos = sorted(set(pontos), key=lambda p: float(sp.N(p)))

    resultados = []

    for i in range(len(pontos) - 1):
        inicio = pontos[i]
        fim = pontos[i + 1]

        meio = (inicio + fim) / 2

        v1 = fx.subs(x, meio)
        v2 = gx.subs(x, meio)

        if sp.N(v1) > sp.N(v2):
            cima = fx
            baixo = gx
        else:
            baixo = fx
            cima = gx

        area = sp.integrate(
            cima - baixo,
            (x, inicio, fim)
        )

        resultados.append({
            "inicio": inicio,
            "fim": fim,
            "superior": cima,
            "inferior": baixo,
            "area": sp.simplify(area)
        })

    return resultados


def calcular_area_intervalo(fx, gx, inicio, fim):
    x = sp.Symbol("x")

    inicio = sp.sympify(inicio)
    fim = sp.sympify(fim)

    if not inicio.is_real or not fim.is_real:
        raise ValueError("Os limites precisam ser números reais.")

    if sp.N(inicio) >= sp.N(fim):
        raise ValueError("O limite inicial precisa ser menor que o final.")

    diferenca = fx - gx

    pontos = [inicio, fim]

    intersecoes = sp.solveset(
        diferenca,
        x,
        domain=sp.Interval(inicio, fim)
    )

    if isinstance(intersecoes, sp.FiniteSet):
        for ponto in intersecoes:
            if ponto.is_real:
                pontos.append(ponto)

    pontos = sorted(set(pontos),key=lambda p: float(sp.N(p)))

    resultados = []

    for i in range(len(pontos) - 1):
        a = pontos[i]
        b = pontos[i + 1]

        meio = (a + b) / 2

        valor_fx = fx.subs(x, meio)
        valor_gx = gx.subs(x, meio)

        if sp.N(valor_fx) >= sp.N(valor_gx):
            cima = fx
            baixo = gx
        else:
            cima = gx
            baixo = fx

        area = sp.integrate(cima - baixo, (x, a, b))

        resultados.append({
            "inicio": a,
            "fim": b,
            "superior": cima,
            "inferior": baixo,
            "area": sp.simplify(area)
        })

    return resultados
