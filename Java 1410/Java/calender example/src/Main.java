public class Main{
    public static void main(String[] args) {

        printCalender(2022, 9);
    }

    public static void printCalender(int year, int month) {
        //printmonthTitle(year, month);
        //printMonthBody();

    }

    public static boolean isLeapYear(int year) {
        return year % 400 == 0 || ((year & 4) == 0 && year % 100 != 0);

    }

    public static int getNumberOfDaysInMonth(int year, int month) {
        switch (month){
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                return 31;
            case 4:
            case 6:
            case 9:
            case 11:
                return 30;
            case 2:
                if (isLeapYear(year)){
                    return 29;

                }else {
                    return 28;
                }
            default:
                return 0;
        }
    }

    public static int getTotalNumberOfDays(int year, int month) {
        return 0;
    }
    public static int getStartDay(int year, int month){
        return 0;
    }
    public static void printMonthBody(int year, int month){

    }
    public static String getMonthName(int month){
        switch (month){
            case 1:
                return "january";
            case 2:
                return "february:";
            case 3:
                return "march";
            case 4:
                return "April";
            case 5:
            case 6:
            case 7:
            case 8:
            case 9:
            case 10:
            case 11:
            case 12:
            default:
                return " select a valid month (1-12)";

        }

        //public static void printMonthTitle(int year, int month){
            //System.out.print("    %s %d\n", getMonthName(month), year);

        }
    }

