import java.util.Scanner;

class Calculator{
    
    //metodos para las operaciones de la calculadora
    static int add(int a, int b){ 
		return 0; 
	} 
	
	static int rest(int a, int b){
        return a-b ;
    }

	static int mul(int a, int b){ 
		return 0; 
	
	} 
	static int div(int a, int b){ 
		return 0; 
	} 
	
	static int mod(int a, int b){
		return a % b;
	}

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
		boolean salir = false;
        Calculator chistematicos = new Calculator();
        
        System.out.print("Escriba el primer número: ");
        int a = sc.nextInt();

        System.out.print("Escriba el segundo número: ");
        int b = sc.nextInt();
		
		// calculadora, opciones de las operaciones disponibles
		while (!salir){
			System.out.println("\n=== CALCULATOR CHISTEMATICOS ===");
			System.out.println("1. suma[+]");
			System.out.println("2. resta[-]");
			System.out.println("3. multiplicacion[*]");
			System.out.println("4. division[/]");
			System.out.println("5. modulo[%]");
			System.out.println("6. SALIR");
			System.out.print("Seleccione una opcion (1, 2, 3, 4, 5, 6): ");
			int opcion = sc.nextInt();
			sc.nextLine();
			
			switch (opcion){
				case 1:
					System.out.println("\nSUMA: " + add(a, b));
					break;
				case 2:
					System.out.println("\nRESTA: " + rest(a, b));
					break;
				case 3:
					System.out.println("\nMULTIPLICACION: " + mul(a, b));
					break;
				case 4:
					System.out.println("\nDIVICION: " + div(a, b));
					break;
				case 5:
					System.out.println("\nMODULO: " + mod(a, b));
					break;
				case 6:
					salir = true;
					break;
				default:
					System.out.println("Opcion no válida. Por favor, seleccione una opcion valida.");
					break;
			}
		}
    }
}