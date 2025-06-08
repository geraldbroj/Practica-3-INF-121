package Persistencia_5;

import java.io.*;
import java.util.*;

public class ArchFarmacia {
    private String nombreArchivo;

    public ArchFarmacia(String nombreArchivo) {
        this.nombreArchivo = nombreArchivo;
    }

    public void crearArchivo() throws IOException {
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nombreArchivo));
        oos.writeObject(new ArrayList<Farmacia>());
        oos.close();
    }

    public void adicionar(Farmacia f) throws IOException, ClassNotFoundException {
        ArrayList<Farmacia> lista = leer();
        lista.add(f);
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nombreArchivo));
        oos.writeObject(lista);
        oos.close();
    }

    public ArrayList<Farmacia> leer() throws IOException, ClassNotFoundException {
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nombreArchivo));
        ArrayList<Farmacia> lista = (ArrayList<Farmacia>) ois.readObject();
        ois.close();
        return lista;
    }

    public void listar() throws Exception {
        for (Farmacia f : leer()) {
            f.mostrar();
        }
    }

    public void mostrarMedicamentosResfrios() throws Exception {
        for (Farmacia f : leer()) {
            f.mostrarMedicamentos("resfrio");
        }
    }

    public double precioMedicamentoTos() throws Exception {
        double total = 0;
        for (Farmacia f : leer()) {
            for (Medicamento m : f.medicamentos) {
                if (m.getTipo().equalsIgnoreCase("tos")) {
                    total += m.getPrecio();
                }
            }
        }
        return total;
    }

    public void mostrarMedicamentosMenorTos() throws Exception {
        for (Farmacia f : leer()) {
            for (Medicamento m : f.medicamentos) {
                if (m.getTipo().equalsIgnoreCase("tos") && m.getPrecio() < 10) {
                    m.mostrar();
                }
            }
        }
    }

    public void mostrarMedicamentosSucursalTos(int sucursal) throws Exception {
        for (Farmacia f : leer()) {
            if (f.getSucursal() == sucursal) {
                f.mostrarMedicamentos("tos");
            }
        }
    }

    public void buscarSucursalConMedicamento(String nombreMedicamento) throws Exception {
        for (Farmacia f : leer()) {
            if (f.buscaMedicamento(nombreMedicamento)) {
                System.out.println("Sucursal: " + f.getSucursal() + " | Dirección: " + f.getDireccion());
            }
        }
    }
}
