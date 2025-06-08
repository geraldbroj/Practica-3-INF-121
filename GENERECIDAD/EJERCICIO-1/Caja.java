//package Generecidad_1;

class Caja <T> {
	private T cont;
	public void guardar(T cont) {
		this.cont = cont;
	}
	public T obtener() {
		return cont;
	}
	public static void main(String[] args) {
		Caja<String> cajaDeTexto = new Caja<>();
		cajaDeTexto.guardar("holaa");
		
		Caja<Integer> cajaDeEntero = new Caja<>();
		cajaDeEntero.guardar(1243);
		System.out.println("contentide de caja texto "+ cajaDeTexto.obtener());
		System.out.println("Contednido de caja entero "+ cajaDeTexto.obtener());
	}
}
