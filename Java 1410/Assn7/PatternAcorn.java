public class PatternAcorn extends Pattern{

    private boolean[][] pattern = {
            {false, true, false, false, false, false, false},
            {false, false, false, true, false, false, false},
            {true, true, false, false, true, true, true}
    };

    public int getSizeX(){
        return 3;
    }
    public int getSizeY(){
        return 7;
    }

    @Override
    public boolean getCell(int x, int y) {
        return pattern[x][y];
    }
}
