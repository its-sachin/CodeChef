import java.util.*;
import java.util.HashMap;


class q5{

    public static void main(String[] args) {
        
        int N;

        Scanner scn = new Scanner(System.in);

        N = scn.nextInt();

        for (int x=0; x<N; x++) {

            int n = scn.nextInt();
            int m = scn.nextInt();
            int[] queue = new int[m];

            for (int a =0; a< m; a++){
                queue[a] = scn.nextInt();
            }

            int i =0;
            int j = m-1;
            int ans = 0;

            HashMap<Integer,Integer> pop = new HashMap<>();
            for (int a =0; a<n; a++){
                pop.put(a+1, a+1);
            }

            while(!pop.isEmpty()){
                System.out.println(ans + " " + i + " " + j);
                
                boolean done = false;

                if (queue[i] ==  queue[j] && pop.containsKey(queue[i])){
                    pop.remove(queue[j]);
                    i+=1;
                    ans+=1;
                    j-=1;
                    done=true;
                    continue;
                }

                if (pop.containsKey(queue[i]) && pop.containsKey(queue[j])){
                    int k = 1;
                    boolean found = false;
                    int temp = 0;

                    while(!found){
                        if(queue[i+k] != queue[i] && pop.containsKey(queue[i+k])){
                            found  = true;
                            temp=1;
                            pop.remove(queue[i+k]);
                            pop.remove(queue[i]);
                            k+=1;
                        }

                        else if(queue[j-k] != queue[j] && pop.containsKey(queue[j-k])){
                            found  = true;
                            temp=2;
                            pop.remove(queue[j-k]);
                            pop.remove(queue[j]);
                            k+=1;
                        }

                        else{
                            k+=1;
                        }
                    }

                    if (temp == 1){
                        i += k;
                        j-=1;
                        ans += k;
                    }

                    else{
                        j -= k;
                        i+=1;
                        ans += k;
                    }
                    continue;
                }

                if (pop.containsKey(queue[i])){
                    pop.remove(queue[i]);
                    i+=1;
                    ans+=1;
                    done = true;
                }

                if (pop.containsKey(queue[j])){
                    pop.remove(queue[j]);
                    j-=1;
                    ans+=1;
                    done = true;
                }

                if (!done){

                    int k = 1;
                    boolean found = false;
                    int temp = 0;

                    while(!found){
                        if(pop.containsKey(queue[i+k])){
                            found  = true;
                            temp=1;
                            pop.remove(queue[i+k]);
                            k+=1;
                        }

                        else if(pop.containsKey(queue[j-k])){
                            found  = true;
                            temp=2;
                            pop.remove(queue[j-k]);
                            k+=1;
                        }

                        else{
                            k+=1;
                        }
                    }

                    if (temp == 1){
                        i += k;
                        ans += k;
                    }

                    else{
                        j -= k;
                        ans += k;
                    }
                }
            }


            System.out.println(ans);

        }

    }



}