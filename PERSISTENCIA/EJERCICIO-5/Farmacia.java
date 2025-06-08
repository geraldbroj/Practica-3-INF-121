package Persistencia_5;
import java.io.Serializable;
import java.util.ArrayList;

public class Farmacia implements Serializable {
    String nombreFarmacia;
    int sucursal;
    String direccion;
    ArrayList<Medicamento> medicamentos;

    public Farmacia(String nombre, int sucursal, String direccion, ArrayList<Medicamento> medicamentos) {
        this.nombreFarmacia = nombre;
        this.sucursal = sucursal;
        this.direccion = direccion;
        this.medicamentos = medicamentos;
    }

    public void mostrar() {
        System.out.println(nombreFarmacia + " - Sucursal: " + sucursal + " - Dirección: " + direccion);
        for (Medicamento m : medicamentos) {
            m.mostrar();
        }
    }

    public int getSucursal() {
        return sucursal;
    }

    public String getDireccion() {
        return direccion;
    }

    public void mostrarMedicamentos(String tipo) {
        for (Medicamento m : medicamentos) {
            if (m.getTipo().equalsIgnoreCase(tipo)) {
                m.mostrar();
            }
        }
    }

    public boolean buscaMedicamento(String nombre) {
        for (Medicamento m : medicamentos) {
            if (m.getNombre().equalsIgnoreCase(nombre)) {
                return true;
            }
        }
        return false;
    }
}