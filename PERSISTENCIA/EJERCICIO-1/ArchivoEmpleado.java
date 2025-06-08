package Persistencia_1;
import java.io.*;
import java.util.ArrayList;

public class ArchivoEmpleado {
    private String nomA;

    public ArchivoEmpleado(String nomA) {
        this.nomA = nomA;
    }

    public void crearArchivo() throws IOException {
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(nomA));
        out.writeObject(new ArrayList<Empleado>());
        out.close();
    }

    public void guardarEmpleado(Empleado e) throws IOException, ClassNotFoundException {
        ArrayList<Empleado> empleados = leerEmpleados();
        empleados.add(e);
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(nomA));
        out.writeObject(empleados);
        out.close();
    }

    public Empleado buscaEmpleado(String nombre) throws IOException, ClassNotFoundException {
        ArrayList<Empleado> empleados = leerEmpleados();
        for (Empleado e : empleados) {
            if (e.getNombre().equals(nombre)) {
                return e;
            }
        }
        return null;
    }

    public Empleado mayorSalario(float salario) throws IOException, ClassNotFoundException {
        ArrayList<Empleado> empleados = leerEmpleados();
        for (Empleado e : empleados) {
            if (e.getSalario() > salario) {
                return e;
            }
        }
        return null;
    }

    private ArrayList<Empleado> leerEmpleados() throws IOException, ClassNotFoundException {
        FileInputStream fileIn = new FileInputStream(nomA);
        ObjectInputStream in = new ObjectInputStream(fileIn);
        ArrayList<Empleado> empleados = (ArrayList<Empleado>) in.readObject();
        in.close();
        return empleados;
    }
}

