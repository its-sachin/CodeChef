import java.util.Scanner;

public class q3 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        node[] p = new node[n];
        for (int i=0; i<3*n;i++){
            System.out.println(i);
            p[i].val = s.nextInt();
            p[i].index = i;
        }
    }

    static int func(node[] p, int n){

        int d=0;
        sortC(p,0,n-1);
        node maxIn = p[0];

        for (int i=0; i<n; i++){
            if (p[i].index>maxIn.index){
                maxIn = p[i];
            }
            d+=p[i].val;
        }

        node minIn = p[2*n];
        for (int i=2*n; i<3*n; i++){
            if (p[i].index<minIn.index){
                minIn = p[i];
            }
            d-=p[i].val;
        }

        if (maxIn.index<minIn.index){
            return d;
        }
        else{

            while(maxIn.index>=minIn.index) {

                if (d-maxIn.val+minIn.val <= d){

                    int i = 2*n-1;

                    while(true){
                        if (p[i].index>minIn.index){
                            d+=minIn.val;
                            minIn = p[i];
                            d-=minIn.val;
                            break;
                        }
                        i-=1;
                    }
                }

                else{

                    while(true){

                        int i = n;

                        if (p[i].index<maxIn.index){
                            d-=maxIn.val;
                            maxIn = p[i];
                            d+=maxIn.val;
                            break;
                        }
                        i+=1;
                    }

                }

            }
            return d;

        }
        
    }

    
    static int part(node[] M, int left, int right) {

        int out = left-1;
        int pivot = M[right].val;
        
        for(int i=left; i< right; i++) {
            if (M[i].val < pivot ) {
                out+= 1;

                int temp = M[out].val;
                M[out].val = M[i].val;
                M[i].val = temp;
            }
        
        }
        out += 1;
        int temp = M[right].val;
        M[right].val = M[out].val;
        M[out].val = temp;

        return out;
    }

    static void sortC(node[] M, int low, int high)
    {

        if(low<high) {
            
            int pivot = part(M,low,high);

            sortC(M,low,pivot-1);
            sortC(M,pivot+1,high);
            
        }
    }

}

class node{

    public int val;
    public int index;
}
