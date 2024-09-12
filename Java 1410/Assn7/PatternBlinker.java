public class PatternBlinker extends Pattern{
    private boolean[][] pattern = {
            {true, true, true}
    };

    public int getSizeX(){
        return 1;
    }
    public int getSizeY(){
        return 3;
    }

    @Override
    public boolean getCell(int x, int y) {
        return pattern[x][y];
    }
}
