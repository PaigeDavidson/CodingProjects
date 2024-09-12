public class GregorianDate{
    int year = 1970;
    int month = 1;
    int day = 1;

    public GregorianDate(){
        long millsSince = System.currentTimeMillis() + java.util.TimeZone.getDefault().getRawOffset();
        long seconds = millsSince / 1000;
        long minutes = seconds / 60;
        long hours = minutes / 60;
        long days = hours / 24;
        int intDays = (int) days;

        addDays(intDays);
    }
    public GregorianDate(int year, int month, int day){
        this.year = year;
        this.month = month;
        this.day = day;
    }
    public void addDays(int days){
        for(int i = 0; i < days; i++){
            day += 1;
            if(day > getNumberOfDaysInMonth(year, month)){
                day = 1;
                month += 1;
                if(month > 12){
                    month = 1;
                    year += 1;
                }
            }

        }
    }
    public void subtractDays(int days){
        for(int i = 0; i < days; i++){
            day -= 1;
            if(day == 0){
                month -= 1;
                if(month == 0){
                    month = 12;
                    year -= 1;
                }
                day = getNumberOfDaysInMonth(year, month);

            }
        }

    }
    public boolean isLeapYear(){
        int year = getYear();
        if(year % 4 == 0 && year % 100 != 0){
            return true;
        } else if(year % 400 == 0){
            return true;
        }else{
            return false;
        }
    }
    public void printShortDate(){
        int month = getMonth();
        int day = getDayOfMonth();
        int year = getYear();
        System.out.print(month + "/" + day + "/" + year);
    }
    public void printLongDate(){
        String month = getMonthName();
        int day = getDayOfMonth();
        int year = getYear();
        System.out.print(month + "/" + day + "/" + year);
    }

    public String getMonthName(){
        return getMonthName(getMonth());
    }

    public int getMonth(){
        return this.month;
    }
    public int getYear(){
        return this.year;
    }
    public int getDayOfMonth(){
        return this.day;
    }
    private boolean isLeapYear(int year){
        if(year % 4 == 0 && year % 100 != 0){
            return true;
        } else if(year % 400 == 0){
            return true;
        }else{
            return false;
        }
    }
    private int getNumberOfDaysInMonth(int year, int month){
        if(month == 9 || month == 4 || month == 6 || month == 11){
            return 30;
        }else if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){
            return 31;
        }else{
            if(isLeapYear(year)){
                return 29;
            }else{
                return 28;
            }
        }
    }
    private int getNumberOfDaysInYear(int year){
        if(isLeapYear(year)){
            return 366;
        }else{
            return 365;
        }
    }
    private String getMonthName(int month){
        String monthName = "";
        if(month == 1){
            monthName = "January";
            return monthName;
        }else if(month == 2){
            monthName = "February";
            return monthName;
        }else if(month == 3) {
            monthName = "March";
            return monthName;
        }    else if(month == 4) {
            monthName = "April";
            return monthName;
        }else if(month == 5) {
            monthName = "May";
            return monthName;
        }else if(month == 6) {
            monthName = "June";
            return monthName;
        }else if(month == 7) {
            monthName = "July";
            return monthName;
        }else if(month == 8) {
            monthName = "August";
            return monthName;
        }else if(month == 9) {
            monthName = "September";
            return monthName;
        }else if(month == 10) {
            monthName = "October";
            return monthName;
        }else if(month == 11) {
            monthName = "November";
            return monthName;
        }else if(month == 12) {
            monthName = "December";
            return monthName;
        }else {
            return null;
        }


    }

}