import sympy as sp

def distancia(fx, gx):
    x = sp.Symbol("x")

    equacao = sp.simplify(fx - gx)

    if equacao == 0:
        return None

    intervalo = sp.Interval(-sp.pi, sp.pi)

    solucoes = sp.solveset(
        equacao,
        x,
        domain=intervalo
    )

    if isinstance(solucoes, sp.FiniteSet):
        intersecoes = list(solucoes)

    else:
        intersecoes = []

        for tentativa in [-10, -5, -2,-0.5, -1, 0, 0.5, 1, 2, 5, 10]:
            try:
                raiz = sp.nsolve(equacao, x, tentativa)

                if raiz.is_real and intervalo.contains(raiz):
                    raiz = sp.N(raiz, 8)

                    if abs(float(raiz) - round(float(raiz))) < 0.0001:
                        raiz = sp.Integer(round(float(raiz)))

                    if not any(
                        abs(float(raiz - ponto)) < 0.0001
                        for ponto in intersecoes
                    ):
                        intersecoes.append(raiz)

            except (ValueError, TypeError, ZeroDivisionError):
                pass

    intersecoes = sorted(
        intersecoes,
        key=lambda ponto: float(sp.N(ponto))
    )

    return intersecoes
