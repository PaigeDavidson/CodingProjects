public class LifeSimulator {
    protected int width;
    protected int height;
    boolean[][] window;

    public LifeSimulator(int sizeX, int sizeY) {
        this.window = new boolean[sizeX][sizeY];
        for(int i = 0; i < sizeX; i++){
            for(int j = 0; j < sizeY; j++){
                window[i][j] = false;
            }
        }
        width = sizeX;
        height = sizeY;

    }

    public int getSizeX() {
        return width;
    }
    public int getSizeY() {
        return height;
    }
    public boolean getCell(int x, int y) {
        return window[x][y];
    }

    public void insertPattern(Pattern pattern, int startX, int startY) {
        for(int i = 0; i < pattern.getSizeX(); i++){
            for(int j = 0; j < pattern.getSizeY(); j++){
                window[i + startX][j + startY] = pattern.getCell(i, j);
            }
        }

    }

    // gets the number of surrounding cells that are alive
    public int aliveCount(int x, int y){
        int count = 0;
        for(int i = x - 1; i < x + 2; i ++){
            for(int j = y - 1; j < y + 2; j ++){
                if(i < 0 || i >= getSizeX() || j < 0 || j >= getSizeY() || (i == x && j == y)){
                    continue;
                }
                if(getCell(i, j)){
                    count += 1;
                }
            }
        }
        return count;
    }

    //    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
//    Any live cell with two or three live neighbours lives on to the next generation.
//    Any live cell with more than three live neighbours dies, as if by overpopulation.
//    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    public void update() {
        boolean dead = false;
        boolean live = true;
        boolean[][] updated = new boolean[getSizeX()][getSizeY()];
        for(int i = 0; i < getSizeX(); i++){
            for(int j = 0; j < getSizeY(); j++){
                if(window[i][j] == live){
                    if(aliveCount(i, j) < 2){
                        updated[i][j] = dead;

                    }
                    if(aliveCount(i, j) == 2 || aliveCount(i, j) == 3){
                        updated[i][j] = live;
                    }
                    if(aliveCount(i, j) > 3){
                        updated[i][j] = dead;
                    }
                }
                else{
                    if(aliveCount(i, j) == 3){
                        updated[i][j] = live;
                    }
                    else{
                        updated[i][j] = dead;
                    }
                }

            }
        }
        this.window = updated;


    }
}
