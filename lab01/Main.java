package lab01;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        Scanner sc = new Scanner(System.in);
        System.out.println("Bienvenido a mi primer proyecto de Git Hub");
        System.out.println("SIMULADOR DE UNA CALCULADORA");

        System.out.println("Ingrese el primer numero: ");
        double num1 = sc.nextInt();

        System.out.println("Ingrese el segundo numero: ");
        double num2 = sc.nextInt();

        // Menú de operaciones
        System.out.println("Selecciona la operación:");
        System.out.println("1. Suma");
        System.out.println("2. Resta");
        System.out.println("3. Multiplicación");
        System.out.println("4. División");
        System.out.println("5. Módulo");

        int option = sc.nextInt(); //leer la opcion del usuario

        double resultado = 0;

        switch (option) {
            case 1:
                resultado = calculator.add(num1, num2);
                System.out.println("Resultado de la suma: " + resultado);
                break;
            case 2:
                resultado = calculator.sub(num1, num2);
                System.out.println("Resultado de la resta: " + resultado);
                break;
            case 3:
                resultado = calculator.mul(num1, num2);
                System.out.println("Resultado de la multiplicación: " + resultado);
                break;
            case 4:
                resultado = calculator.div(num1, num2);
                System.out.println("Resultado de la división: " + resultado);
                break;
            case 5:
                resultado = calculator.mod(num1, num2);
                System.out.println("Resultado del módulo: " + resultado);
                break;
            default:
                System.out.println("Opción no válida.");
        }
        sc.close();
    }
}
