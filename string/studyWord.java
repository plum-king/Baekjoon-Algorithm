import java.util.Locale;
import java.util.Scanner;

public class studyWord {
    public static void main(String[] args){
        int alpha[] = new int[26];
        Scanner scn = new Scanner(System.in);
        String str = scn.next();
        str = str.toUpperCase(Locale.ROOT);
        int max = -1;
        char ch = '?';

        for(int i = 0; i < str.length(); i++)
            alpha[str.charAt(i) - 65] += 1;
        for(int i = 0; i < 26; i++) {
            if (max < alpha[i]) {
                max = alpha[i];
                ch = (char) (i + 65);
            }
            else if (alpha[i] == max)
                ch = '?';
        }
        System.out.print(ch);
    }
}