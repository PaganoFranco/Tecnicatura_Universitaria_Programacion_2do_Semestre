
package Clases;

public class PruebaPersonas {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Franco";
        persona1.apellido = "Pagano";
        persona1.obtenerInformacion();
    }
}
