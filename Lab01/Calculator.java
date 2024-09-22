import java.util.Scanner;
public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int primernum, segundonum, operador;
        String continuar;

        do {
            System.out.println("Ingrese el primer número");
            primernum = sc.nextInt();
            System.out.println("Ingrese el segundo número");
            segundonum = sc.nextInt();
            System.out.println("Ingrese el operador\n(1)Suma\n(2)Resta\n(3)Multiplicación\n(4)División\n(5)Módulo o resto");
            operador = sc.nextInt();

            switch (operador) {
                case 1:
                    System.out.println("La suma es: " + sum(primernum, segundonum));
                    break;
                case 2:
                    System.out.println("La resta es: " + sub(primernum, segundonum));
                    break;
                case 3:
                    System.out.println("La multiplicación es: " + mul(primernum, segundonum));
                    break;
                case 4:
                    if (segundonum == 0) {
                        System.out.println("División entre 0, INSTRUCCIÓN NO VÁLIDA");
                    } else {
                        System.out.println("La división es: " + div(primernum, segundonum));
                    }
                    break;
                case 5:
                    if (segundonum == 0) {
                        System.out.println("Módulo entre 0, INSTRUCCIÓN NO VÁLIDA");
                    } else {
                        System.out.println("El módulo o resto es: " + mod(primernum, segundonum));
                    }
                    break;
                default:
                    System.out.println("Instrucción inválida");
                    break;
            }

            System.out.println(" Escriba si quiere seguir calculando operaciones (s/n)");
            continuar = sc.next(); 
        } while (continuar.equalsIgnoreCase("s")); // Continúa si la respuesta es 's'

        sc.close(); // Cerrar el scanner al final
        System.out.println("GRACIAS por elegirnos. Nos vemos");
    }

    public static int sum(int a, int b) {
        return a + b;
    }

    public static int sub(int a, int b) {
        return a - b;
    }

    public static int mul(int a, int b) {
        return a * b;
    }

    public static int div(int a, int b) {
        return a / b;
    }

    public static int mod(int a, int b) {
        return a % b;
    }
}
