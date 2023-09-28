
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        int a = 10; // Creamos variables locales
        int b = 7; //Memoria stack
        miMetodo(); //Llamamos al metodo nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        // aritmetica1 = null; No se usa mas que para eliminar todo y limpiar
        aritmetica1.sumarNumeros();
        //Para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = " + resultado);
       
        System.out.println("aritmetica a: "+aritmetica1.a);
        System.out.println("aritmetica a: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        // aritmetica1 = null; Tampoco se usa al final, ya que al final se limpia solo
        // System.gc(); Este comando es un recolector de basura (pero tampco se usa)
        Persona persona = new Persona("Franco","Pagano");
        System.out.println("persona nombre = " + persona.nombe);
        System.out.println("persona apeliido = " + persona.apellido);
    }
    // Modularidad creamos un nuevo metodo
    public static void miMetodo(){
        int a = 10; //Una variable esta limitada 
        System.out.println("Aqui hay otro método");
    }
}


class Persona{
    String nombe;
    String apellido;
    
    Persona(String nombre, String apellido){ //Constructor
        this.nombe = nombre;
        this.apellido = apellido;
    }
}