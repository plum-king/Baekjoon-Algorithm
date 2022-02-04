import java.util.Scanner;

public class findAlphabet {
    public static void main(String[] args){
        char word[] = new char[1000];
        int alpha[] = new int[26];
        Scanner scn = new Scanner(System.in);
        String str = scn.next();
        for(int i = 0; i < str.length(); i++)
            word[i] = str.charAt(i);
        for(int i = 0; i < 26; i++)
            alpha[i] = -1;
        for(int i = 0; i < str.length(); i++){
            if(alpha[(int)word[i] - 97] != -1){
                continue;
            }
            alpha[(int)word[i] - 97] = i;
        }
        for(int i = 0; i< 26; i++)
            System.out.print(alpha[i] + " ");
    }
}
