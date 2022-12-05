package hcs.coleta.dados;

import conexao.bd.DadosConexao;
import conexao.bd.DadosConexaoAWS;
import org.springframework.jdbc.core.JdbcTemplate;

public class InserirDados {

    DadosConexao database = new DadosConexao();

    JdbcTemplate connection = database.getConnection();

    DadosConexaoAWS databaseAWS = new DadosConexaoAWS();

    JdbcTemplate connectionAWS = databaseAWS.getConnection();
    Pipefy pipefy = new Pipefy();

    public void inserirDadosCpu() {
        String descricaoCpu;
        DadosCpu dadosCpu = new DadosCpu();

        connection.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (CURRENT_TIMESTAMP,"
                + dadosCpu.getConsumoCpu() + ", 5);");

        connectionAWS.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (now(),"
                + dadosCpu.getConsumoCpu() + ", 5);");

        if (dadosCpu.getConsumoCpu() > 70 && dadosCpu.getConsumoCpu() < 90) {
            descricaoCpu = String.format("O carro está com a cpu em %.1f%%", dadosCpu.getConsumoCpu());
            pipefy.criarCards("Novo carro em estado de alerta", descricaoCpu);
        } else if (dadosCpu.getConsumoCpu() > 90) {
            descricaoCpu = String.format("O carro está com a cpu em %.1f%%", dadosCpu.getConsumoCpu());
            pipefy.criarCards("Novo carro em estado CRITICO", descricaoCpu);
        }
    }

    public void inserirDadosRam() {
        String descricaoRam;
        DadosMemoriaRam dadosRam = new DadosMemoriaRam();

        connection.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (CURRENT_TIMESTAMP,"
                + dadosRam.getConsumoRam() + ", 7);");

        connectionAWS.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (now(),"
                + dadosRam.getConsumoRam() + ", 7);");

        if (dadosRam.getConsumoRam() > 70 && dadosRam.getConsumoRam() < 90) {
            descricaoRam = String.format("O carro está com a ram em %.1f%%", dadosRam.getConsumoRam());
            pipefy.criarCards("Novo carro em estado de alerta", descricaoRam);
        } else if (dadosRam.getConsumoRam() > 90) {
            descricaoRam = String.format("O carro está com a ram em %.1f%%", dadosRam.getConsumoRam());
            pipefy.criarCards("Novo carro em estado CRITICO", descricaoRam);
        }
    }

    public void inserirDadosDisco() {
        // Em desenvolvimento
    }

    public void inserirDadosTemperatura() {
        DadosTemperatura dadosTemp = new DadosTemperatura();

        connection.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (CURRENT_TIMESTAMP,"
                + dadosTemp.getTemperaturaCelsius() + ", 6);");

        connectionAWS.update("insert into Medida(horario_registro,valor,fk_dispositivo) values (now(),"
                + dadosTemp.getTemperaturaCelsius() + ", 6);");
    }
}
