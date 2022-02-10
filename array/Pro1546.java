import java.io.IOException;
import java.util.Scanner;

public class Pro1546 {
    public static void main(String[] args) throws IOException {
        Scanner scn = new Scanner(System.in);
        int count = scn.nextInt();
        double sum = 0;
        double[] num = new double[count];
        double max = Integer.MIN_VALUE;
        for(int i = 0; i < count; i++){
            int n = scn.nextInt();
            num[i] = n;
            if (max < n) max = n;
        }
        for(int i = 0; i < count; i++){
//            if(num[i] == max) sum += max;
//            else
            sum = sum + (num[i]/max * 100);
//            System.out.println(sum);
        }
        System.out.println(sum/count);
    }
}
