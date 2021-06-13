import java.util.*;


class q5{

    public static void main(String[] args) {
        

        Scanner scn = new Scanner(System.in);

        int N = scn.nextInt();

        for(int a=0;a<N;a++){

            int n = scn.nextInt();
            int k = scn.nextInt();

            String s = scn.next();

            char[] ch = new char[n];
  
            for (int i = 0; i < n; i++) {
                ch[i] = s.charAt(i);
            }

            int d = 0;

            for(int j=0; j<n; j++) {
                if (j!= 0 and j!= n-1){
                    if (s[j] == s[j-1]){
                        d+=2
                    }
                    else{
                        d+=1
                    }
                    if (s[j] == s[j+1]){
                        d+=2
                    }
                    else{
                        d+=1
                    }
                }
            }

            int i;
            for (int j=0; j<k; j++){
                i = scn.nextInt()-1;

                if (i==0){
                    if (s[i] == s[i+1]){
                        d-=1
                    }
                    else{
                        d+=1
                    }
                }
                else if(i==n-1){
                    if (s[i] == s[i-1]){
                        d-=1
                    }
                    else{
                        d+=1
                    }
                }
                else{
                    if (s[i] == s[i-1]){
                        if(s[i] == s[i+1]){
                            d-=2
                        }
                    }
                    else{
                        if (s[i] != s[i+1]){
                            d+=2
                        }
                    }
                }

                if (s[i]=='1'){
                    s[i]='0'
                }
                else{
                    s[i]='1'
                }
                System.out.println(d)
            }
        }
    }



}