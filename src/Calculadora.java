import java.util.Scanner;

import Metodos.Division;
import Metodos.Modulo;
import Metodos.Multiplicacion;
import Metodos.Resta;
import Metodos.Suma;

public class Calculadora {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean continuar = true; // Variable para controlar el bucle

        while (continuar) { // Bucle para repetir operaciones
            double num1, num2;
            int op;

            System.out.println("Calculadora de Operaciones Básicas");
            System.out.print("Por favor, dame el primer número de la operación: ");
            num1 = sc.nextDouble();
            System.out.print("Por favor, dame el segundo número de la operación: ");
            num2 = sc.nextDouble();

            System.out.println("¿Qué operación desea hacer? (Solo coloque un número) \n" +
                    "1: Sumar\n" +
                    "2: Restar\n" +
                    "3: Multiplicar\n" +
                    "4: Dividir\n" +
                    "5: Módulo");
            op = sc.nextInt();

            switch (op) {
                case 1:
                    System.out.println("Resultado de la suma: " + Suma.sumar(num1, num2));
                    break;
                case 2:
                    System.out.println("Resultado de la resta: " + Resta.restar(num1, num2));
                    break;
                case 3:
                    System.out.println("Resultado de la multiplicación: " + Multiplicacion.multiplicar(num1, num2));
                    break;
                case 4:
                    if (num2 != 0) {
                        System.out.println("Resultado de la división: " + Division.dividir(num1, num2));
                    } else {
                        System.out.println(
                                "Dividir por cero no es posible. Asegúrate de ingresar un número distinto de cero como divisor.");
                    }
                    break;
                case 5:
                    if (num2 != 0) {
                        System.out.println("Resultado del módulo: " + Modulo.modular(num1, num2));
                    } else {
                        System.out.println(
                                "No se puede calcular el módulo con un divisor de cero. Por favor, ingresa un número distinto de cero.");
                    }
                    break;
                default:
                    System.out.println("¡Seleccione un número entre 1 y 5!");
                    break;
            }

            // Preguntar si desea realizar otra operación
            System.out.print("¿Desea realizar otra operación? (s/n): ");
            char respuesta = sc.next().charAt(0); // Leer la respuesta del usuario
            continuar = (respuesta == 's' || respuesta == 'S'); // Continuar si la respuesta es 's' o 'S'
        }
        System.out.println("Gracias por usar nuestra calculadora. ¡Hasta luego!");
    }
}
