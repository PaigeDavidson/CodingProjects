/**
 * Assignment 3 for CS 1410
 * This program determines if points are contained within circles or rectangles.
 */
import java.lang.Math;
public class Inside {
    /**
     * This is the primary driver code to test the "inside" capabilities of the
     * various functions.
     */
    public static void main(String[] args) {
        double[] ptX = { 1, 2, 3, 4 };
        double[] ptY = { 1, 2, 3, 4 };
        double[] circleX = { 0, 5 };
        double[] circleY = { 0, 5 };
        double[] circleRadius = { 3, 3 };
        double[] rectLeft = { -2.5, -2.5 };
        double[] rectTop = { 2.5, 5.0 };
        double[] rectWidth = { 6.0, 5.0 };
        double[] rectHeight = { 5.0, 2.5 };

        System.out.println("--- Report of Points and Circles ---");
        System.out.println();
        for(int i = 0; i < circleX.length; i++){
            for(int j = 0; j < ptX.length; j++){
                reportPoint(ptX[j], ptY[j]);
                if(isPointInsideCircle(ptX[j], ptY[j], circleX[i], circleY[i], circleRadius[i])){
                    System.out.print(" is inside ");
                }else{
                    System.out.print(" is outside ");
                }
                reportCircle(circleX[i], circleY[i], circleRadius[i]);
            }
        }
        System.out.println();
        System.out.println("--- Report of Points and Rectangles ---");
        System.out.println();
        for(int i = 0; i < rectTop.length; i++){
            for(int j = 0; j < ptX.length; j++){
                reportPoint(ptX[j], ptY[j]);
                if(isPointInsideRectangle(ptX[j], ptY[j], rectLeft[i], rectTop[i], rectWidth[i], rectHeight[i])){
                    System.out.print(" is inside ");
                }else{
                    System.out.print(" is outside ");
                }
                reportRectangle(rectLeft[i], rectTop[i], rectWidth[i], rectHeight[i]);
            }
        }

    }
    public static void reportPoint(double x, double y){
        System.out.print("Point(" + x + ", " + y + ")");
    }
    public static void reportCircle(double x, double y, double r){
        System.out.println("Circle(" + x + ", " + y + ") Radius: " + r);
    }
    public static void reportRectangle(double left, double top, double width, double height){
        double right = left + width;
        double bottom = top - height;
        System.out.println("Rectangle(" + left + ", " + top + ", " + right + ", " + bottom + ")");
    }
    public static boolean isPointInsideCircle(double ptX, double ptY, double circleX, double circleY, double circleRadius){
        double distance = Math.sqrt(Math.pow(ptX-circleX, 2) + Math.pow(ptY - circleY, 2));
        if(distance <= circleRadius){
            return true;
        }else{
            return false;
        }
    }
    public static boolean isPointInsideRectangle(double ptX, double ptY, double rLeft, double rTop, double rWidth, double rHeight){
        if(ptX >= rLeft && ptX <= (rWidth + rLeft) && ptY >= (rTop - rHeight) && ptY <= rTop){
            return true;
        }else{
            return false;
        }
    }

}
