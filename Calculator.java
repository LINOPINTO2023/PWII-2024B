import java.util.Scanner;
public class Calculator {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int primernum, segundonum, operador;
        System.out.println("Ingrese el primer número");
        primernum = sc.nextInt();
        System.out.println("Ingrese el segundo número");
        segundonum = sc.nextInt();
        System.out.println("Ingrese el operador\n(1)Suma\n(2)Resta\n(3)Multiplicación\n(4)División");
        operador = sc.nextInt();
        
        System.out.println("La suma es: "+ sum(primernum, segundonum));
    }
    
    public static int sum(int a, int b){ 
        return a + b;
    }
    int sub(int a, int b){ return 0; }
    int mul(int a, int b){
        return a * b; 
    }
    int div(int a, int b){ 
        return a / b;    
    }
    int mod(int a, int b){ return 0; }
}
