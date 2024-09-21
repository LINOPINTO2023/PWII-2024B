package lab01;

class Calculator {
        int add(int a, int b) {
            return a + b;
        } 
        int sub(int a, int b) {
            return a - b;
        } 
        int mul(int a, int b) {
            return a * b;
        } 
        int div(int a, int b) {
            if (b == 0) {
                System.out.println("Error: No se puede dividir entre cero.");
                return 0;
            }
            return a / b;
        } 
    
        int mod(int a, int b) {
            if (b == 0) {
                System.out.println("Error: No se puede calcular el módulo con divisor cero.");
                return 0;
            }
            return a % b;
        }
}