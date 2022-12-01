package hcs.coleta.dados;

import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.util.Conversor;

public class DadosTemperatura {
    
    Looca looca = new Looca();
    Conversor conversor = new Conversor();
    
    Double temperatura;
    
//      Código Base para coleta de Temperatura
//    public Double getTemperatura(){
//        Double temperatura = looca.getTemperatura().getTemperatura();
//        return temperatura;
//        return looca.getTemperatura().getTemperatura();
//    }
    
    public Double getTemperaturaCelsius(){
        Double temperatura = looca.getTemperatura().getTemperatura();
        Double celsius = temperatura;
        return celsius;
    }
    
    public Double getTemperaturaFaren(){
        Double temperatura = looca.getTemperatura().getTemperatura();
        Double faren = (temperatura * 1.8) + 32;
        return faren;
    }
    
    public Double getTemperaturaKelvin(){
        Double temperatura = looca.getTemperatura().getTemperatura();
        Double kelvin = temperatura + 273.15;
        return kelvin;
    }
}
