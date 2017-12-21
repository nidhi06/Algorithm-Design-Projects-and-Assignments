import java.util.Scanner;
import java.util.Random;
public class Generate {
 //Method to generate random graph
 static int[][] generate(int nodeSize,int[][] array){ 
  for(int i=0;i<nodeSize;i++){
   for(int j=0;j<nodeSize;j++) 
    if(i==j)
     array[i][j]=0; 
    else if(i>j){
     int value=(int) (Math.random()*10); 
     if(value>0){
      array[i][j]=value;
     }
     else{
      array[i][j]=value+1;
     }
     array[j][i]=array[i][j];
    }
    /*else{
     a[i][j]=Integer.MAX_VALUE; //uncomment for sparse matrix generation
    }*/
  }
  //copying the upper diagonal to the lower for symmetry
  for(int i=0; i<nodeSize;i++){
   for(int j=0; j<nodeSize; j++){
    if(i==j+1){
     array[i][j]=array[j][i];
    }
   }
   
  }
 
   //Please uncomment to display the graph
                   for(int i=0;i<nodeSize;i++){
                         //System.out.println(i);
                         for (int j=0;j<nodeSize;j++){
                          System.out.print(array[i][j]+"\t");
                         }
                         System.out.println();
                   }

 return array;
 }
}
