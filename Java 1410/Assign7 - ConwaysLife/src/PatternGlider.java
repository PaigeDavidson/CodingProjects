public class PatternGlider extends Pattern{
    private boolean[][] pattern = {
            {false, true, false},
            {false, false, true},
            {true, true, true}
    };

    public int getSizeX(){
        return 3;
    }
    public int getSizeY(){
        return 3;
    }

    @Override
    public boolean getCell(int x, int y) {
        return pattern[x][y];
    }
}
