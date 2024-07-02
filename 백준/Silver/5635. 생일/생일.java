import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String arr[][] = new String[n][4];

        for(int i=0; i<n; i++){
            arr[i][0] = in.next();
            arr[i][1] = in.next();
            arr[i][2] = in.next();
            arr[i][3] = in.next();
        }

        Arrays.sort(arr, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                if(Integer.parseInt(o1[3]) == Integer.parseInt(o2[3])){
                    if(Integer.parseInt(o1[2]) == Integer.parseInt(o2[2])){
                        return Integer.compare(Integer.parseInt(o1[1]), Integer.parseInt(o2[1]));
                    } else
                        return Integer.compare(Integer.parseInt(o1[2]), Integer.parseInt(o2[2]));
                }
                return Integer.compare(Integer.parseInt(o1[3]), Integer.parseInt(o2[3]));
            }
        });

        System.out.println(arr[n-1][0] + "\n" + arr[0][0]);

        in.close();
    }
}
