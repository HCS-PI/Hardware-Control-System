
package hcs.view;

import com.github.britooo.looca.api.core.Looca;
import com.github.britooo.looca.api.util.Conversor;
import conexao.bd.DadosConexao;
import hcs.coleta.dados.DadosCpu;
import hcs.coleta.dados.DadosDisco;
import hcs.coleta.dados.DadosMemoriaRam;
import hcs.coleta.dados.DadosSistema;
import hcs.coleta.dados.InserirDados;
import java.awt.Image;
import java.awt.Toolkit;
import java.net.URL;
import java.util.Timer;
import java.util.TimerTask;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;
import org.springframework.jdbc.core.JdbcTemplate;

/**
 *
 * @author VAV02
 */
public class Dashboard extends javax.swing.JFrame {

    /**
     * Creates new form Dashboard
     */
    public Dashboard() {
        try {
            UIManager.setLookAndFeel(UIManager.getCrossPlatformLookAndFeelClassName());
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(Dashboard.class.getName()).log(Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            Logger.getLogger(Dashboard.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            Logger.getLogger(Dashboard.class.getName()).log(Level.SEVERE, null, ex);
        } catch (UnsupportedLookAndFeelException ex) {
            Logger.getLogger(Dashboard.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        URL caminhoIcone = getClass().getResource("/assets/hcs.png");
        Image iconeTitulo = Toolkit.getDefaultToolkit().getImage(caminhoIcone);
        this.setIconImage(iconeTitulo);
        
        initComponents();

        Looca looca = new Looca();
        Conversor conversor = new Conversor();
        
        DadosCpu dadosCpu = new DadosCpu();
        DadosMemoriaRam dadosRam = new DadosMemoriaRam();
        
        InserirDados insertDados = new InserirDados();

        informacoesSitesma();
        informacoesCpu();
        informacoesDisco();
        informacoesRam();

        Timer temporizador = new Timer();
        TimerTask task = new TimerTask() {
            @Override
            public void run() {
                consumoCpuRealTime();
                consumoRamRealTime();
                insertDados.inserirDadosCpu();
                insertDados.inserirDadosRam();
                
            }
        };

        temporizador.schedule(task, 0, 1000);

    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        lblSo = new javax.swing.JLabel();
        lblTempoAtv = new javax.swing.JLabel();
        lblArquitetura = new javax.swing.JLabel();
        pgBarDisco = new javax.swing.JProgressBar();
        lblDiscoTotal = new javax.swing.JLabel();
        lblDiscoUso = new javax.swing.JLabel();
        lblDiscoDisp = new javax.swing.JLabel();
        pgBarRam = new javax.swing.JProgressBar();
        lblRamTotal = new javax.swing.JLabel();
        lblRamUso = new javax.swing.JLabel();
        lblRamDisp = new javax.swing.JLabel();
        pgBarCpu = new javax.swing.JProgressBar();
        lblNucleosFisicos = new javax.swing.JLabel();
        lblNucleosVirtuais = new javax.swing.JLabel();
        lblThreads = new javax.swing.JLabel();
        lblModelo = new javax.swing.JLabel();
        panelHeader = new javax.swing.JPanel();
        jLabel4 = new javax.swing.JLabel();
        panelMenu = new javax.swing.JPanel();
        jButton1 = new javax.swing.JButton();
        jButton2 = new javax.swing.JButton();
        jButton3 = new javax.swing.JButton();
        jButton4 = new javax.swing.JButton();
        jButton5 = new javax.swing.JButton();
        panelHome = new javax.swing.JPanel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();

        lblSo.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblSo.setForeground(new java.awt.Color(255, 255, 102));

        lblTempoAtv.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblTempoAtv.setForeground(new java.awt.Color(255, 255, 102));
        lblTempoAtv.setText("0 Days, 14:25:36");

        lblArquitetura.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblArquitetura.setForeground(new java.awt.Color(255, 255, 102));

        pgBarDisco.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        pgBarDisco.setForeground(new java.awt.Color(0, 153, 0));
        pgBarDisco.setStringPainted(true);

        lblDiscoTotal.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblDiscoTotal.setForeground(new java.awt.Color(51, 255, 51));
        lblDiscoTotal.setText("0");

        lblDiscoUso.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblDiscoUso.setForeground(new java.awt.Color(51, 255, 51));
        lblDiscoUso.setText("0");

        lblDiscoDisp.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblDiscoDisp.setForeground(new java.awt.Color(51, 255, 51));
        lblDiscoDisp.setText("0");

        pgBarRam.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        pgBarRam.setForeground(new java.awt.Color(112, 36, 181));
        pgBarRam.setStringPainted(true);

        lblRamTotal.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblRamTotal.setForeground(new java.awt.Color(112, 36, 181));
        lblRamTotal.setText("0");

        lblRamUso.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblRamUso.setForeground(new java.awt.Color(112, 36, 181));
        lblRamUso.setText("0");

        lblRamDisp.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblRamDisp.setForeground(new java.awt.Color(112, 36, 181));
        lblRamDisp.setText("0");

        pgBarCpu.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        pgBarCpu.setForeground(new java.awt.Color(73, 167, 222));
        pgBarCpu.setStringPainted(true);

        lblNucleosFisicos.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblNucleosFisicos.setForeground(new java.awt.Color(0, 244, 244));
        lblNucleosFisicos.setText("0");

        lblNucleosVirtuais.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblNucleosVirtuais.setForeground(new java.awt.Color(0, 244, 244));
        lblNucleosVirtuais.setText("0");

        lblThreads.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        lblThreads.setForeground(new java.awt.Color(0, 244, 244));
        lblThreads.setText("12");

        lblModelo.setFont(new java.awt.Font("Segoe UI", 1, 12)); // NOI18N
        lblModelo.setForeground(new java.awt.Color(0, 244, 244));
        lblModelo.setText("Modelo");

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Hardware Control System - Dashboard Sistema");
        setBackground(new java.awt.Color(204, 204, 255));
        setResizable(false);
        setSize(new java.awt.Dimension(800, 600));
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        panelHeader.setBackground(new java.awt.Color(4, 30, 84));
        panelHeader.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel4.setFont(new java.awt.Font("Microsoft New Tai Lue", 1, 30)); // NOI18N
        jLabel4.setForeground(new java.awt.Color(255, 255, 255));
        jLabel4.setText("Hardware Control System");
        jLabel4.setPreferredSize(new java.awt.Dimension(250, 250));
        panelHeader.add(jLabel4, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 10, 500, 40));

        getContentPane().add(panelHeader, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 920, 60));

        panelMenu.setBackground(new java.awt.Color(9, 22, 112));
        panelMenu.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jButton1.setBackground(new java.awt.Color(26, 119, 213));
        jButton1.setFont(new java.awt.Font("Ebrima", 1, 14)); // NOI18N
        jButton1.setForeground(new java.awt.Color(255, 255, 255));
        jButton1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/assets/thermometerIconWhite.png"))); // NOI18N
        jButton1.setText("TEMP ");
        jButton1.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        jButton1.setRolloverEnabled(false);
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        panelMenu.add(jButton1, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 410, 140, 70));

        jButton2.setBackground(new java.awt.Color(26, 119, 213));
        jButton2.setFont(new java.awt.Font("Ebrima", 1, 14)); // NOI18N
        jButton2.setForeground(new java.awt.Color(255, 255, 255));
        jButton2.setIcon(new javax.swing.ImageIcon(getClass().getResource("/assets/managementIconWhite.png"))); // NOI18N
        jButton2.setText("SISTEMA");
        jButton2.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        jButton2.setRolloverEnabled(false);
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });
        panelMenu.add(jButton2, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 10, 140, 70));

        jButton3.setBackground(new java.awt.Color(26, 119, 213));
        jButton3.setFont(new java.awt.Font("Ebrima", 1, 14)); // NOI18N
        jButton3.setForeground(new java.awt.Color(255, 255, 255));
        jButton3.setIcon(new javax.swing.ImageIcon(getClass().getResource("/assets/cpuIconWhite.png"))); // NOI18N
        jButton3.setText("CPU");
        jButton3.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        jButton3.setRolloverEnabled(false);
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });
        panelMenu.add(jButton3, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 110, 140, 70));

        jButton4.setBackground(new java.awt.Color(26, 119, 213));
        jButton4.setFont(new java.awt.Font("Ebrima", 1, 14)); // NOI18N
        jButton4.setForeground(new java.awt.Color(255, 255, 255));
        jButton4.setIcon(new javax.swing.ImageIcon(getClass().getResource("/assets/hardDiscIconWhite.png"))); // NOI18N
        jButton4.setText("DISCO");
        jButton4.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        jButton4.setRolloverEnabled(false);
        jButton4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton4ActionPerformed(evt);
            }
        });
        panelMenu.add(jButton4, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 210, 140, 70));

        jButton5.setBackground(new java.awt.Color(26, 119, 213));
        jButton5.setFont(new java.awt.Font("Ebrima", 1, 14)); // NOI18N
        jButton5.setForeground(new java.awt.Color(255, 255, 255));
        jButton5.setIcon(new javax.swing.ImageIcon(getClass().getResource("/assets/ramIconWhite.png"))); // NOI18N
        jButton5.setText("RAM");
        jButton5.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        jButton5.setRolloverEnabled(false);
        jButton5.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton5ActionPerformed(evt);
            }
        });
        panelMenu.add(jButton5, new org.netbeans.lib.awtextra.AbsoluteConstraints(20, 310, 140, 70));

        getContentPane().add(panelMenu, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 60, 180, 520));

        panelHome.setBackground(new java.awt.Color(110, 124, 255));
        panelHome.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel2.setFont(new java.awt.Font("Microsoft New Tai Lue", 1, 120)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(255, 255, 255));
        jLabel2.setText("VINDO");
        jLabel2.setPreferredSize(new java.awt.Dimension(250, 250));
        panelHome.add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(190, 190, 430, 190));

        jLabel3.setIcon(new javax.swing.ImageIcon(getClass().getResource("/assets/hc2white.png"))); // NOI18N
        jLabel3.setPreferredSize(new java.awt.Dimension(250, 250));
        panelHome.add(jLabel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(430, 100, 180, 140));

        jLabel5.setFont(new java.awt.Font("Microsoft New Tai Lue", 1, 120)); // NOI18N
        jLabel5.setForeground(new java.awt.Color(255, 255, 255));
        jLabel5.setText("BEM");
        jLabel5.setPreferredSize(new java.awt.Dimension(250, 250));
        panelHome.add(jLabel5, new org.netbeans.lib.awtextra.AbsoluteConstraints(170, 90, 430, 190));

        getContentPane().add(panelHome, new org.netbeans.lib.awtextra.AbsoluteConstraints(180, 60, 740, 520));

        pack();
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton3ActionPerformed
        new Cpu().setVisible(true);
        this.dispose();
    }//GEN-LAST:event_jButton3ActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        new Sistema().setVisible(true);
        this.dispose();
    }//GEN-LAST:event_jButton2ActionPerformed

    private void jButton4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton4ActionPerformed
        new Disco().setVisible(true);
        this.dispose();
    }//GEN-LAST:event_jButton4ActionPerformed

    private void jButton5ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton5ActionPerformed
        new Ram().setVisible(true);
        this.dispose();
    }//GEN-LAST:event_jButton5ActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        new Temp().setVisible(true);
        this.dispose();
    }//GEN-LAST:event_jButton1ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Dashboard.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Dashboard.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Dashboard.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Dashboard.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Dashboard().setVisible(true);
            }
        });
    }
    
    public void consumoCpuRealTime(){
        DadosCpu dadosCpu = new DadosCpu();
        
        pgBarCpu.setValue(dadosCpu.getConsumoCpu().intValue());
        
        
    }
    public void consumoRamRealTime(){
        DadosMemoriaRam dadosRam = new DadosMemoriaRam();
        
        pgBarRam.setValue(dadosRam.getConsumoRam().intValue());
    }   
    
    public void informacoesSitesma() {
        // Informações Sistema
        DadosSistema dadosSistema = new DadosSistema();
        
        lblSo.setText(dadosSistema.getSistemaOperacional());
        
        //lblFabricante.setText(dadosSistema.getFabricanteSistema());
        
        lblArquitetura.setText(dadosSistema.getArquiteturaSistema());
        
        lblTempoAtv.setText(dadosSistema.getTempoAtvSistema());
    }

    public void informacoesCpu() {
        // Informações CPU
        DadosCpu dadosCpu = new DadosCpu();
        
        lblModelo.setText(dadosCpu.getModeloCpu());
        
        lblNucleosFisicos.setText(dadosCpu.getQtdNucleosFisicos().toString());
        
        lblNucleosVirtuais.setText(dadosCpu.getQtdNucleosVirtuais().toString());
        
        lblThreads.setText(dadosCpu.getQtdTotalNucleos().toString());
        

    }

    public void informacoesDisco() {
        // Informações DISCO
        DadosDisco dadosDisco = new DadosDisco();
 
        lblDiscoTotal.setText(dadosDisco.getStrDiscoTotalGb());
        
        lblDiscoUso.setText(dadosDisco.getStrDiscoUsadoGb());
        
        lblDiscoDisp.setText(dadosDisco.getStrDiscoDispGb());

        pgBarDisco.setValue(dadosDisco.getConsumoDisco().intValue());
        
    }

    public void informacoesRam() {
        // Informações RAM
        DadosMemoriaRam dadosRam = new DadosMemoriaRam();
        
        lblRamTotal.setText(dadosRam.getMemoriaTotalGb());
        
        lblRamUso.setText(dadosRam.getMemoriaUsoGb());
        
        lblRamDisp.setText(dadosRam.getMemoriaDisponivelGb());

    }   
    
//    public void tempAtvRealTime(Looca looca, Conversor conversor) {
//        String tempoAtvSistema = conversor.formatarSegundosDecorridos(looca.getSistema().getTempoDeAtividade());
//        lblTempoAtv.setText(tempoAtvSistema);
//    }
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButton4;
    private javax.swing.JButton jButton5;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel lblArquitetura;
    private javax.swing.JLabel lblDiscoDisp;
    private javax.swing.JLabel lblDiscoTotal;
    private javax.swing.JLabel lblDiscoUso;
    private javax.swing.JLabel lblModelo;
    private javax.swing.JLabel lblNucleosFisicos;
    private javax.swing.JLabel lblNucleosVirtuais;
    private javax.swing.JLabel lblRamDisp;
    private javax.swing.JLabel lblRamTotal;
    private javax.swing.JLabel lblRamUso;
    private javax.swing.JLabel lblSo;
    private javax.swing.JLabel lblTempoAtv;
    private javax.swing.JLabel lblThreads;
    private javax.swing.JPanel panelHeader;
    private javax.swing.JPanel panelHome;
    private javax.swing.JPanel panelMenu;
    private javax.swing.JProgressBar pgBarCpu;
    private javax.swing.JProgressBar pgBarDisco;
    private javax.swing.JProgressBar pgBarRam;
    // End of variables declaration//GEN-END:variables
}
