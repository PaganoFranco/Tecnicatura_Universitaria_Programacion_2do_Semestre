
package teste;

public class TesteArreglos {
    public static void main(String[] args) {
        int edades [] = new int[3]; 
        //El lado izquiedo es donde declaramos la variable
        //EL lado derecho instanciamos un objeto de tipo Object
        System.out.println("edades = " + edades);
        
        //Modificar un elemento del arreglo
        edades[0] = 17;
        System.out.println("edades 0 = " + edades [0]);
        
        //Tarea 
        edades[1] = 24;
        System.out.println("edades 1 = " + edades[1]);
        edades[2] = 2;
        System.out.println("edades 2 = " + edades[2]);
    }
}
