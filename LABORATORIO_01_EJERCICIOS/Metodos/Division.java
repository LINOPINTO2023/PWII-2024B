package Metodos;

/**
 * Método para dividir dos números.
 * 
 * @param num1 El dividendo.
 * @param num2 El divisor.
 * @return El resultado de dividir num1 entre num2. Devuelve double.
 * @throws ArithmeticException Si num2 es cero.
 */
public class Division {
    public static double dividir(double num1, double num2) {
        if (num2 == 0) {
            throw new ArithmeticException("No se puede dividir entre cero.");
        }
        return num1 / num2;
    }
}
