package conexao.bd;

import org.apache.commons.dbcp2.BasicDataSource;
import org.springframework.jdbc.core.JdbcTemplate;

public class DadosConexaoAWS {

    // ATRIBUTO
    private JdbcTemplate connection;

    // CONSTRUTOR
    public DadosConexaoAWS() {

        BasicDataSource dataSource2 = new BasicDataSource();

        dataSource2.setDriverClassName("com.microsoft.sqlserver.jdbc.SQLServerDriver");

        dataSource2.setUrl("jdbc:sqlserver://hcs-bd.database.windows.net:1433;"
                + "database=hcs-bd;"
                + "user=hcs-Grupo09@hcs-bd;"
                + "password=hardwareCSg9;"
                + "encrypt=true;"
                + "trustServerCertificate=false;"
                + "hostNameInCertificate=*.database.windows.net;loginTimeout=30;");

        dataSource2.setUsername("hcs-Grupo09");

        dataSource2.setPassword("hardwareCSg9");

        this.connection = new JdbcTemplate(dataSource2);

    }

    public JdbcTemplate getConnection() {
        return connection;
    }
}
