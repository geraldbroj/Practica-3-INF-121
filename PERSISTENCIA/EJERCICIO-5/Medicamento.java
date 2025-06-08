package Persistencia_5;

import java.io.Serializable;

public class Medicamento implements Serializable {
    String nombre;
    int codMedicamento;
    String tipo;
    double precio;

    public Medicamento(String nombre, int cod, String tipo, double precio) {
        this.nombre = nombre;
        this.codMedicamento = cod;
        this.tipo = tipo;
        this.precio = precio;
    }

    public void mostrar() {
        System.out.println(nombre + " | Tipo: " + tipo + " | Precio: " + precio);
    }

    public String getTipo() {
        return tipo;
    }

    public double getPrecio() {
        return precio;
    }

    public String getNombre() {
        return nombre;
    }
}