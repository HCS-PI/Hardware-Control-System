package hcs.graficos;

import java.util.TimerTask;

public class GraficoTempTask extends TimerTask
{
   
  private GraficoTemp graficoLinha;

  public GraficoTempTask(GraficoTemp graficoLinha) {
    this.graficoLinha = graficoLinha;
  }

  @Override
  public void run() {
    graficoLinha.atualizarDataSet();
  }
}
