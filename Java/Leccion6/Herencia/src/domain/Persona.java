
package domain;

public class Persona {
    //Atributos de herencia
    protected String nombre;
    protected char gener;
    protected int edad;
    protected String direccion;
    
    //Constructor vacio: este es para crear objetos sin necesidad de inicializar
    //los atributos de la clase
    public Persona(){ //Constructor 1
        
    }
    
    public Persona(String nombre){ //Constructor 2
        this.nombre = nombre;
    }

    public Persona(String nombre, char gener, int edad, String direccion) {
        this.nombre = nombre;
        this.gener = gener;
        this.edad = edad;
        this.direccion = direccion;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGener() {
        return this.gener;
    }

    public void setGener(char gener) {
        this.gener = gener;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getDireccion() {
        return this.direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", gener=" + gener + ", edad=" + edad + ", direccion=" + direccion + '}';
    }
    
}
