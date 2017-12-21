public class ComparisonCountSort {
    public static void main(String [] args) throws Exception{

final long startTime = System.nanoTime();

//Test Case#1 -> 6 elements
  //     int [] array = { 62, 31, 84, 96, 19, 47};  
//Test Case#2  -> 40 elements                                               
    //    int [] array ={11,80,-15,93,-55,10,59,-35,84,-10,53,-73,16,-37,59,-45,-73,-3,84,                
      //          -29,-75,54,-38,-59,-78,-92,100,3,-88,83,59,32,-46,68,-68,-34,-73,50,-78,-19};
//Test Case#3 ->26 elements
  //     int [] array = {61,85,70,63,80,60,57,73,31,74,14,2,32,33,13,64,97,59,29,90,66,84,15,29,15,33}; 
 //Test Case#4 -> 20 elements
        int [] array = {-4,-1,-87,-42,-6,-74,-3,-26,-46,-16,-66,-93,-75,-97,-89,-54,-15,-39,-98,-29}; 
 
        int size = array.length;
        int [] count = new int[size];
        int [] result = new int[size];
        for (int i = 0; i < size; i++)
            result[i] = Integer.MIN_VALUE;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (i != j)
                    if (array[i] > array[j])
                        count[i]++;
            }
        }
        for (int i = 0; i < size; i++) {
            if (result[count[i]] != Integer.MIN_VALUE){
                int temp_counter = count[i];
                while (result[temp_counter] != Integer.MIN_VALUE)
                    temp_counter++;
                result[temp_counter] = array[i];
            }
            else
            result[count[i]] = array[i];
        }
        System.out.println(" Original Array:");
        for (int i = 0; i < size; i++)
            System.out.print(array[i]+" ");
        System.out.println("\n"+"Table of count: ");
        for (int i = 0; i < size; i++)
            System.out.print(count[i]+" ");
        System.out.println("\n"+" Sorted array: ");
        for (int i = 0; i < size; i++)
            System.out.print(result[i]+" ");
final long duration = System.nanoTime() - startTime; 
System.out.println("\n"+duration+" nano seconds");
}
}

