
import Plot from 'react-plotly.js';

function Grafico({ fx, gx, resultado }) {
  if (!resultado || !resultado.grafico) {
    return <p>O gráfico aparecerá após o cálculo.</p>;
  }

  const pontos = resultado.grafico;

  const dados = [
    {
      x: pontos.x,
      y: pontos.fx,
      type: 'scatter',
      mode: 'lines',
      name: fx,
      line: { color: '#3478f6' }
    },
    {
      x: pontos.x,
      y: pontos.gx,
      type: 'scatter',
      mode: 'lines',
      name: gx,
      line: { color: '#f59e0b' }
    }
  ];

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
