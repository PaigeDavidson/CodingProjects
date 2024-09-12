/*
Very simple object to contain steps and id. The board does the heavy lifting.
*/
public class State implements Comparable<State>{
    private final String steps;
    private final String id;
    private final String[] ArrayList = {"1", "2", "3", "4", "5", "6", "7", "8", "0"};
    private Integer priority;
    State(String id, String steps) {
        this.steps = steps;
        this.id = id;
        //this is where you compute the priority
        priority = getPriority();
    }
    public int getPriority(){
        // compute this from the id
        //hamming distance
        //compute the number of tiles in the wrong position
        int priorityNum = 0;
        String[] idList = id.split("");
        for(int i = 0; i < id.length(); i++){
            if(!idList[i].equals("0")){
                if(!idList[i].equals(ArrayList[i])){
                    priorityNum += 1;

                }
            }
        }
        //How many moves were already required plus the number of tiles in the wrong position
        return priorityNum + getNumSteps();
    }
    /**
     * @return last move made
     */
    public char getLast(){
        if (steps.equals("")) return '*';
        int last = steps.length();
        return steps.charAt(last-1);
    }
    public String getId() {
        return id;
    }
    public String getSteps() {
        return steps;
    }
    public int getNumSteps() {
        return steps.length();
    }
    public String toString(){
        return "State " + id + " steps: " + steps + " " + priority;
    }
    //compares the ids - makes the class comparable
    public int compareTo(State aState){
        //this is where you find and compare the priority for the tree
        return (this.priority.compareTo( aState.priority));
    }
}