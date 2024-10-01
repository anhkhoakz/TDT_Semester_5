
// Ex04/SensorImpl.java
import java.rmi.RemoteException;
import java.util.Random;

public class SensorImpl implements Sensor {
    private String latestReading;

    public SensorImpl() throws RemoteException {
        updateSensorData();
    }

    public void updateSensorData() {
        Random rand = new Random();
        int temperature = rand.nextInt(100);
        latestReading = "Temperature: " + temperature + "°C";
    }

    public String getLatestReading() throws RemoteException {
        updateSensorData();
        return latestReading;
    }
}