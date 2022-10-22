
package conexao.bd;


public class Medida {
    
    private Integer id_medida;
    private String  horario_registro;
    private Double  valor;
    private Integer fk_dispositivo;

    public Integer getId_medida() {
        return id_medida;
    }

    public void setId_medida(Integer id_medida) {
        this.id_medida = id_medida;
    }

    public String getHorario_registro() {
        return horario_registro;
    }

    public void setHorario_registro(String horario_registro) {
        this.horario_registro = horario_registro;
    }

    public Double getValor() {
        return valor;
    }

    public void setValor(Double valor) {
        this.valor = valor;
    }

    public Integer getFk_dispositivo() {
        return fk_dispositivo;
    }

    public void setFk_dispositivo(Integer fk_dispositivo) {
        this.fk_dispositivo = fk_dispositivo;
    }
    
    
}
