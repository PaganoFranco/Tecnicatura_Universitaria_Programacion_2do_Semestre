
package test;

public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2];
        System.out.println("edades = " + edades);
        
        edades[0][0] = 5; //LLenado manual
        edades[0][1] = 7; //Es una diferente columna
        edades[1][0] = 8; 
        edades[1][1] = 4;
        
        System.out.println("edades 0 * 0 = " + edades[0][0]);
        System.out.println("edades 0 * 1 = " + edades[0][1]);
        System.out.println("edades 1 * 0 = " + edades[1][0]);
        System.out.println("edades 1 * 1 = " + edades[1][1]);
        
    }
}
