const loanAmountObj = document.getElementById("loanAmount"); 
const anualInterestRateObj = document.getElementById("annualInterestRate"); 
const numberOfYearsObj = document.getElementById("numberOfYears"); 
const mOutput = document.getElementById("mortgageOutput");

let mElements = [loanAmountObj, anualInterestRateObj, numberOfYearsObj]
let mElementsName = ["Loan amount entered is not a number", 
"Interest Rate entered is not a number", 
"Number of years entered is not a number"]

//set default values for elements if incorrect values are supplied
function defultValue(element){
    if(element === loanAmountObj){
        loanAmountObj.value = 100000;
    }
    if(element === anualInterestRateObj){
        anualInterestRateObj.value = 5;
    }
    if(element === numberOfYearsObj){
        numberOfYearsObj.value = 30;
    }
}

function calculate(){
    let monthlyRate = (parseFloat(anualInterestRateObj.value)/100)/ 12;
    let numPayments = parseFloat(numberOfYearsObj.value) * 12;

    let numerator = monthlyRate * Math.pow((1 + monthlyRate),numPayments);
    let denominator = Math.pow((1 + monthlyRate),numPayments) - 1;

    let payment = parseFloat(loanAmountObj.value) * (numerator / denominator);
    if(Number.isNaN(payment)){
        return("You have provided invalid input")
    }else{
        return payment.toFixed(2);
    }
}

// first display payment with default values id user provides no input
mOutput.innerHTML = `Monthly Payment: $${calculate()}`

function calculateMortgage(){
    for (let i = 0; i < mElements.length; i++){
        //if no values are provided or the user blurs the field before entering a new value, calculate with default values
        if(mElements[i].value === ""){
            defultValue(mElements[i]);
            mOutput.innerHTML = `Monthly Payment: $${calculate()}`
        }
        //if the user provides input that is not a number display an error message
        if(Number.isNaN(parseFloat(mElements[i].value))){
            mOutput.innerHTML = `${mElementsName[i]}`;
            return;
        }
        //otherwise calculate payments with user input
        else{
            mOutput.innerHTML = `Monthly Payment: $${calculate()}`
        }
    }

}

loanAmountObj.addEventListener("blur", calculateMortgage);
anualInterestRateObj.addEventListener("blur", calculateMortgage);
numberOfYearsObj.addEventListener("blur", calculateMortgage);