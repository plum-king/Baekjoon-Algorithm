import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Pro17427 {
    // 시간 초과 + sum을 int로 해서 발생한 오류
//    public static void main(String[] args) {
//        Scanner scn = new Scanner(System.in);
//        int n = scn.nextInt();
//        int sum = 0;
//        for (int i = 1; i <= n; i++) {
//            for (int j = 1; j <= i; j++) {
//                if (i % j == 0) sum += j;
//            }
//        }
//        System.out.println(sum);
//    }
    // 해결 방법
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long sum = 0;
        for (int i = 1; i <= n; i++) {
           sum += (n/i)*i;
        }
        System.out.print(sum);
    }
}
