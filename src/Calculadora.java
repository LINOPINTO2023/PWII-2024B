import java.util.*;
class Calculadora{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double num1, num2;
        int op;
        System.out.println("Calculadora");
        System.out.println("Ingrese un numero");
        num1 = sc.nextDouble();
        System.out.println("Ingrese otro numero");
        num2 = sc.nextDouble();
        System.out.println("Elija una opcion: \n"+
                           "1: Suma\n"+
                           "2: Resta\n"+
                           "3: Multiplicacion\n"+
                           "4: Division\n"+
                           "5: Modulo\n");
        op = sc.nextInt();
        switch (op) {
            case 1: System.out.println("Resultado de la suma: "); break;
            case 2: System.out.println("Resultado de la resta: "); break;
            case 3: System.out.println("Resultado de la multiplicacion: "); break;
            case 4: 
                if (num2 != 0) {
                    System.out.println("Resultado de la división: " + division(num1, num2)); 
                } else {
                 System.out.println("Error: No se puede dividir entre cero.");
                }
                break;
            case 5:
            if (num2 != 0) {
                if (num2 != 0) {
                    System.out.println("Resultado del módulo: " + modulo(num1, num2)); 
                } else {
                    System.out.println("Error: No se puede calcular el módulo con divisor cero.");
                }
            break;
        }
    }

    public static double division(double a, double b) {
        return a / b;
    }
    public static double modulo(double a, double b) {
        return a % b;
    }
}
