package hcs.graficos;

import java.util.TimerTask;

public class GraficoRamTask extends TimerTask
{
    
   private GraficoRam graficoLinha;

  public GraficoRamTask(GraficoRam graficoLinha) {
    this.graficoLinha = graficoLinha;
  }

  @Override
  public void run() {
    graficoLinha.atualizarDataSet();
  }
}
