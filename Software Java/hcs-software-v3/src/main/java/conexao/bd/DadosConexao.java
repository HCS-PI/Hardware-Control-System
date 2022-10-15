
package conexao.bd;

import org.apache.commons.dbcp2.BasicDataSource;
import org.springframework.jdbc.core.JdbcTemplate;

public class DadosConexao {
    // ATRIBUTO
    private JdbcTemplate connection;

    // CONSTRUTOR
    public DadosConexao() {

        BasicDataSource dataSource = new BasicDataSource();

        dataSource​.setDriverClassName("com.mysql.jdbc.Driver");

        dataSource​.setUrl("jdbc:mysql://localhost/hardware_control_system");

        dataSource​.setUsername("root");

        dataSource​.setPassword("Vini_0507");

        this.connection = new JdbcTemplate(dataSource);

    }

    public JdbcTemplate getConnection() {
        return connection;
    }
}
