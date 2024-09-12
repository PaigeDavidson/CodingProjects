public class Queue<T> {
    Node<T> head;
    Node<T> tail;

    public Queue(){
        head = null;
        tail = null;
    }

    public Queue(T initialValue){
        Node<T> firstNode = new Node<>(initialValue);
        head = firstNode;
        tail = firstNode;
    }

    public void add(T value) {
        Node<T> nodeToAdd = new Node<>(value);
        if(head == null){
            tail = nodeToAdd;
            head = nodeToAdd;
        }else{
        tail.next = nodeToAdd;
        tail = nodeToAdd;
        }
    }

    public T remove() {
        if(head == null){
            return null;
        }else{
            T data = head.data;
            head = head.next;
            return data;
        }
    }

    public void printContents() {
        System.out.println("The Queue is:");
        for(Node<T> node = head; node != null;  node = node.next){
            System.out.print(node.data + "   ");
        }
        System.out.println();
    }
}
