
import Plot from 'react-plotly.js';

function Grafico({ fx, gx, resultado }) {
  if (!resultado || !resultado.grafico) {
    return <p>O gráfico aparecerá após o cálculo.</p>;
  }

  const pontos = resultado.grafico;

  const dados = [];

  // Cria o preenchimento vermelho de cada área calculada
  (resultado.regioes_grafico || []).forEach((regiao, indice) => {
    dados.push({
      x: regiao.x,
      y: regiao.superior,
      type: 'scatter',
      mode: 'lines',
      line: { color: 'rgba(0,0,0,0)' },
      showlegend: false,
      hoverinfo: 'skip',
      name: `Área ${indice + 1}`
    });

    dados.push({
      x: regiao.x,
      y: regiao.inferior,
      type: 'scatter',
      mode: 'lines',
      line: { color: 'rgba(0,0,0,0)' },
      fill: 'tonexty',
      fillcolor: 'rgba(255, 0, 0, 0.65)',     
      showlegend: false,
      hoverinfo: 'skip'
    });
  });

  // Curva f(x)
  dados.push({
    x: pontos.x,
    y: pontos.fx,
    type: 'scatter',
    mode: 'lines',
    name: fx,
    line: { color: '#3478f6' }
  });

  // Curva g(x)
  dados.push({
    x: pontos.x,
    y: pontos.gx,
    type: 'scatter',
    mode: 'lines',
    name: gx,
    line: { color: '#f59e0b' }
  });

  // Pontos de interseção
  dados.push({
    x: resultado.pontos_intersecao?.map(p => p.x) || [],
    y: resultado.pontos_intersecao?.map(p => p.y) || [],
    type: 'scatter',
    mode: 'markers',
    name: 'Interseções',
    marker: {
      color: 'red',
      size: 10,
      symbol: 'circle'
    }
  });

  return (
    <Plot
      data={dados}
      layout={{
        title: 'Gráfico das funções',
        xaxis: { title: 'Eixo X', zeroline: true },
        yaxis: { title: 'Eixo Y', zeroline: true },
        autosize: true,
        margin: { t: 50, r: 30, b: 50, l: 50 }
      }}
      style={{ width: '100%' }}
      useResizeHandler={true}
      config={{ responsive: true }}
    />
  );
}

export default Grafico;
