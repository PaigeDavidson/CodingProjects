public class PatternBlock extends Pattern{
    private boolean[][] pattern = {
            {true, true},
            {true, true}
    };

    public int getSizeX(){
        return 2;
    }
    public int getSizeY(){
        return 2;
    }

    @Override
    public boolean getCell(int x, int y) {
        return pattern[x][y];
    }
}
