
package CicloWhile;

public class EjercicioWhile {
    public static void main(String[] args) {
        // Ciclo While
        var conteo = 0; //Inferencia de tipos
        while(conteo < 7){
            System.out.println("conteo = "+conteo);
            conteo++; //Vamos a aumentar en un uno la variable 
        }
        //Ciclo Do While
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador ++;
        }while(contador < 7);
        //Ciclo For
        for(var contando = 0; contando < 7; contando++){
             System.out.println("contando = " + contando);
            }
        //Rompe Ciclos - BRACK
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 ==0 ) {
             System.out.println("contando = " + contando);
             break;
            }
        }
        //Rome Ciclos - BRACK
        for(var contando = 0; contando < 7; contando++){
            if(contando % 2 ==0 ) {
             continue;
            }
            System.out.println("contando = " + contando);
        }
    }
}
