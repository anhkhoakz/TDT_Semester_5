import java.rmi.RemoteException;

public class CalculatorImpl implements Calculator {
    public double calculate(double a, double b, String operator) throws RemoteException {
        switch (operator) {
            case "+":
                return addition(a, b);
            case "-":
                return subtract(a, b);
            case "x":
                return multiply(a, b);
            case "/":
                return divide(a, b);
            default:
                throw new IllegalArgumentException("Invalid operator");
        }
    }

    public double addition(double a, double b) throws RemoteException {
        return a + b;
    }

    public double subtract(double a, double b) throws RemoteException {
        return a - b;
    }

    public double multiply(double a, double b) throws RemoteException {
        return a * b;
    }

    public double divide(double a, double b) throws RemoteException {
        if (b == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        return a / b;
    }

}
