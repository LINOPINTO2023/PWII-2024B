import java.util.InputMismatchException;
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

        System.out.println("Calculadora de Operaciones Básicas");
        System.out.println("====================================");
        while (continuar) { 
            double num1 = 0, num2 = 0;
            int op = 0; // Inicializar variable de operación

            boolean inputValido = false; // Control de la entrada

            while (!inputValido) {
                try {
                    System.out.print("Ingrese el primer operando: ");
                    num1 = sc.nextDouble();
                    inputValido = true;
                } catch (InputMismatchException e) {
                    System.out.println("Error: Debes ingresar un número válido.");
                    sc.next(); // Limpiar la entrada incorrecta
                }
            }

            inputValido = false;

            while (!inputValido) {
                try {
                    System.out.print("Ingrese el segundo operando: ");
                    num2 = sc.nextDouble();
                    inputValido = true; 
                } catch (InputMismatchException e) {
                    System.out.println("Error: Debes ingresar un número válido.");
                    sc.next(); // Limpiar la entrada incorrecta
                }
            }

            System.out.println("¿Qué operación desea hacer? (Solo coloque un número) \n" +
                    "1: Sumar\n" +
                    "2: Restar\n" +
                    "3: Multiplicar\n" +
                    "4: Dividir\n" +
                    "5: Módulo");
            op = sc.nextInt();

            double resultado = 0;
            boolean esEntero = false; // Variable para determinar si el resultado es entero

            switch (op) {
                case 1:
                    resultado = Suma.sumar(num1, num2);
                    break;
                case 2:
                    resultado = Resta.restar(num1, num2);
                    break;
                case 3:
                    resultado = Multiplicacion.multiplicar(num1, num2);
                    break;
                case 4:
                    if (num2 != 0) {
                        resultado = Division.dividir(num1, num2);
                    } else {
                        System.out.println(
                                "Dividir por cero no es posible. Asegúrate de ingresar un número distinto de cero como divisor.");
                        continue;
                    }
                    break;
                case 5:
                    if (num2 != 0) {
                        resultado = Modulo.modulo(num1, num2);
                    } else {
                        System.out.println(
                                "No se puede calcular el módulo con un divisor de cero. Por favor, ingresa un número distinto de cero.");
                        continue;
                    }
                    break;
                default:
                    System.out.println("¡Seleccione un número entre 1 y 5!");
                    continue;
            }

            // Verificar si el resultado es un número entero
            if (resultado % 1 == 0) {
                esEntero = true;
            }

            // Imprimir el resultado de acuerdo al tipo (entero o decimal)
            if (esEntero) {
                System.out.println("Resultado: " + (int) resultado);
            } else {
                System.out.println("Resultado: " + resultado);
            }

            // Preguntar si desea realizar otra operación
            System.out.print("¿Desea realizar otra operación? (s/n): ");
            char respuesta = sc.next().charAt(0); // Leer la respuesta del usuario
            continuar = (respuesta == 's' || respuesta == 'S'); // Continuar si la respuesta es 's' o 'S'
        }
        System.out.println("Gracias por usar nuestra calculadora. ¡Hasta luego!");
    }
}
