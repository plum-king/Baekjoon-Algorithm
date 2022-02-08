import java.io.IOException;
import java.util.Scanner;

public class Pro1037 {
    public static void main(String[] args) throws IOException {
        Scanner scn = new Scanner(System.in);
        int count = scn.nextInt();
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        for(int i = 0; i < count; i++){
            int n = scn.nextInt();
            if(n > max) max = n;
            if(n < min) min = n;
        }
        System.out.println(min * max);
    }
}
