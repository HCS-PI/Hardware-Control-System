
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

        dataSource​.setUrl("jdbc:mysql://localhost/teste_java");

        dataSource​.setUsername("root");

        dataSource​.setPassword("mdS5005jooj");

        this.connection = new JdbcTemplate(dataSource);

    }

    public JdbcTemplate getConnection() {
        return connection;
    }
}
