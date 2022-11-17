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
                + dadosCpu.getConsumoCpu() + ", 1);");

        connectionAWS.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (now(),"
                + dadosCpu.getConsumoCpu() + ", 1);");
    }

    public void inserirDadosRam() {
        DadosMemoriaRam dadosRam = new DadosMemoriaRam();

        connection.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (CURRENT_TIMESTAMP,"
                + dadosRam.getConsumoRam() + ", 3);");

        connectionAWS.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (now(),"
                + dadosRam.getConsumoRam() + ", 3);");
    }

    public void inserirDadosDisco() {
        // Em desenvolvimento
    }
}
