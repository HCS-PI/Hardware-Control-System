package hcs.coleta.dados;

import conexao.bd.DadosConexao;
import conexao.bd.DadosConexaoAWS;
import org.springframework.jdbc.core.JdbcTemplate;

public class InserirDados {

    DadosConexao database = new DadosConexao();

    JdbcTemplate connection = database.getConnection();

    DadosConexaoAWS databaseAWS = new DadosConexaoAWS();

    JdbcTemplate connectionAWS = databaseAWS.getConnection();

    public void inserirDadosCpu() {
        DadosCpu dadosCpu = new DadosCpu();

        connection.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (CURRENT_TIMESTAMP,"
                + dadosCpu.getConsumoCpu() + ", 5);");

        connectionAWS.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (now(),"
                + dadosCpu.getConsumoCpu() + ", 5);");
    }

    public void inserirDadosRam() {
        DadosMemoriaRam dadosRam = new DadosMemoriaRam();

        connection.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (CURRENT_TIMESTAMP,"
                + dadosRam.getConsumoRam() + ", 7);");

        connectionAWS.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (now(),"
                + dadosRam.getConsumoRam() + ", 7);");
    }

    public void inserirDadosDisco() {
        // Em desenvolvimento
    }

    public void inserirDadosTemperatura(){
        DadosTemperatura dadosTemp = new DadosTemperatura();

        connection.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (CURRENT_TIMESTAMP,"
                + dadosTemp.getTemperaturaCelsius() + ", 6);");

        connectionAWS.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (now(),"
                + dadosTemp.getTemperaturaCelsius() + ", 6);");
    }
}
