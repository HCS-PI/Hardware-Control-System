package hcs.graficos;

import com.github.britooo.looca.api.core.Looca;
import java.awt.Color;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;
import org.jfree.ui.ApplicationFrame;

public class GraficoTemp extends ApplicationFrame
{
    
    private XYSeries series1;
    private XYSeries series2;
    private XYSeries series3;
    private XYSeriesCollection dataSet;

    Looca looca = new Looca();

    Double processadorUso = looca.getProcessador().getUso();

    Integer respostaCPU = processadorUso.intValue();

    Integer temperatura = looca.getTemperatura().getTemperatura().intValue();
    
    Long memoriaUso = (looca.getMemoria().getEmUso() * 100) / looca.getMemoria().getTotal();

    Integer respostaMemoria = memoriaUso.intValue();
    
    
    public XYDataset gerarDataSetInicial() {
        this.series1 = new XYSeries("TEMP");
        series1.add(0.0, 0.0);
        
        this.series2 = new XYSeries("CPU");
        series2.add(0.0, 0.0);
        
        this.series3 = new XYSeries("RAM");
        series3.add(0.0, 0.0);
        
        final XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(series1);
        dataset.addSeries(series2);
        dataset.addSeries(series3);
    
        return dataset;

    }
    
    public JFreeChart gerarGrafico(final XYDataset dataset) {

        JFreeChart chart = ChartFactory.createXYLineChart(
                "Monitoramento TEMPERATURA - CPU X RAM",
                "",
                "",
                dataset,
                PlotOrientation.VERTICAL,
                true,
                true,
                false
        );

        chart.setBackgroundPaint(Color.WHITE);

        final XYPlot plot = chart.getXYPlot();
        plot.setBackgroundPaint(Color.lightGray);
        plot.setDomainGridlinePaint(Color.white);
        plot.setRangeGridlinePaint(Color.white);

        final XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer();
        plot.setRenderer(renderer);

        final NumberAxis rangeAxis = (NumberAxis) plot.getRangeAxis();
        rangeAxis.setStandardTickUnits(NumberAxis.createIntegerTickUnits());

        return chart;
    }
    
    
    public void atualizarDataSet() {
        processadorUso = looca.getProcessador().getUso();
        respostaCPU = processadorUso.intValue();
        memoriaUso = (looca.getMemoria().getEmUso() * 100) / looca.getMemoria().getTotal();
        respostaMemoria = memoriaUso.intValue();
        temperatura = looca.getTemperatura().getTemperatura().intValue();

        // pegando o último valor do eixo X
        double maxXSeries1 = series1.getMaxX();
        double maxXSeries2 = series2.getMaxX();
        double maxXSeries3 = series3.getMaxX();
        
        double minXSeries1 = series1.getMinX();
        double minXSeries2 = series2.getMinX();
        double minXSeries3 = series3.getMinX();
       

        if (maxXSeries1 > 5 ) {
            series1.remove(minXSeries1);
            series2.remove(minXSeries2);
            series3.remove(minXSeries3);
            
        }
        series1.add(maxXSeries1 + 1, temperatura);
        series2.add(maxXSeries2 + 1, respostaCPU);
        series3.add(maxXSeries3 + 1, respostaMemoria);
               
        dataSet = new XYSeriesCollection();
        dataSet.addSeries(series1);
        dataSet.addSeries(series2);
        dataSet.addSeries(series3);
      
    }
    
    public GraficoTemp(String title) {
        super(title);
    }
    
}
