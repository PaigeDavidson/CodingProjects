public class JulianDate extends Date{

    public JulianDate(){
        super(1, 1, 1, "julianDate");
        addDays(719164);
        long millsSince = System.currentTimeMillis() + java.util.TimeZone.getDefault().getRawOffset();
        long seconds = millsSince / 1000;
        long minutes = seconds / 60;
        long hours = minutes / 60;
        long days = hours / 24;
        int intDays = (int) days;

        addDays(intDays);
    }
    public JulianDate(int year, int month, int day){

        super(year, month, day, "julianDate");
    }

}

