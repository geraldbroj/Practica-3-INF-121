package Persistencia_1;

public class main {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        try {
            ArchivoEmpleado archivo = new ArchivoEmpleado("empleados.dat");
            archivo.crearArchivo();
            archivo.guardarEmpleado(new Empleado("Ana", 30, 3500f));
            archivo.guardarEmpleado(new Empleado("Luis", 25, 4200f));

            System.out.println("Buscando Ana:");
            System.out.println(archivo.buscaEmpleado("Ana"));

            System.out.println("Buscando sueldo mayor a 4000:");
            System.out.println(archivo.mayorSalario(4000f));
        } catch (Exception e) {
            e.printStackTrace();
        }   
	}
}
