
package test;

import domain.Persona;


public class PersonaPrueba {
    private int contador;
    
    public static void main(String[] args) {
        Persona persona1 = new Persona("Franco");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("Julieta");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
        //this.contador = 10; //No se puede referencias desde un contexto estatico
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.getContador());
    }
    
    static public void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
    
    public int getContador(){
        imprimir(new Persona("Juan"));
        return this.contador;
    }
}
 