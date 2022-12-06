
package hcs.view;

public class Verificacao {
    private static Integer intVerificacao;
    private static String nomeVerificacao;

    public static String getNomeVerificacao() {
        return nomeVerificacao;
    }

    public void setNomeVerificacao(String nomeVerificacao) {
        Verificacao.nomeVerificacao = nomeVerificacao;
    }
    
    public static Integer getIntVerificacao() {
        return intVerificacao;
    }

    public void setIntVerificacao(Integer intVerificacao) {
        Verificacao.intVerificacao = intVerificacao;
    }
}
