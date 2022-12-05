package hcs.graficos;

import hcs.graficos.GraficoCpu;
import java.util.TimerTask;

// Tarefa de atualização do gráfico de linha
public class GraficoCpuTask extends TimerTask
{
    
  private GraficoCpu graficoLinha;

  public GraficoCpuTask(GraficoCpu graficoLinha) {
    this.graficoLinha = graficoLinha;
  }

  @Override
  public void run() {
    graficoLinha.atualizarDataSet();
  }
  
}
