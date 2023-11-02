
package domain;

public class Empleado extends Persona{
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados; // Es para incremetar
    
    
    //Constructores 
        //Constructores
    public Empleado(){ //Constructor 1
        this.idEmpleado = ++Empleado.contadorEmpleados; 
    }

    public Empleado(String nombre,double sueldo) {
        //super(nombre);
        this(); //De esta forma se llama al constructor interno (constuctor vacio)
        this.nombre = nombre;
        //De esta forma se puede usar super o this para el nombre (Pero no se pueden usar
        //los dos a la ves)
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }
    
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(",").append(super.toString());
        sb.append('}');
        return sb.toString();
    }

    
    
}
