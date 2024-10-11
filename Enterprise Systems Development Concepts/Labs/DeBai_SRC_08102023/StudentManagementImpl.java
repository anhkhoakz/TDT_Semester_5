// DO NOT USE PACKAGE

import java.io.*;
import java.rmi.RemoteException;
import java.util.ArrayList;

public class StudentManagementImpl implements StudentManagement {

    ArrayList<Student> students;

    public StudentManagementImpl() {
        this.students = new ArrayList<>();
    }

    public StudentManagementImpl(String dataPath) {
        this.students = new ArrayList<>();
        readData(dataPath);
    }

    private void readData(String filePath) {
        try {
            File file = new File(filePath);
            BufferedReader br = new BufferedReader(new FileReader(file));

            String readLine = "";
            while ((readLine = br.readLine()) != null) {
                String[] data = readLine.split("\t");

                if (data.length != 5) {
                    continue;
                }

                Student student = new Student(data[0], data[1], data[2], Double.parseDouble(data[3]),
                        data[4]);
                students.add(student);
            }

            br.close();
        } catch (IOException ex) {
            System.err.println(ex.getMessage());
        }
    }

    @Override
    public int getNoOfStudent() throws RemoteException {
        if (isStudentsEmpty()) {
            return -1;
        }
        return students.size();
    }

    @Override
    public int getNoOfStudent_byGender(String gender) throws RemoteException {
        if (isStudentsEmpty()) {
            return -1;
        }
        int count = 0;
        for (Student student : students) {
            if (student.getGender().equalsIgnoreCase(gender)) {
                count++;
            }
        }
        return count;
    }

    @Override
    public int getNoOfStudent_byMajor(String major) throws RemoteException {
        if (isStudentsEmpty()) {
            return -1;
        }
        int count = 0;
        for (Student student : students) {
            if (student.getMajor().equalsIgnoreCase(major)) {
                count++;
            }
        }
        return count;
    }

    @Override
    public int getNoOfStudent_byGPA(double gpa) throws RemoteException {
        if (isStudentsEmpty()) {
            return -1;
        }
        int count = 0;
        for (Student student : students) {
            if (student.getGpa() < gpa) {
                count++;
            }
        }
        return count;
    }

    @Override
    public Student findStudent_byName(String name) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }
        for (Student student : students) {
            if (student.getName().equalsIgnoreCase(name)) {
                return student;
            }
        }
        return null;
    }

    @Override
    public Student findStudent_byID(String id) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }
        for (Student student : students) {
            if (student.getId().equalsIgnoreCase(id)) {
                return student;
            }
        }
        return null;
    }

    @Override
    public ArrayList<Student> findStudent_byMajor(String major) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }
        ArrayList<Student> result = new ArrayList<>();
        for (Student student : students) {
            if (student.getMajor().equalsIgnoreCase(major)) {
                result.add(student);
            }
        }
        return result;
    }

    @Override
    public ArrayList<Student> findStudent_byGPA(double GPA) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        ArrayList<Student> result = new ArrayList<>();
        for (Student student : students) {
            if (student.getGpa() < GPA) {
                result.add(student);
            }
        }
        return result;
    }

    @Override
    public double getAvgGPA() throws RemoteException {
        if (isStudentsEmpty()) {
            return -1;
        }

        double sum = 0;
        for (Student student : students) {
            sum += student.getGpa();
        }
        return sum / students.size();

    }

    @Override
    public Student getHighestGPA_byGender(String gender) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        double maxGPA = Double.MIN_VALUE;
        Student result = null;

        for (Student student : students) {
            if (student.getGender().equalsIgnoreCase(gender) && student.getGpa() > maxGPA) {
                maxGPA = student.getGpa();
                result = student;
            }
        }
        return result;
    }

    @Override
    public Student getHighestGPA_byFName(String fname) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        double maxGPA = Double.MIN_VALUE;
        Student result = null;

        for (Student student : students) {
            String firstName = student.getName().split(" ")[0];
            if (firstName.equalsIgnoreCase(fname) && student.getGpa() > maxGPA) {
                maxGPA = student.getGpa();
                result = student;
            }
        }
        return result;
    }

    @Override
    public Student getHighestGPA_byLName(String lname) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        double maxGPA = Double.MIN_VALUE;
        Student result = null;

        for (Student student : students) {
            String[] nameParts = student.getName().split(" ");
            String lastName = nameParts[nameParts.length - 1];

            if (lastName.equalsIgnoreCase(lname) && student.getGpa() > maxGPA) {
                maxGPA = student.getGpa();
                result = student;
            }
        }
        return result;
    }

    @Override
    public Student getHighestGPA_byMajor(String major) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        double maxGPA = Double.MIN_VALUE;
        Student result = null;

        for (Student student : students) {
            if (student.getMajor().equalsIgnoreCase(major) && student.getGpa() > maxGPA) {
                maxGPA = student.getGpa();
                result = student;
            }
        }
        return result;
    }

    @Override
    public Student getLowestGPA_byMajor(String major) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        double minGPA = Double.MAX_VALUE;
        Student result = null;

        for (Student student : students) {
            if (student.getMajor().equalsIgnoreCase(major) && student.getGpa() < minGPA) {
                minGPA = student.getGpa();
                result = student;
            }
        }
        return result;
    }

    @Override
    public ArrayList<Student> getTop10_byGPA() throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        ArrayList<Student> result = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            double maxGPA = Double.MIN_VALUE;
            Student student = null;
            for (Student s : students) {
                if (s.getGpa() > maxGPA && !result.contains(s)) {
                    maxGPA = s.getGpa();
                    student = s;
                }
            }
            result.add(student);
        }

        return result;
    }

    @Override
    public ArrayList<Student> getTop10GPA_byGender(String gender) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        ArrayList<Student> result = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            double maxGPA = Double.MIN_VALUE;
            Student student = null;
            for (Student s : students) {
                if (s.getGpa() > maxGPA && !result.contains(s) && s.getGender().equalsIgnoreCase(gender)) {
                    maxGPA = s.getGpa();
                    student = s;
                }
            }
            result.add(student);
        }

        return result;
    }

    @Override
    public ArrayList<Student> getTop10GPA_byMajor(String major) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        ArrayList<Student> result = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            double maxGPA = Double.MIN_VALUE;
            Student student = null;
            for (Student s : students) {
                if (s.getGpa() > maxGPA && !result.contains(s) && s.getMajor().equalsIgnoreCase(major)) {
                    maxGPA = s.getGpa();
                    student = s;
                }
            }
            result.add(student);
        }

        return result;
    }

    @Override
    public ArrayList<Student> getLast10GPA_byGender(String gender) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        ArrayList<Student> result = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            double minGPA = Double.MAX_VALUE;
            Student student = null;
            for (Student s : students) {
                if (s.getGpa() < minGPA && !result.contains(s) && s.getGender().equalsIgnoreCase(gender)) {
                    minGPA = s.getGpa();
                    student = s;
                }
            }
            result.add(student);
        }

        return result;
    }

    @Override
    public ArrayList<Student> getLast10GPA_byMajor(String major) throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        ArrayList<Student> result = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            double minGPA = Double.MAX_VALUE;
            Student student = null;
            for (Student s : students) {
                if (s.getGpa() < minGPA && !result.contains(s) && s.getMajor().equalsIgnoreCase(major)) {
                    minGPA = s.getGpa();
                    student = s;
                }
            }
            result.add(student);
        }

        return result;
    }

    @Override
    public ArrayList<String> getMajors() throws RemoteException {
        if (isStudentsEmpty()) {
            return null;
        }

        ArrayList<String> result = new ArrayList<>();
        for (Student student : students) {
            if (!result.contains(student.getMajor())) {
                result.add(student.getMajor());
            }
        }
        return result;
    }

    public boolean isStudentsEmpty() {
        return students == null || students.isEmpty() || students.size() == 0;
    }

}
