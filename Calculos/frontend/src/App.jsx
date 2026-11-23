
import { useState } from 'react';
import './App.css';
import Grafico from './grafico';

function App() {
  const [fx, setFx] = useState('');
  const [gx, setGx] = useState('');
  const [modo, setModo] = useState('automatico');
  const [inicio, setInicio] = useState('');
  const [fim, setFim] = useState('');
  const [resultado, setResultado] = useState(null);
  const [erro, setErro] = useState('');

  async function calcularArea() {
    setErro('');
    setResultado(null);

    if (!fx.trim() || !gx.trim()) {
      setErro('Informe as duas funções antes de calcular.');
      return;
    }

    if (modo === 'manual') {
      if (inicio.trim() === '' || fim.trim() === '') {
        setErro('Informe os dois limites do intervalo.');
        return;
      }

      if (Number(inicio) >= Number(fim)) {
        setErro('O limite inicial precisa ser menor que o final.');
        return;
      }
    }

    try {
      const resposta = await fetch('http://127.0.0.1:8000/calcular', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          fx: fx,
          gx: gx,
          modo: modo,
          inicio: modo === 'manual' ? inicio : null,
          fim: modo === 'manual' ? fim : null
        })
      });

      const dados = await resposta.json();

      if (!resposta.ok) {
        throw new Error(dados.detail || 'Não foi possível realizar o cálculo.');
      }

      setResultado(dados);

    } catch (erro) {
      setErro(erro.message || 'Erro ao conectar com o servidor Python.');
      console.log(erro);
    }
  }

  return (
    <div className="pagina">
      <header className="cabecalho">
        <h1>Calculadora de Área entre Curvas</h1>
        <p>
          Descubra a área delimitada entre duas funções matemáticas.
        </p>
      </header>

      <main className="conteudo">
        <section className="entrada">
          <h2>Informe as funções</h2>

          <div className="campo">
            <label>Primeira função f(x)</label>
            <input
              type="text"
              value={fx}
              onChange={(evento) => setFx(evento.target.value)}
            />
          </div>

          <div className="campo">
            <label>Segunda função g(x)</label>
            <input
              type="text"
              value={gx}
              onChange={(evento) => setGx(evento.target.value)}
            />
          </div>

          <div className="campo">
            <label>Modo de cálculo</label>
            <select
              value={modo}
              onChange={(evento) => setModo(evento.target.value)}
            >
              <option value="automatico">Automático - encontrar interseções</option>
              <option value="manual">Manual - escolher intervalo</option>
            </select>
          </div>

          {modo === 'manual' && (
            <div className="limites">
              <h3>Intervalo de cálculo</h3>

              <div className="campo">
                <label>Ponto Inicial (a)</label>
                <input
                  type="number"
                  step="any"
                  value={inicio}
                  onChange={(evento) => setInicio(evento.target.value)}
                />
              </div>

              <div className="campo">
                <label>Ponto Final (b)</label>
                <input
                  type="number"
                  step="any"
                  value={fim}
                  onChange={(evento) => setFim(evento.target.value)}
                />
              </div>
            </div>
          )}

          <button onClick={calcularArea}>
            Calcular área
          </button>
        </section>

        <section className="resultado">
          <h2>Gráfico e resultados</h2>

          <Grafico
            fx={fx}
            gx={gx}
            resultado={resultado}
          />

          {erro && <p className="erro">{erro}</p>}

          {resultado && (
            <div>
              {resultado.mensagem ? (
                <p>{resultado.mensagem}</p>
              ) : (
                <>
                  <h3>Interseções</h3>

                  {resultado.intersecoes.length > 0 ? (
                    <p>{resultado.intersecoes.join(', ')}</p>
                  ) : (
                    <p>Nenhuma interseção encontrada.</p>
                  )}
                </>
              )}

              <h3>Áreas encontradas</h3>

              {resultado.areas.length > 0 ? (
                resultado.areas.map((area, indice) => (
                  <div className="area-item" key={indice}>
                    <p>
                      Intervalo: {area.inicio} até {area.fim}
                    </p>

                    <p>Função superior: {area.superior}</p>
                    <p>Função inferior: {area.inferior}</p>
                    <p>Área: {area.area}</p>

                  </div>
                ))
                
              ) : (
                <p>Nenhuma área delimitada encontrada.</p>
              )}
              <div className="area-total">
                <h3>Área total</h3>
                <p>{resultado.area_total} {resultado.unidade}</p>
            </div>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
