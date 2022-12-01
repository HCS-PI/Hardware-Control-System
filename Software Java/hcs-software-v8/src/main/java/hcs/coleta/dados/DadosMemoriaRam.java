
package hcs.coleta.dados;

import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.util.Conversor;


public class DadosMemoriaRam {
    
    Looca looca = new Looca();
    Conversor conversor = new Conversor();
    
    String MemoriaTotalGb, MemoriaUsoGb, MemoriaDisponivelGb;
    
    Long consumoRam;

    public Long getConsumoRam() {
        
        Double conRam = (looca.getMemoria().getEmUso().doubleValue() * 100) / looca.getMemoria().getTotal(); // Consumo RAM %
        
        Long consumoRam = Math.round(conRam);// Consumo de RAM Arredondado para inserir no setValue() da ProgressBar

        return consumoRam;
    }
    
    public String getMemoriaTotalGb() {
        
        MemoriaTotalGb = conversor.formatarBytes(looca.getMemoria().getTotal()); // String Memória RAM Total Gb
        
        return MemoriaTotalGb;
    }

    public String getMemoriaUsoGb() {
        
        MemoriaUsoGb = conversor.formatarBytes(looca.getMemoria().getEmUso()); // String Memória Disponível Total Gb
        
        return MemoriaUsoGb;
    }

    public String getMemoriaDisponivelGb() {
        
        MemoriaDisponivelGb = conversor.formatarBytes(looca.getMemoria().getDisponivel()); // String Memória RAM Usada Gb
        
        return MemoriaDisponivelGb;
    }
    
    
}
