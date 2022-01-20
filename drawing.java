import java.awt.Color;
import java.awt.Canvas;
import java .awt.Graphics;
import javax.swing.JFrame;
class drawing{
	void main(){
		int windowSize = 800;
		JFrame frame = new JFrame("CS 112 Recursive Graphics");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setBackground(Color.WHITE);
		frame.pack();
		frame.setVisible(true);
		drawline((int)(windowSize/4),(int)(windowSize/4),(int)(windowSize*3/4),(int)(windowSize*3/4));
		 
    }
    public void drawLine(double x1, double y1, double x2, double y2, Graphics g) {
		 	g.drawLine(round(x1),round(y1),round(x2), round(y2));
		 }
}
