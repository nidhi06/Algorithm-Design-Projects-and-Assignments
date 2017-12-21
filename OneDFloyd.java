import java.util.Scanner;
import java.lang.Math;
public class OneDFloyd {
 //method to generate the random graph
 static int[][] graphmapping(int sizeOfNode, int[][] matelement) {
        for(int i=0;i<sizeOfNode;i++)
            for(int j=0;j<sizeOfNode;j++)
                if(i==j)
                 matelement[i][j]=0;
                else if(i>j) {
                    int element=(int)(Math.random()*10);
                    if(element>0)
                     matelement[i][j]=element;
                    else
                     matelement[i][j]=element+1;
                    matelement[j][i]=matelement[i][j];
                }
                /*else
                    //uncomment for sparse graph
                 matelement[i][j]=Integer.MAX_VALUE; */
             for(int i=0;i<sizeOfNode;i++)
                for(int j=0;j<sizeOfNode;j++)
                    if(i==j+1)
                     matelement[i][j]=matelement[j][i];
             
    // Please uncomment to display the graph
    /*for(int i=0;i<sizeOfNode;i++)
                 for(int j=0;j<sizeOfNode;j++)
                     System.out.print(matelement[i][j]+"\t");
                 System.out.println();*/     
         return matelement; 
    }

    public static void main(String[] args) {
        
        //Node values of 100,1000,2000,3000,4000,5000 and 6000 are selected to carry out the graph
        int size=6000;
        int d=size;
        int[][] m=new int[size][size];
        //calculating the time stamp
        long Time1=System.currentTimeMillis();
        //call randomm generator function to generate the graph
        m=graphmapping(size,m);
        
        //creating the output array
        int[] oneD=new int[size*size];
        int[] path=new int[size*size];
        
        //copy the lower triangular matrix to one dimensional array
        for(int i=1;i<size;i++)
            for(int j=0;j<i;j++) {
                int l=(i*(i-1)/2);
                oneD[l]=m[i][j];
            }
        System.out.println();
        
        long Time=System.currentTimeMillis();
        long time1=Time-Time1;
        
        for(int i=0;i<d;i++) {
            for(int j=0;j<d;j++){                 
                path[(i*(i-1)/2)+j]=j;
            }
        }
        //cFloy'ds algorithm using the One dimension
        for(int k=0;k<d;k++) {
            for(int i=0;i<d;i++) {
                for(int j=0;j<d;j++) {
                    if(oneD[i*(i-1)/2+j]> oneD[i*(i-1)/2+k]+oneD[k*(k-1)/2+j]) {
                        oneD[i*(i-1)/2+j]=oneD[i*(i-1)/2+k]+oneD[k*(k-1)/2+j];
                        path[i*(i-1)/2+j]=path[i*(i-1)/2+k];
                    }
                }
            }
        }
        long Time2=System.currentTimeMillis();
        long time=Time2-Time1;
        
        //Print statements for displaying the time elapsed
        System.out.println("Time to construct adjacency matrix :"+time1/1000.000+" seconds");
        System.out.println("Time to compute shortest path is: "+time/1000.000+" seconds");
        System.out.println("Total time taken: "+((time1+time)/1000.000)+" seconds");    
    }
}
