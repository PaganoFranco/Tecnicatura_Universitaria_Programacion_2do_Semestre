
package test;

public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2];
        System.out.println("edades = " + edades);
        
        edades[0][0] = 5; //LLenado manual
        edades[0][1] = 7; //Es una diferente columna
        edades[1][0] = 8; 
        edades[1][1] = 4;
        edades[2][0] = 4;
        edades[2][1] = 4;
       
        
        System.out.println("edades 0 * 0 = " + edades[0][0]);
        System.out.println("edades 0 * 1 = " + edades[0][1]);
        System.out.println("edades 1 * 0 = " + edades[1][0]);
        System.out.println("edades 1 * 1 = " + edades[1][1]);
        System.out.println("edades 2 * 0 = " + edades[2][0]);
        System.out.println("edades 2 * 1 = " + edades[2][1]);
        
        
        for (int fila = 0; fila < edades.length; fila++) {
            for (int col = 0; col < edades[fila].length; col++) {
                System.out.println("edades " + fila+"-"+col+ ": " + edades[fila][col]);
            }
            
        }
    }
}
