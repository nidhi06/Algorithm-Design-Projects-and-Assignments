import java.util.*;
public class BinaryTreeMirror {
    public static void main(String[] args) throws Exception {
final long startTime = System.nanoTime();
//Test Case#1
   //   String tree = "[3,9,20,null,null,15,7]";   
//Test Case#2             
//       String tree = "[5,14,15,null,3,6,9,1]";    
//Test Case#3             
        String tree = "[3,20,9,null,null,1,5,2,4,null,null,15]";  
        System.out.println("The Binary Tree: " + tree);
        BinaryTreeMirror obj = new BinaryTreeMirror();
        String result = obj.createMirror(tree);
        System.out.println("Generated mirror of the Binary Tree: " + result);
final long duration = System.nanoTime() - startTime; 
System.out.println("\n"+duration+" nano seconds");
    }

    public String createMirror(String stringtree) {
        Map<Integer, List<String>> Hashtree = new HashMap<>();
        int start_index = 0, height = 0, n, parent;
        boolean flag = true;
        stringtree = stringtree.replace("[", "");
        stringtree = stringtree.replace("]", "");
        String[] splittree = stringtree.split(",");
        while (flag) {
            n = (int) Math.pow(2.0, height);
            List<String> tree = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (start_index >= splittree.length) {
                    tree.add("null");
                    flag = false;
                } else {
                    if (height == 0)
                        tree.add(splittree[start_index]);
                    else {
                        parent = i / 2;
                        if (Hashtree.get((height - 1)).get(parent).equalsIgnoreCase("null")) {
                            tree.add("null");
                            start_index--;
                        } else
                            tree.add(splittree[start_index]);
                    }
                }
                start_index++;
            }
            if (start_index > splittree.length) {
                flag = false;
            }
            Hashtree.put(height, tree);
            height++;
        }

        for (int k = 0; k < Hashtree.size(); k++) {
            List<String> testree = Hashtree.get(k);
            int num = testree.size() / 2;
            int j = num - 1;
            String tmp;
            if (num != 0) {
                for (int i = num; i < testree.size(); i++) {
                    tmp = testree.get(i);
                    testree.set(i, testree.get(j));
                    testree.set(j, tmp);
                    j--;
                }
            }
        }

        for (int k = Hashtree.size()-1; k >= 1 ; k--){
        int size = (int)Math.pow(2.0,k);
        flag = true;
        for (int i = size-1; i >= 0; i = i-2) {
            parent = i / 2;
            if (Hashtree.get((k - 1)).get(parent).equalsIgnoreCase("null"))
            {
                Hashtree.get(k).remove(i);
                Hashtree.get(k).remove(i-1);	//pruning the tree
            }
            else if(Hashtree.get(k).get(i).equalsIgnoreCase("null")
                    && Hashtree.get(k).get(i-1).equalsIgnoreCase("null")
                    && flag){
                Hashtree.get(k).remove(i);
                Hashtree.get(k).remove(i-1);
            }
            else
                flag = false;
        }
        }
        
        List<List> mirrorTree = new ArrayList<>();
        for (int i = 0; i < Hashtree.size(); i++) {
            if (!Hashtree.get(i).isEmpty())
            mirrorTree.add(Hashtree.get(i));
//again converting the tree into string format for output generation
        }
        String result = mirrorTree.toString();
        result = result.replace("[", "");
        result = result.replace("]", "");
        result = "[" + result + "]";
        return result;

    }
}