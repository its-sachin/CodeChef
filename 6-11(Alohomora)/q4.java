import java.util.Scanner;
import java.util.HashMap;

class q4{

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        int N = scn.nextInt();

        for (int i=0; i<N;i++){
            int n = scn.nextInt();
            int[][] a = new int[n][3];
            int[][] s = new int[n][3];

            for (int j=0; j<n;j++){
                s[j][0] = scn.nextInt();
                s[j][1] = scn.nextInt(); 
                s[j][2] = 0;

                a[j][0] = s[j][0];
                a[j][1] = s[j][1]; 
                a[j][2] = scn.nextInt();
            }
            sortC(s,0,n-1);

            HashMap<Integer,int[]> h = new HashMap<>();

            for (int j=0; j<n; j++){
                h.put(j, s[j]);
            }

            for (int j=0; j<n; j++){
                int v = a[j][2];
                h.get(key)

            }
        }
    }

    static int part(int[][] M,int left,int right){

        int out = left-1;
        int[] pivot = M[right];
        
        int i = left;
        while(i < right){
            if (M[i][0] < pivot[0] || (M[i][0] == pivot[0] && M[i][1] > pivot[1])){
                out+= 1;

                int[] temp = M[out];
                M[out] = M[i];
                M[i] = temp;
            }
            i +=1;
        }
        
        out += 1;
        int[] temp = M[right];
        M[right] = M[out];
        M[out] = temp;

        return out;
    }

    static void sortC(int[][] M,int low,int high){

        if(low<high){
            
            int pivot = part(M,low,high);

            sortC(M,low,pivot-1);
            sortC(M,pivot+1,high);
        }
    }

}
