
package conexao.bd;

public class Carro {
    private Integer id_carro;
    private String endereco_mac;
    private String placa_carro;
    private String modelo;
    private Integer fk_empresa;

    public Integer getId_carro() {
        return id_carro;
    }

    public void setId_carro(Integer id_carro) {
        this.id_carro = id_carro;
    }

    public String getEndereco_mac() {
        return endereco_mac;
    }

    public void setEndereco_mac(String endereco_mac) {
        this.endereco_mac = endereco_mac;
    }

    public String getPlaca_carro() {
        return placa_carro;
    }

    public void setPlaca_carro(String placa_carro) {
        this.placa_carro = placa_carro;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public Integer getFk_empresa() {
        return fk_empresa;
    }

    public void setFk_empresa(Integer fk_empresa) {
        this.fk_empresa = fk_empresa;
    }
    
    
}
