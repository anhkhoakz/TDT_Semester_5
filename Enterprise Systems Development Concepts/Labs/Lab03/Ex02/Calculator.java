import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Calculator extends Remote {

    public double calculate(double a, double b, String operator) throws RemoteException;

    public double addition(double a, double b) throws RemoteException;

    public double subtract(double a, double b) throws RemoteException;

    public double multiply(double a, double b) throws RemoteException;

    public double divide(double a, double b) throws RemoteException;

}
