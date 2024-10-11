// DO NOT USE PACKAGE

import java.io.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {

    public static void main(String[] args) {
        try {
            // Parse the input arguments
            if (args.length < 3) {
                System.err.println("usage  : java Client <host> <port> run");
                System.err.println("example: java Client localhost 1100 run");
                System.exit(1);
            }
            int index = 0;
            String host = args[index++];
            int port = Integer.parseInt(args[index++]);

            // Getting the registry
            Registry registry = LocateRegistry.getRegistry(host, port);

            // Looking up the registry for the remote object
            StudentManagement stub = (StudentManagement) registry.lookup("StuManagement");

            // Write to output
            try (BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"))) {
                bw.write(stub.getNoOfStudent() + "\n");
                bw.write(stub.getNoOfStudent_byGender("male") + "\n");
                bw.write(stub.getNoOfStudent_byMajor("Information System") + "\n");
                bw.write(stub.getNoOfStudent_byGPA(4) + "\n");

                bw.write(stub.findStudent_byName("Lindsy Pugsley").toString() + "\n");
                bw.write(stub.findStudent_byID("51009070").toString() + "\n");
                bw.write(stub.findStudent_byMajor("Computational Intelligent").size() +
                        "\n");

                bw.write(stub.findStudent_byGPA(4).size() + "\n");
                bw.write(stub.getHighestGPA_byGender("male").toString() + "\n");
                bw.write(stub.getHighestGPA_byFName("Ardella").toString() + "\n");

                bw.write(stub.getHighestGPA_byLName("Scales").toString() + "\n");
                bw.write(stub.getHighestGPA_byMajor("Information System").toString() + "\n");
                bw.write(stub.getLowestGPA_byMajor("Information System").toString() + "\n");

                bw.write(String.format("%.2f", stub.getAvgGPA()) + "\n");

                // Print getTop10_byGPA()
                for (Student s : stub.getTop10_byGPA()) {
                    bw.write(s.toString() + "\n");
                }

                // Print getTop10GPA_byGender("male")
                for (Student s : stub.getTop10GPA_byGender("male")) {
                    bw.write(s.toString() + "\n");
                }

                // Print getTop10GPA_byMajor("Information System")
                for (Student s : stub.getTop10GPA_byMajor("Information System")) {
                    bw.write(s.toString() + "\n");
                }

                // Print getLast10GPA_byGender("female")
                for (Student s : stub.getLast10GPA_byGender("female")) {
                    bw.write(s.toString() + "\n");
                }

                // Print getLast10GPA_byMajor("Computational Intelligent")
                for (Student s : stub.getLast10GPA_byMajor("Computational Intelligent")) {
                    bw.write(s.toString() + "\n");
                }

                bw.close();

                System.out.println("Done!");

            } catch (IOException e) {
                System.err.println(e.getMessage());
            }

        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }

}
