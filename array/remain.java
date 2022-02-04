import java.util.Scanner;

public class remain {
    public static void main(String[] args){
        int count = 0, num;
        int nextNum[] = new int[42];
        Scanner scn = new Scanner(System.in);

        for(int i = 0; i < 10; i++){
            num = scn.nextInt() % 42;
            nextNum[num]++;
            count++;
            if(nextNum[num] > 1) count--;
        }
        System.out.println(count);
    }
}
