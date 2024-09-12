public class Node<T> {
    public T data;

    public Node<T> next;

    public Node(T initialData){
        data = initialData;
        next = null;
    }
}
