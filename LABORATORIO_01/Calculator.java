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
            throw new ArithmeticException("Indefinido: división por cero");
        }
        return a / b;
    }

    int mod(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Indefinido: módulo por cero");
        }
        return a % b;
    }

    public static void main(String[] args) {
        Calculator calcular = new Calculator();

        try {
            int suma = calcular.add(10, 5);
            System.out.println("Suma: " + suma);

            int resta = calcular.sub(10, 5);
            System.out.println("Resta: " + resta);

            int multiplicacion = calcular.mul(10, 5);
            System.out.println("Multiplicación: " + multiplicacion);

            int division = calcular.div(10, 2);
            System.out.println("División: " + division);

            int modulo = calcular.mod(10, 3);
            System.out.println("Módulo: " + modulo);

        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
        }
    }
}
