package hcs.coleta.dados;

import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.util.Conversor;

public class DadosCpu {

    Looca looca = new Looca();
    Conversor conversor = new Conversor();

    String modeloCpu;
    
    Integer qtdNucleosFisicos, qtdNucleosVirtuais, qtdTotalNucleos;
    
    Long consumoCpu;

    public Long getConsumoCpu() {
        
        Double conCpu = looca.getProcessador().getUso();
        Long consumoCpu = Math.round(conCpu);// Consumo de CPU Arredondado para inserir no setValue() da Progre
        
        return consumoCpu;
    }

    public String getModeloCpu() {
        
        modeloCpu = looca.getProcessador().getNome();
        
        return modeloCpu;
    }

    public Integer getQtdNucleosFisicos() {
        
        qtdNucleosFisicos = looca.getProcessador().getNumeroCpusFisicas();
        
        return qtdNucleosFisicos;
    }

    public Integer getQtdNucleosVirtuais() {
        
        qtdNucleosVirtuais  = looca.getProcessador().getNumeroCpusLogicas() - getQtdNucleosFisicos();
        
        return qtdNucleosVirtuais;
    }

    public Integer getQtdTotalNucleos() {
        
        qtdTotalNucleos = getQtdNucleosFisicos() + getQtdNucleosVirtuais();
        
        return qtdTotalNucleos;
    }
}
