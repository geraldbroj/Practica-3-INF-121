package Persistencia_5;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ArchFarmacia arch = new ArchFarmacia("farmacias.dat");
        arch.crearArchivo();

        ArrayList<Medicamento> meds1 = new ArrayList<>();
        meds1.add(new Medicamento("Golpex", 1, "Tos", 12.5));
        meds1.add(new Medicamento("Resfrix", 2, "Resfrio", 9.0));

        ArrayList<Medicamento> meds2 = new ArrayList<>();
        meds2.add(new Medicamento("Bronquix", 3, "Tos", 8.0));
        meds2.add(new Medicamento("Paracetamol", 4, "Fiebre", 7.0));

        Farmacia f1 = new Farmacia("Salud Total", 101, "Calle 1, Zona Central", meds1);
        Farmacia f2 = new Farmacia("Farmacia Plus", 202, "Av. Siempre Viva 742", meds2);

        arch.adicionar(f1);
        arch.adicionar(f2);

        System.out.println("--- Listar farmacias ---");
        arch.listar();

        System.out.println("\n--- Medicamentos para resfríos ---");
        arch.mostrarMedicamentosResfrios();

        System.out.println("\n--- Precio total medicamentos para la tos ---");
        System.out.println(arch.precioMedicamentoTos());

        System.out.println("\n--- Medicamentos para la tos con precio < 10 ---");
        arch.mostrarMedicamentosMenorTos();

        System.out.println("\n--- Medicamentos para la tos en sucursal 202 ---");
        arch.mostrarMedicamentosSucursalTos(202);

        System.out.println("\n--- Buscar sucursal con medicamento 'Golpex' ---");
        arch.buscarSucursalConMedicamento("Golpex");
    }
}
