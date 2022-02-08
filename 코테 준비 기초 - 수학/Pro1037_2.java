import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Pro1037_2 {
    public static void main(String[] args) throws IOException {
//        Scanner scn = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(br.readLine());
//        int count = scn.nextInt();
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        for(int i = 0; i < count; i++){
            int n = Integer.parseInt(st.nextToken());
            if(n > max) max = n;
            if(n < min) min = n;
        }
        System.out.println(min * max);
    }
}
