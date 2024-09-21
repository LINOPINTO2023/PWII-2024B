package lab01;

class Calculator {
        double add(double a, double b) {
            return a + b;
        } 
        double sub(double a, double b) {
            return a - b;
        } 
        double mul(double a, double b) {
            return a * b;
        } 
        double div(double a, double b) {
            if (b == 0) {
                System.out.println("Error: No se puede dividir entre cero.");
                return 0;
            }
            return a / b;
        } 
    
        double mod(double a, double b) {
            if (b == 0) {
                System.out.println("Error: No se puede calcular el módulo con divisor cero.");
                return 0;
            }
            return a % b;
        }
}