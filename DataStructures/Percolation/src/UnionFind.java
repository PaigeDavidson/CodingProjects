import java.util.Arrays;

public class UnionFind {
    private final int[] parentArray;
    private final int[] height;


    public UnionFind(int numElements){
        parentArray = new int[numElements];
        height = new int[numElements];

        for(int i = 0; i < numElements; i++){
            parentArray[i] = i;
            height[i] = 1;
        }

    }

    public int find(int x) {
        // this is making sure it is not the root
        if (parentArray[x] != x) {
            parentArray[x] = find(parentArray[x]); // Path compression
            return parentArray[x];
        }
        return parentArray[x];
    }

    public void union(int firstRoot, int secondRoot){
        //get root of both trees
        int root1 = find(firstRoot);
        int root2 = find(secondRoot);

        //return if the values are already in the same tree
        if(root1 == root2){
            return;
        }
        //if height of tree 2 is larger, the root of the second tree becomes the root
        if(height[root1] < height[root2]){
            parentArray[root1] = root2;
        }else if (height[root1] > height[root2]){
            parentArray[root2] = root1;
        }else{
            parentArray[root2] = root1;
            height[root1]++;
        }
    }


    public static void main(String[] args) {
        //this is where the tests go
        int numElements = 10;

        UnionFind UF = new UnionFind(numElements);
        System.out.println("parent Array");
        System.out.println(Arrays.toString(UF.parentArray));

        System.out.println("basic test");
        UF.union(0, 1);
        UF.union(2, 3);
        UF.union(4, 5);
        UF.union(6, 7);
        UF.union(1, 3);
        UF.union(5, 7);

        System.out.println(UF.find(0));

        //test path compression
        System.out.println("path compression");
        UF.find(6);
        for(int i = 0; i < numElements; i++){
            System.out.println(UF.find(i));
        }

        //test union
        System.out.println("union");
        UF.union(2, 4);
        System.out.println(UF.find(3));

        //make sure it's not cycling
        System.out.println("cycle detection");
        UF = new UnionFind(5);
        UF.union(0, 1);
        UF.union(1, 2);
        UF.union(2, 3);
        UF.union(3, 4);
        System.out.println(UF.find(0));


    }

}
