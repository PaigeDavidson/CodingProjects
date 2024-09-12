

public class MaxLeftHeap <T extends Comparable<T>> {
    private Node<T> root;

    public MaxLeftHeap() {
        root = null;
    }

    private static class Node<T> {

        Node( T theElement ) {
            this( theElement, null, null );
        }
        Node( T theElement, Node<T> lt, Node<T> rt ) {
            element = theElement; left = lt; right = rt; npl = 0;
        }
        T element; // The data in the node
        Node<T> left; // Left child
        Node<T> right; // Right child
        int npl; // null path length
    }
    public boolean isEmpty(){
        return root == null;
    }
    public void insert(T node){
        // create a new node
        Node<T> theNode = new Node<>(node);
        root = merge(root, theNode);
    }
    public T findMax(){
        if(isEmpty()){
            return null;
        }
        return root.element;
    }
    public T deleteMax(){
        if(isEmpty()){
            return null;
        }
        T max = root.element;
        root = merge(root.left, root.right);
        return max;
    }
    private Node<T> merge(Node<T> node1, Node<T> node2){
        //check that neither of the nodes are null
        if(node1 == null){
            return node2;
        }
        if(node2 == null){
            return node1;
        }
        //if node1 is smaller, switch so node 2 is on the left and becomes node1
        if(node1.element.compareTo(node2.element) < 0){
            Node<T> saveNode = node1;
            node1 = node2;
            node2 = saveNode;
        }
        //merge the now right child with the second node
        node1.right = merge(node1.right, node2);

        //if there is no left child, switch, so it stays a leftist tree with the right node
        if(node1.left == null){
            node1.left = node1.right;
            node1.right = null;
        //otherwise, if the left child is smaller than the right child, switch the children
        }else if(node1.left.element.compareTo(node1.right.element) < 0){
            Node<T> saveNode = node1.left;
            node1.left = node1.right;
            node1.right = saveNode;
        }
        return node1;

    }
    public static void main(String[] args) {
        //to test that my heap is working correctly
        MaxLeftHeap<Integer> heap = new MaxLeftHeap<>();
        heap.insert(5);
        heap.insert(9);
        heap.insert(3);
        heap.insert(10);
        heap.insert(1);
        heap.insert(22);


        System.out.println("Max element: " + heap.findMax());

        System.out.println("Deleting max element: " + heap.deleteMax());
        System.out.println("Max element after deletion: " + heap.findMax());
    }


}
