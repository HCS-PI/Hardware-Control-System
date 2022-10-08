package com.mycompany.teste.looca;

import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.group.discos.Volume;
import com.github.britooo.looca.api.util.Conversor;
import java.lang.Math;

public class TesteLooca {

    public static void main(String[] args) {

        Looca looca = new Looca();
        Conversor conversor = new Conversor();
        
        informacoesSitesma(looca, conversor);
        informacoesCpu(looca, conversor);
        informacoesRam(looca, conversor);
        informacoesDisco(looca, conversor);

    }

    public static void informacoesSitesma(Looca looca, Conversor conversor) {
        // Informações Sistema 

        String sistemaOperacional, fabricanteSistema, tempoAtvSistema, arquiteturaSistema;

        sistemaOperacional = looca.getSistema().getSistemaOperacional();
        fabricanteSistema = looca.getSistema().getFabricante();
        arquiteturaSistema = String.format("%d Bits", looca.getSistema().getArquitetura());
        tempoAtvSistema = conversor.formatarSegundosDecorridos(looca.getSistema().getTempoDeAtividade());

        System.out.println("-".repeat(72));
        System.out.println("*** INFORMAÇÕES DO SISTEMA ***");
        System.out.println("Sistema Operacional: " + sistemaOperacional); // SO
        System.out.println("Fabricante: " + fabricanteSistema); // FABRICANTE
        System.out.println("Arquitetura SO: " + arquiteturaSistema); // ARQUITETURA
        System.out.println("Tempo de Atividade do Sistema: " + tempoAtvSistema); // TEMPO DE ATIVIDADE
    }

    public static void informacoesCpu(Looca looca, Conversor conversor) {
        // Informações CPU
        String modeloCpu = looca.getProcessador().getNome();
        Integer qtdNucleosFisicos, qtdNucleosLogicos, qtdTotalNucleos;

        qtdNucleosFisicos = looca.getProcessador().getNumeroCpusFisicas();
        qtdNucleosLogicos = looca.getProcessador().getNumeroCpusLogicas();
        qtdTotalNucleos = looca.getProcessador().getNumeroCpusFisicas() + looca.getProcessador().getNumeroCpusLogicas();

        Double consumoCpu = looca.getProcessador().getUso();
        Long pgBarCpu = Math.round(consumoCpu);// Consumo de CPU Arredondado para inserir no setValue() da ProgressBar

        String strConsumoCpu = String.format("%.1f %%", consumoCpu);// String Consumo de CPU para inserir no setString() da ProgressBar

        System.out.println("-".repeat(72));
        System.out.println("*** INFORMAÇÕES DA CPU ***");
        System.out.println("Modelo CPU: " + modeloCpu); // Modelo
        System.out.println("Núcleos Físicos: " + qtdNucleosFisicos); // Núcleos Físicops
        System.out.println("Núcleos Lógicos: " + qtdNucleosLogicos); // Núcleos Lógicos
        System.out.println("Total de Núcleos: " + qtdTotalNucleos); // Total Núcleos
        System.out.println("Consumo de RAM: " + strConsumoCpu);
        System.out.println("Consumo de CPU (INT PGBAR): " + pgBarCpu.intValue());

    }

    public static void informacoesRam(Looca looca, Conversor conversor) {
        // Informações RAM
        String strMemoriaTotalGb, strMemoriaUsoGb, strMemoriaDisponívelGb, strConsumoRam;

        Double consumoRam = (looca.getMemoria().getEmUso().doubleValue() * 100) / looca.getMemoria().getTotal(); // Consumo RAM %
        Long pgBarRam = Math.round(consumoRam);// Consumo de RAM Arredondado para inserir no setValue() da ProgressBar

        strConsumoRam = String.format("%.1f %%", consumoRam);// String Consumo de RAM para inserir no setString() da ProgressBar

        strMemoriaTotalGb = conversor.formatarBytes(looca.getMemoria().getTotal()); // String Memória RAM Total Gb
        strMemoriaDisponívelGb = conversor.formatarBytes(looca.getMemoria().getDisponivel()); // String Memória Disponível Total Gb
        strMemoriaUsoGb = conversor.formatarBytes(looca.getMemoria().getEmUso()); // String Memória RAM Usada Gb

        System.out.println("-".repeat(72));
        System.out.println("*** INFORMAÇÕES DA MEMÓRIA RAM ***");
        System.out.println("Espaço Total: " + strMemoriaTotalGb);
        System.out.println("Espaço Usado: " + strMemoriaUsoGb);
        System.out.println("Espaço Disponível: " + strMemoriaDisponívelGb);
        System.out.println("Consumo de RAM: " + strConsumoRam);
        System.out.println("Consumo de RAM (INT PGBAR): " + pgBarRam.intValue());
    }

    public static void informacoesDisco(Looca looca, Conversor conversor) {
        // Informações DISCO
        Long espacoDiscoTotal = looca.getGrupoDeDiscos().getVolumes().get(0).getTotal(); // Espaço Total do Disco
        Long espacoDiscoDisp = looca.getGrupoDeDiscos().getVolumes().get(0).getDisponivel(); // Espaço Disponível do Disco
        Long espacoDiscoUso = espacoDiscoTotal - espacoDiscoDisp; // Espaço Usado do Disco

        String strDiscoTotalGb = conversor.formatarBytes(espacoDiscoTotal); // Espaço Total do Disco
        String strDiscoDispGb = conversor.formatarBytes(espacoDiscoDisp); // Espaço Disponível do Disco
        String strDiscoUsadoGb = conversor.formatarBytes(espacoDiscoUso); // Espaço Usado do Disco

        Double consumoDisco = (espacoDiscoUso.doubleValue() * 100) / espacoDiscoTotal.doubleValue(); // Consumo de Disco em %
        Long pgBarDisco = Math.round(consumoDisco); // Consumo de Disco Arredondado para inserir no setValue() da ProgressBar
        String strConsumoDisco = String.format("%.1f %%", consumoDisco); // String Consumo de Disco para inserir no setString() da ProgressBar

        System.out.println("-".repeat(72));
        System.out.println("*** INFORMAÇÕES DO DISCO ***");
        System.out.println("Espaço Total: " + strDiscoTotalGb);
        System.out.println("Espaço Usado: " + strDiscoUsadoGb);
        System.out.println("Espaço Disponível: " + strDiscoDispGb);
        System.out.println("Consumo De Disco: " + strConsumoDisco);
        System.out.println("Consumo De Disco (INT PGBAR): " + pgBarDisco);
        System.out.println("-".repeat(72));
    }
}
