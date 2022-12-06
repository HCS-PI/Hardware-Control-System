
package conexao.bd;

public class Dispositivo {
    private Integer id_dispositivo;
    private String tipo;
    private String modelo;
    private String unid_medida;
    private Integer fk_carro;

    public Integer getId_dispositivo() {
        return id_dispositivo;
    }

    public void setId_dispositivo(Integer id_dispositivo) {
        this.id_dispositivo = id_dispositivo;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getUnid_medida() {
        return unid_medida;
    }

    public void setUnid_medida(String unid_medida) {
        this.unid_medida = unid_medida;
    }

    public Integer getFk_carro() {
        return fk_carro;
    }

    public void setFk_carro(Integer fk_carro) {
        this.fk_carro = fk_carro;
    }
    
    
}
