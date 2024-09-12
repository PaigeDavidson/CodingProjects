import java.util.Scanner;
import java.util.*;
public class Game {
    private static final String SOLVED_ID = "123456780";
    Board theBoard;
    String originalBoardID;
    String boardName;
    /**
     * Solve the provided board
     * @param label Name of board (for printing)
     * @param b Board to be solved
     */
    public void playGiven(String label, Board b) {
        theBoard = b;
        originalBoardID = b.getId();
        boardName = label;
        System.out.println("Board initial: " + boardName + " \n" +
                theBoard.toString());
        State winningState = solve();
        if(winningState == null){
            System.out.println("No solution found, board is probably unsolvable");
            //if the winning state is null or you have tried 25 possibilities that means the board is unsolvable, probably
        }else {
            printSteps(theBoard, winningState.getSteps());
        }
    }
    public State solve(){
        int queueAdded = 0;
        int queueRemoved = 0;
        boolean done = false;
        Queue<State> queue = new Queue<>();
        State ogState = new State(originalBoardID, "");
        queue.add(ogState);

        //while loop
        while(!done){
            if(queueRemoved <= 3){
                queue.printContents();
            }
            State currentState = queue.remove();
            queueRemoved += 1;
            char[] moves = "UDLR".toCharArray();
            for(int i = 0; i < moves.length; i++){
                Board board = new Board(currentState.getId());
                if(board.makeMove(moves[i], currentState.getLast())){
                    int numSteps = currentState.getNumSteps();
                    if(numSteps > 26){
                        return null;
                        // if the board takes more than 26 steps to solve it is probably unsolvable
                    }
                    if(Objects.equals(currentState.getId(), SOLVED_ID)){
                        done = true;
                        System.out.println(boardName + " Queue added = " + queueAdded + " Removed = " + queueRemoved);
                        return currentState;

                    }

                    State newState = new State(board.getId(), currentState.getSteps() + moves[i]);
                    queue.add(newState);
                    queueAdded += 1;
                }
            }

        }
        return null;
    }
    /**
     * Create a random board (which is solvable) by jumbling jumnbleCount times.
     * Solve
     * @param label Name of board (for printing)
     * @param jumbleCount number of random moves to make in creating a board
     */
    public void playRandom(String label, int jumbleCount) {
        theBoard = new Board();
        theBoard.makeBoard(jumbleCount);
        System.out.println(label + "\n" + theBoard);
        playGiven(label, theBoard);
    }
    public static void main(String[] args) {
        String[] games = {"102453786", "123740658", "023156478", "413728065",
                "145236078", "123456870"};
        String[] gameNames = {"Easy Board", "Game1", "Game2", "Game3", "Game4",
                "Game5 No Solution"};
        Game g = new Game();
        Scanner in = new Scanner(System.in);
        Board b;
        String resp;
        for (int i = 0; i <= games.length - 1; i++) {
            b = new Board(games[i]);
            g.playGiven(gameNames[i], b);
            System.out.println("Click any key to continue\n");
            resp = in.nextLine();
        }
        boolean playAgain = true;
//playAgain = false;
        int JUMBLECT = 18; // how much jumbling to do in random board
        while (playAgain) {
            g.playRandom("Random Board", JUMBLECT);
            System.out.println("Play Again? Answer Y for yes\n");
            resp = in.nextLine().toUpperCase();
            playAgain = (resp != "") && (resp.charAt(0) == 'Y');
        }
    }
    public static void printSteps(Board OGboard, String steps){

        char[] letterList = steps.toCharArray();
        System.out.println("Solution");
        //print original board
        System.out.println(OGboard);
        //make changes and print moves
        for(int i = 0; i < letterList.length; i++){
            if(i == 0){
                OGboard.makeMove(letterList[i], '*');
            } else{
                OGboard.makeMove(letterList[i], letterList[i-1]);
            }
            System.out.println(letterList[i] + "==>");
            System.out.println(OGboard);
        }
        System.out.println("Moves Required: " + steps + "(" + letterList.length + ")");

    }
}
