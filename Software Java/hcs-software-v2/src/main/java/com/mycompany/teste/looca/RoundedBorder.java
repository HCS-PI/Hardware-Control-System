
package com.mycompany.teste.looca;

import java.awt.Component;
import java.awt.Graphics;
import java.awt.Insets;


import javax.swing.border.Border;

public class RoundedBorder {
    RoundedBorder() {
        
    }
    
    public static class RoundedBorderC implements Border {
        
        public int radius;
        
        RoundedBorderC(int radius) {
            this.radius = radius;
        }
        @Override
        public Insets getBorderInsets(Component c) {
            return new Insets(this.radius+1, this.radius+1, this.radius+2, this.radius);
        }

        @Override
        public boolean isBorderOpaque() {
            return true;
        }

        @Override
        public void paintBorder(Component c, Graphics g, int x, int y, int width, int height) {
            g.drawRoundRect(x,y,width-1,height-1,radius,radius);
        }
    }
}
