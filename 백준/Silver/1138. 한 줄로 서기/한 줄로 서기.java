import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        List<Integer> n_list = new ArrayList<>();
        for(int i=0; i<n; i++){
            n_list.add(in.nextInt());
        }
        
        List<Integer> cm = new ArrayList<>();
        for(int i=1; i<=n+1; i++){
            cm.add(i);
        }
        
        List<Integer> result = new ArrayList<>();
        
        int j = n_list.size() - 1;
        for(int i=0; i<n; i++){
            result.add(n_list.get(j), cm.get(j));
            j--;
        }
        
        for(int i:result){
            System.out.print(i+" ");
        }
    }
}