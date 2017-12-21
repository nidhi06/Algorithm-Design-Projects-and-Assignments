import java.util.Scanner;
import java.util.Random;
public class ShortestPathFloyd {
 //method to compute shortest path
 public static int[][] shortestpath(int[][] adj, int[][] direction) {
  int n = adj.length;
  int[][] ans = new int[n][n]; 
  
  //shortest path computation and also the direction according to the algorithm
  for (int k=0; k<n;k++) {
   for (int i=0; i<n; i++) {
    for(int j=0;j<n;j++){
     if(ans[i][k]+ans[k][j]<ans[i][j]){
      ans[i][j]=ans[i][k]+ans[k][j];
      direction[i][j]=direction[k][j];
     }
    }
   } 
  }
  // Return the shortest path matrix.
  return ans;
  }
   
}

