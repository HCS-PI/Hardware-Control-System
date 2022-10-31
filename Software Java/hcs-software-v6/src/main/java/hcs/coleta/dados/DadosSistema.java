package hcs.coleta.dados;

import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.util.Conversor;

public class DadosSistema {

    Looca looca = new Looca();
    Conversor conversor = new Conversor();
    
    String sistemaOperacional, fabricanteSistema, arquiteturaSistema, tempoAtvSistema;

    public String getSistemaOperacional() {
        
        sistemaOperacional = looca.getSistema().getSistemaOperacional();
        
        return sistemaOperacional;
    }

    public String getFabricanteSistema() {
        
        fabricanteSistema  = looca.getSistema().getFabricante();
        
        return fabricanteSistema;
    }

    public String getArquiteturaSistema() {
        
        arquiteturaSistema  = String.format("%d Bits", looca.getSistema().getArquitetura());
        
        return arquiteturaSistema;
    }

    public String getTempoAtvSistema() {
        
        tempoAtvSistema = conversor.formatarSegundosDecorridos(looca.getSistema().getTempoDeAtividade());
        
        return tempoAtvSistema;
    }
}
