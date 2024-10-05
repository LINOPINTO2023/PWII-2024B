package calculadora.pweb;

public class Main {
	public static void main(String[] args) {
		Calculadora calcular= new Calculadora(150,0);
		System.out.println("La suma es: "+calcular.sumar());
		System.out.println("La resta es: "+calcular.restar());
		System.out.println("La divison es: "+calcular.dividir());
		System.out.println("La multiplicacion es: "+calcular.multiplicar());
		System.out.println("El modulo es: "+calcular.modulo());
		
		System.out.println();
		
		Calculadora calcular1= new Calculadora(10,50);
		System.out.println("La suma es: "+calcular1.sumar());
		System.out.println("La resta es: "+calcular1.restar());
		System.out.println("La divison es: "+calcular1.dividir());
		System.out.println("La multiplicacion es: "+calcular1.multiplicar());
		System.out.println("El modulo es: "+calcular1.modulo());
	}
}
