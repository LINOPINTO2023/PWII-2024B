import java.util.Scanner;
public class Calculator {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int primernum, segundonum, operador;
        System.out.println("Ingrese el primer número");
        primernum = sc.nextInt();
        System.out.println("Ingrese el segundo número");
        segundonum = sc.nextInt();
        System.out.println("Ingrese el operador\n(1)Suma\n(2)Resta\n(3)Multiplicación\n(4)División\n(5)Módulo o resto"); //falta agregae mas operaciones
        operador = sc.nextInt();
        switch (operador) {
            case 1:
            System.out.println("La suma es: "+ sum(primernum, segundonum));
                break;
            case 2:
            System.out.println("La resta es: "+ sum(primernum, segundonum));//falta el metodo de resta
            break;
            case 3:
            System.out.println("La multiplicacion es: "+ mul(primernum, segundonum));
            break;
            case 4:
            System.out.println("La division es: "+ div(primernum, segundonum));
            break;
            case 5:
            System.out.println("El módulo o resto es: "+ mod(primernum, segundonum));
            break;
            default:
            System.out.println("Instruccion Invalida");
            break;
        }
       
    }
    
    public static int sum(int a, int b){ 
        return a + b;
    }
    public static int sub(int a, int b){ 
        return a - b; 
    }
    public static int mul(int a, int b){
        return a * b; 
    }
    public static int div(int a, int b){ 
        return a / b;    
    }
    public static int mod(int a, int b){ 
        return a % b; 
    }
}
