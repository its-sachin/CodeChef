import java.util.Scanner;

class q1{

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int m = s.nextInt();
        int n = s.nextInt();
        int k = s.nextInt();

        int[] row = new int[m];
        int[] col = new int[n];
        int[] same = new int[Math.min(m,n)];
        
        for (int i=0; i<k; i++) {
            int x = s.nextInt();
            int y = s.nextInt();

            row[x-1]+=1;
            col[y-1]+=1;

            if (x==y){
                same[x-1]=1;
            }

        }

        int mr=-1;
        int mc=-1;

        for (int i=0; i<m; i++) {
            if (mr==-1 || row[mr]<row[i]){
                mr=i;
            }
            else if (row[mr]==row[i] && (same[mr] == 1)){
                mr=i;
            }
        }

        for (int i=0; i<n; i++) {
            if (mc==-1 || col[mc]<col[i]){
                mc=i;
            }
            else if (col[mc]==col[i] && (same[mc] == 1)){
                mc=i;
            }
        }

        if (same[mr] ==1){
            row[mr]-=1;
        }

        System.out.println(row[mr]+col[mc]);
    }


}