import java.io.IOException;
import java.util.Scanner;

public class Pro2577 {
    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        Scanner scn = new Scanner(System.in);
        int mul = 1;
        int num[] = new int[]{0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        for(int i = 0; i < 3; i++){
//            int n = Integer.parseInt(st.nextToken());
            int n = scn.nextInt();
            mul *= n;
        }
        while(mul != 0){
            int left = mul % 10;
            num[left]++;
            mul /= 10;
        }
        for(int i = 0; i < 10; i++){
            System.out.println(num[i]);
        }
    }
}
