public class GregorianDate extends Date {

    public GregorianDate() {
        super(1970, 1, 1,"gregorianDate");
        long millsSince = System.currentTimeMillis() + java.util.TimeZone.getDefault().getRawOffset();
        long seconds = millsSince / 1000;
        long minutes = seconds / 60;
        long hours = minutes / 60;
        long days = hours / 24;
        int intDays = (int) days;

        addDays(intDays);

    }

    public GregorianDate(int year, int month, int day) {
        super(year, month, day, "gregorianDate");
    }
}
