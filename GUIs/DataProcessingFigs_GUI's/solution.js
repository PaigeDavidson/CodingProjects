/*
  filter: returns a subset of the input data that contains only the items for which the predicate 
  returns true
  @data: an array of any arbitrary data
  @predicate: a function that takes a single datapoint as an argument. Returns either true or false.
  @return: a new array that contains all of the values in data
           for which the predicate function returns true
*/
function filter(data, predicate){
    let subsetArray = [];
    for(dataPoint of data){
        if(predicate(dataPoint)){
            subsetArray.push(dataPoint);
        }
    }
    return subsetArray;
}

/*
  findLast: finds the last value in an array that meets the condition specified in the predicate
  @data: an array of any arbitrary data
  @predicate: a function that takes a single datapoint as an argument. Returns either true or false.
  @return: a single data point from data
*/

function findLast(data, predicate){
    let predicateArray = [];
    for(dataPoint of data){
      if(predicate(dataPoint)){
        predicateArray.push(dataPoint);
    }
    }
    return predicateArray[predicateArray.length - 1];
}

/*
  map: creates a new array based on the input array where the value at each position in the array is 
  the result of the callback function.
  @data: an array of any arbitrary data
  @callback: a function that takes a single datapoint as an argument. Returns a new value based on 
  the input value
  @return: a new array of the callback function results
*/

function map(data, callback){
    let functionRetultsArray = [];
    for(dataPoint of data){
        functionRetultsArray.push(callback(dataPoint));
    }
    return functionRetultsArray;
}

/*
  pairIf: creates a new array based on the input arrays where the value at each position is an 
          array that contains the 2 values that pair according to the predicate function.
  @data1: an array of any arbitrary data
  @data2: an array of any arbitrary data
  @predicate: a function that takes a single datapoint from each input array as an argument. 
  Returns true or false
  @return: the newly created array of pairs
*/

function pairIf(data1, data2, predicate){
  let pairArray = [];
  for(let dataPoint1 of data1){
    for(let dataPoint2 of data2){
      if(predicate(dataPoint1, dataPoint2)){
        pairArray.push([dataPoint1, dataPoint2]);
      }
    }
  }
    return pairArray;
}

/*
  reduce: creates an accumulated result based on the reducer function. The value returned is returned
          is the return value of the reducer function for the final iteration.
  @data: an array of any arbitrary data
  @reducer: a function that takes a single datapoint from each input array as an
            argument and the result of the reducer function from the previous iteration.
            Returns the result to be passed to the next iteration
  @initialValue: the starting point for the reduction.
  @return: the value from the final call to the reducer function.
*/ 

function reduce(data1, reducer, initialValue){
  for (value of data1) {
    initialValue = reducer(value, initialValue);
  }
  return initialValue;
    
}

// now answer the questions with the functions

// How many invalid transactions are there?
const jamArray = ["FIG_JAM", "FIG_JELLY", "SPICY_FIG_JAM", "ORANGE_FIG_JELLY"]

const invalidArray = filter(transactions, (datapoint) => {
  return !(datapoint["amount"] && jamArray.includes(datapoint["product"]));
});

let numInvalid = invalidArray.length;

// How many duplicate customers are there?

const pairArray = pairIf(customers, customers, (datapoint1, datapoint2) =>
  (datapoint1["emailAddress"] === datapoint2["emailAddress"]) && (datapoint1["id"] !== datapoint2["id"]));

let numDuplicates = (pairArray.length / 2);

// // How much was the most recent transaction that was over $200?
const recentTransaction = findLast(transactions, (datapoint) => (datapoint["amount"] > 200));


// How many small, medium, and large transactions are there?
const validArray = filter(transactions, (datapoint) => {
  return (datapoint["amount"] && jamArray.includes(datapoint["product"]));
});
// small - reduce function, under $25
const smalltransactions = reduce(validArray, (transaction, initialValue) => {
  if(transaction["amount"] < 25) {
    initialValue.total++;

  } 
  return initialValue;
}, {total: 0});

// medium - reduce function between $25 and $75
const mediumTransaction = reduce(validArray, (transaction, initialValue) => {
  if(25 <= transaction["amount"] && transaction["amount"] < 75) {
    initialValue.total++;

  } 
  return initialValue;
}, {total: 0});

//large Transaction - $75 and over
const largeTransaction = reduce(validArray, (transaction, initialValue) => {
  if(transaction["amount"] >= 75) {
    initialValue.total++;

  } 
  return initialValue;
}, {total: 0});



// Which customers have at least one transaction over $200?

// Filter the list to get only transactions over $200
bigTransactionsArray = filter(validArray, (datapoint) => datapoint["amount"] > 200);

// Pair each transaction with it's customer
transactionPersonPairs = pairIf(bigTransactionsArray, customers, (transaction, customer) => {
  return (transaction["customerId"] === customer["id"]);
});
// Reduce the pairs into a list of unique customer objects
const reducedList = reduce(transactionPersonPairs, (pair, initialValue) => {
  if(!initialValue.includes(pair[1])){
    initialValue.push(pair[1]);
  }
  return initialValue;
}, []);

// Map over the reduced list to get the names of the customers
customerNames = map(reducedList, (datapoint) => {
  return datapoint["firstName"] + " " + datapoint["lastName"];
});


console.log("Number of invalid transactions: " + numInvalid);
console.log("Number of duplicate customers: " + numDuplicates);
console.log("Most recent transaction over $200: $" + recentTransaction["amount"]);
console.log("Number of small transactions: " + smalltransactions.total);
console.log("Number of medium transaction: " + mediumTransaction.total);
console.log("Number of large transactions: " + largeTransaction.total);
console.log("Customers with transactions over $200: ")
console.log(reducedList);
console.log("Names of customers with transactions over $200: ");
console.log(customerNames);