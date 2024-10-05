package calculadora.pweb;

public class Calculadora {
	private int numero1;
	private int numero2;
	
	public Calculadora(int numero1,int numero2) {
		this.numero1=numero1;
		this.numero2=numero2;
	}
	public int sumar() {
		return numero1+numero2;
	}
	public int restar() {
		return numero1-numero2;
	}
	public int multiplicar() {
		return numero1*numero2;
	}
	public double dividir() {
		if(numero2==0) {
			System.out.println("La division entre 0 no esta permitida");
			return Double.NaN;
		}
		return (double)numero1/numero2;
	}
	public int modulo() {
		if(numero2==0) {
			System.out.println("El numero 2 no debe ser 0");
			return -1;
		}
		return numero1%numero2;
	}
}
