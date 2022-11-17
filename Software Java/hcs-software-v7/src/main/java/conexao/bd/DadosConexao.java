
package conexao.bd;

import org.apache.commons.dbcp2.BasicDataSource;
import org.springframework.jdbc.core.JdbcTemplate;

public class DadosConexao {
    // ATRIBUTO
    private JdbcTemplate connection;

    // CONSTRUTOR
    public DadosConexao() {

        BasicDataSource dataSource = new BasicDataSource();

        dataSource​.setDriverClassName("com.microsoft.sqlserver.jdbc.SQLServerDriver");

        dataSource​.setUrl("jdbc:sqlserver://hcs-bd.database.windows.net:1433;database=hcs-bd;user=hcs-Grupo09@hcs-bd;password=hardwareCSg9;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;");

        dataSource​.setUsername("hcs-Grupo09");

        dataSource​.setPassword("hardwareCSg9");

        this.connection = new JdbcTemplate(dataSource);

    }

    public JdbcTemplate getConnection() {
        return connection;
    }
}
