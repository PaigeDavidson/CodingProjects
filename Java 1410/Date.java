import java.util.Objects;

public class Date {
    private int year;
    private int month;
    private int day;
    private String whatCalender;

    public Date(){

    }
    public Date(int year, int month, int day, String whatCalender){
        this.year = year;
        this.month = month;
        this.day = day;
        this.whatCalender = whatCalender;
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
        if(Objects.equals(this.whatCalender, "gregorianDate")){
            int year = getYear();
            if(year % 4 == 0 && year % 100 != 0){
                return true;
            } else if(year % 400 == 0){
                return true;
            }else{
                return false;
            }
        }else {
            if(getYear() % 4 == 0){
                return true;
            }else{
                return false;
            }
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
    int getMonth(){
        return this.month;
    }
    int getYear(){
        return this.year;
    }
    int getDayOfMonth(){
        return this.day;
    }
    public int getNumberOfDaysInMonth(int year, int month){
        if(month == 9 || month == 4 || month == 6 || month == 11){
            return 30;
        }else if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){
            return 31;
        }else{
            if(isLeapYear()){
                return 29;
            }else{
                return 28;
            }
        }
    }
    public int getNumberOfDaysInYear(int year){
        if(isLeapYear()){
            return 366;
        }else{
            return 365;
        }
    }
    public String getMonthName(int month){
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
//    public void setYear(int year){
//        this.year = year;
//    }
//    public void setMonth(int month){
//        this.month = month;
//    }
//    public void setDay(int day){
//        this.day = day;
//    }
//    public int getDaysToAdd(){
//        return daysToAdd;
//    }
}