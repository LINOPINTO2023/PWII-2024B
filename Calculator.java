import java.util.Scanner;

class Calculator{
    
    //metodos para las operaciones de la calculadora
    int rest(int a, int b){
        return a-b ;
    }
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Calculator chistematicos = new Calculator();
        
        System.out.print("Escriba el primer número: ");
        int a = sc.nextInt();

        System.out.print("Escriba el segundo número: ");
        int b = sc.nextInt();
        
        System.out.println("Escriba la operacion");
        System.out.println("suma[+], resta[-], multiplicaion[*], division[/], modulo[%] ");
        String operation = sc.next();

        System.out.println("El resultado es");
        //agregar logica para q imprima el resultado
    }

}
