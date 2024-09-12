import java.util.Random;
public class Percolation {
    Integer SIZE;
    int[][] grid;
    Random random = new Random();
    int openCells;
    int TOP;
    int BOTTOM;

    UnionFind unionFind;
    //have all the colors as a string
    String BLUE = "\u001B[44m";
    String WHITE = "\u001B[47m"; // Use a different ANSI code for white text
    String BLACK = "\u001B[40m";
    String RED = "\u001B[41m";
    String RESET = "\u001b[0m";
    String[] sym = {BLACK + "   " + RESET, WHITE + "   " + RESET, BLUE + "   " + RESET, RED + "   " + RESET};


    public Percolation(int size) {
        this.TOP = size * size;
        this.BOTTOM = TOP + 1;
        this.openCells = 0;
        this.SIZE = size;
        initialize(size);
        this.unionFind = new UnionFind(SIZE * SIZE + 2);
    }

    public void print(int[][] grid) {
        for (int x = 0; x < SIZE; x++) {
            for (int y = 0; y < SIZE; y++) {
                int color = grid[x][y];
                int id = getId(x, y);
                if(unionFind.find(id) == unionFind.find(TOP)){
                    color = 2;
                }
                System.out.print(sym[color]);
            }
            System.out.println();
        }
    }

    public int getId(int x, int y){
        return SIZE * x + y;
    }

    //function that creates the array with empty values - all blocked
    public void initialize(int size){
        //make new grid with all spaces blocked
        this.grid = new int[size][size];
        for(int i = 0; i < size; i ++){
            for(int j = 0; j < size; j++){
                grid[i][j] = 0;
            }
        }

    }

    //open neighbor function that looks at if a cell has an open neighbor and unions if it is open
    public void unionNeighbor(int id, int x, int y){
        // if the cell is at the top of the grid
        if(x < 0){
            unionFind.union(TOP, id);
            return;
        }
        // if the cell is at the bottom of the grid
        if(x == SIZE){
            unionFind.union(BOTTOM, id);
            return;
        }
        //if the neighbor is off the left or right edges, we dont care about them
        if(y < 0 || y == SIZE){
            return;
        }
        // if the grid is open
        if(grid[x][y] == 1){
            int neighborId = getId(x, y);
            unionFind.union(id, neighborId);
        }
    }

    //function that runs through and does the percolation - opens a specified number of cells - updates graph
    public int percolate(boolean print){
        while(unionFind.find(TOP) != unionFind.find(BOTTOM)){
            //get the random cell
            int randomRow = random.nextInt(SIZE);
            int randomCol = random.nextInt(SIZE);

            int id = getId(randomRow, randomCol);

            //if the cell is not open, open it and change to white, otherwise, try again
            if(grid[randomRow][randomCol] == 0){
                if (print && openCells % 50 == 0 && openCells != 0) {
                    print(grid);
                    System.out.println("Open Cells: " + openCells);
                }

                grid[randomRow][randomCol] = 1;
                openCells += 1;
                // if the cell has a neighbor that is also open, union, change color to blue
                unionNeighbor(id, randomRow + 1, randomCol);
                unionNeighbor(id, randomRow - 1, randomCol);
                unionNeighbor(id, randomRow, randomCol + 1);
                unionNeighbor(id, randomRow, randomCol - 1);
            }

        }
        if(print){
            System.out.println("Percolated!");
            print(grid);
            System.out.println("Open Cells: " + openCells);
        }

        return openCells;
    }


    public static void main(String[] args) {
        int open = 0;
        Percolation percolation = new Percolation(20);
        open += percolation.percolate(true);

        open += percolation.percolate(false);
        open += percolation.percolate(false);
        open += percolation.percolate(false);
        open += percolation.percolate(false);
        open += percolation.percolate(false);

        System.out.println("Average: " + (int)((((double) open / 6) / (20 * 20) ) * 100) + "% of cells are open");

    }
}
