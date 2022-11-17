package conexao.bd;
import org.apache.commons.dbcp2.BasicDataSource;
import org.springframework.jdbc.core.JdbcTemplate;

public class DadosConexaoAWS {
    // ATRIBUTO
    private JdbcTemplate connection;

    // CONSTRUTOR
    public DadosConexaoAWS() {

        BasicDataSource dataSource2 = new BasicDataSource();

        dataSource2.setDriverClassName("com.mysql.jdbc.Driver");

        dataSource2.setUrl("jdbc:mysql://3.91.232.92:3306/hardware_control_system");

        dataSource2.setUsername("root");

        dataSource2.setPassword("urubu100");

        this.connection = new JdbcTemplate(dataSource2);

    }

    public JdbcTemplate getConnection() {
        return connection;
    }
}