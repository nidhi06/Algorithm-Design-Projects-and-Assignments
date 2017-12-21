import java.util.Scanner;
public class FloydDimTwo {

 public static void main(String[] args) {
  Scanner stdin = new Scanner(System.in);
  
  //Node sizes are 100, 500, 1000, 3000, etc as mentioned in the requirement.
  
  int size=100;
  
  
  //int[][] a = new int[][]{{1000,1000,1000,29,1000,1000,1000,1000},{1000,1000,1000,1000,1000,11,11,1000},{1000,1000,1000,12,1000,5,5,1000},{29,1000,12,1000,5,1000,13,1000},{1000,1000,1000,5,1000,1000,7,11},{1000,11,5,1000,1000,1000,1000,17},{1000,11,5,13,7,1000,1000,1000},{1000,1000,1000,1000,11,17,1000,1000}};
  
  //int size=12;
  //int[][] a= new int[][]{{1000,11,14,1000,8,1000,29,28,1000,1000,14,1000},{11,1000,12,1000,6,1000,1000,1000,1000,1000,1000,1000},{14,12,1000,18,13,13,1000,1000,25,1000,1000,16},{1000,1000,18,1000,1000,1000,27,17,9,25,1000,1000},{8,6,13,1000,1000,1000,1000,1000,1000,1000,1000,22},{1000,1000,13,1000,1000,1000,1000,15,5,1000,1000,1000},{29,1000,1000,27,1000,1000,1000,1000,1000,1000,1000,1000},{28,1000,1000,17,1000,15,1000,1000,5,9,1000,1000},{1000,1000,25,9,1000,5,1000,5,1000,1000,25,1000},{1000,1000,1000,25,1000,1000,1000,9,1000,1000,1000,1000},{14,1000,1000,1000,1000,1000,1000,1000,25,1000,1000,1000},{1000,1000,16,1000,22,1000,1000,1000,1000,1000,1000,1000}}; 
  
  
  //Calculating elapsed time
  double startTime=System.currentTimeMillis(); 
  
  //Uncomment for random graph generation
  int[][] a = new int[size][size];
  a=Generate.generate(size,a);
  
  //Start time of the generation
  double Time1=System.currentTimeMillis();
  
  
  int[][] shortpath;
  int[][] path = new int[size][size];
  
  ///Marking the inputs such that the blanks in the inputs are considered.
  for (int i=0; i<size; i++){
   for (int j=0; j<size; j++){
    if (a[i][j] == 1000) 
     path[i][j] = -1;
    else
     path[i][j] = i; 
    if (a[i][j]!=-1)
     path[i][j] = i; 
   }
  }
  //Making diagonal elements as zero.
  for (int i=0; i<size; i++){
    path[i][i] = i;
  }
  //calling the class and the corresponding method to generate the shortest path.
  shortpath = ShortestPathFloyd.shortestpath(a, path);
  
  double endTime2=System.currentTimeMillis();
  
  
 
  //Printing the output
  //Uncomment the following code to print the output and to print the shortest path
  
  /*System.out.println("Shortest Path matrix:");
  for (int i=0; i<size;i++) {
              for (int j=0; j<size;j++){
               System.out.print(shortpath[i][j]+" "); 
               
              }
              System.out.println();
  }*/
  System.out.println("Time to create Adjacency Matrix: "+(Time1- startTime)/1000+"seconds");
  System.out.println("Time to generate input and compute shortest path: "+(endTime2-startTime)/1000+"seconds");
  System.out.println(("Time to compute shortest if input is provided: "+(endTime2-startTime)/1000+"seconds"));
  System.out.println("Enter start and end vertex:"); 
  //Consider the inputs to the function i.ie the nodes.
  int One = stdin.nextInt();
  int Two = stdin.nextInt();
  
  String myPath = Two + "";
  
  int sum=0;
  int flag=0;
  
  while (path[One][Two] != One) {
        flag=1;
        myPath = path[One][Two] + " -> " + myPath;
        sum+=shortpath[One][Two]; //OneD
        Two = path[One][Two];
  }
  
  if (flag==0)
        sum=shortpath[One][Two]; //OneD
  myPath = One + " -> " + myPath; 
  //Print the path of the inputed nodes.
  System.out.println("Shortest Path "+myPath);
  System.out.println("Distance: "+sum);  
  }
}


