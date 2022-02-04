import java.util.Scanner;

public class overAverage {
    public static void main(String[] args){
        int intArr[] = new int[1000];
        Scanner scn = new Scanner(System.in);
        int num = scn.nextInt();

        for(int i = 0; i <num; i++) {
            int student = scn.nextInt();
            double sum = 0;

            for (int j = 0; j < student; j++) {
                intArr[j] = scn.nextInt();
                sum += intArr[j];
            }
            double avg = sum / student;
            double count = 0;

            for (int j = 0; j < student; j++) {
                if (intArr[j] > avg) count++;
            }
            System.out.printf("%.3f%%\n", (count/student) * 100);
        }
        scn.close();
    }
}
