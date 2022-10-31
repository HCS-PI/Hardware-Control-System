package hcs.coleta.dados;

import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.util.Conversor;

public class DadosDisco {

    Looca looca = new Looca();
    Conversor conversor = new Conversor();

    Long espacoDiscoTotal = looca.getGrupoDeDiscos().getVolumes().get(0).getTotal(); // Espaço Total do Disco
    Long espacoDiscoDisp = looca.getGrupoDeDiscos().getVolumes().get(0).getDisponivel(); // Espaço Disponível do Disco
    Long espacoDiscoUso = espacoDiscoTotal - espacoDiscoDisp; // Espaço Usado do Disco
    
    String strDiscoTotalGb, strDiscoDispGb, strDiscoUsadoGb;

    public Long getConsumoDisco() {
        
        Double conDisco = (espacoDiscoUso.doubleValue() * 100) / espacoDiscoTotal.doubleValue(); // Consumo de Disco em %
        
        Long consumoDisco = Math.round(conDisco); // Consumo de Disco Arredondado para inserir no setValue() da ProgressBar

        return consumoDisco;
    }

    public String getStrDiscoTotalGb() {
         
        strDiscoTotalGb = conversor.formatarBytes(espacoDiscoTotal); // Espaço Total do Disco
        
        return strDiscoTotalGb;
    }

    public String getStrDiscoDispGb() {
         
        strDiscoDispGb = conversor.formatarBytes(espacoDiscoDisp); // Espaço Disponível do Disco
        
        return strDiscoDispGb;
    }

    public String getStrDiscoUsadoGb() {
        
        strDiscoUsadoGb = conversor.formatarBytes(espacoDiscoUso); // Espaço Usado do Disco
        
        return strDiscoUsadoGb;
    }

}
