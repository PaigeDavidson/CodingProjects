

public class BinarySearchTree <E extends  Comparable<E>>{
    TreeNode<E> root;
    private class TreeNode<E>{
        public E value;
        public TreeNode<E> left;
        public TreeNode<E> right;
        public TreeNode(E value) {
            this.value = value;
        }
    }
    public boolean insert(E value){
        if(search(value)) {
            return false;
        }
        if(root == null){
            root = new TreeNode<>(value);
            return true;
        }
        return insert(null, root, value);
    }
    private boolean insert(TreeNode<E> parent, TreeNode<E> node, E value){
        // if the value is already in the tree return false
        //otherwise, find where the node = null (the end of the branch), set the parent = to the parent of the null
        // branch, and set the value = to the child of that parent
            if(node == null){
                if (parent.value.compareTo(value) > 0) {
                    parent.left = new TreeNode<>(value);
                } else {
                    parent.right = new TreeNode<>(value);
                }
                return true;
            }
            else if (node.value.compareTo(value) > 0) {
                return insert(node, node.left, value);
            }else{
                return insert(node, node.right, value);
            }
    }
    //If the value was in the tree and deleted, return true, otherwise, return false.
    public boolean remove(E value){
        TreeNode<E>parent = null;
//        TreeNode<E>node = new TreeNode<>(value);
        TreeNode<E>node = root;

        boolean done = false;
        while (!done) {
            if (node == null){
                return false;
            }
            if (node.value.compareTo(value) == 0) {
                done = true;
            }
            else if (node.value.compareTo(value) > 0) {
                parent = node;
                node = node.left;
            } else {
                parent = node;
                node = node.right;
            }
        }
        // Check for left child
        if(node.left != null) {
            TreeNode<E>parentOfRight = node;
            TreeNode<E>rightMost = node.left;

            while (rightMost.right != null) {
                parentOfRight = rightMost;
                rightMost = rightMost.right;
            }
            // rightMost has the largest value in the left subtree
            node.value = rightMost.value;

            if (parentOfRight.right == rightMost) {
                parentOfRight.right = rightMost.left;
            } else {
                parentOfRight.left = rightMost.left;
            }
            return true;
        } else {
            // Remove based on no-left child
            if (parent == null) {
                root = root.right;
            } else {
                if (parent.value.compareTo(value) < 0) {
                    parent.right = node.right;
                } else {
                    parent.left = node.right;
                }
            }
            return true;
        }
    }
    public boolean search(E value){
        return search(root, value);
    }
    private boolean search(TreeNode<E> node, E value){
        if(node == null){
            return false;
        }
        if(node.value.compareTo(value) == 0){
            return true;
        }

        else if (node.value.compareTo(value) > 0) {
            return search(node.left, value);
        }else{
            return search(node.right, value);
        }
    }
    public void display(String message){
        System.out.println(message);
        traverseInOrder(root);
    }
    private void traverseInOrder(TreeNode<E> node){
        if (node != null) {
            traverseInOrder(node.left);
            System.out.println(node.value);
            traverseInOrder(node.right);
        }
    }
    // nodes have children and parents
    public int numberNodes(){
        return numberNodes(root);
    }
    private int numberNodes(TreeNode<E> node){
        if(node == null){
            return 0;
        }else{
            return 1 + numberNodes(node.left) + numberNodes(node.right);
        }
    }
    // leaf nodes have no children
    public int numberLeafNodes(){
        return numberLeafNodes(root);
    }
    private int numberLeafNodes(TreeNode<E> node){
        if(node != null){
            // test if it's a leaf node
            if(node.right == null && node.left == null){
                return 1;
            }
            return numberLeafNodes(node.left) + numberLeafNodes(node.right);
        }else{
            return 0;
        }
    }
    //height is the Path length from the root to the furthest leaf
    public int height(){
        return height(root);
    }
    private int height(TreeNode<E> node){
        if(node != null) {
            int leftHeight = height(node.left);
            int rightHeight = height(node.right);
            if(leftHeight > rightHeight){
                return 1 + leftHeight;
            }else{
                return 1 + rightHeight;
            }
        }
        else{
            return -1;
        }

    }
}
