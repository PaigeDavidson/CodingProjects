const ProperNoun = document.getElementById("properNoun");
const Verb1 = document.getElementById("verb1");
const Verb2 = document.getElementById("verb2");
const Adjective = document.getElementById("adjective");
const Obj = document.getElementById("obj");
const button = document.getElementById("generate");
const output = document.getElementById("madLibsOutput");

let elements = [ProperNoun, Verb1, Verb2, Adjective, Obj];
let elementsName = ["a noun", "a verb", "another verb", "an adjective", "an object"]

function story() { 
    for (let i = 0; i < elements.length; i++){
        //check that the user has provided input
        if(elements[i].value === ""){
            output.innerHTML = `You must provide ${elementsName[i]}!`;
            return;
        }else{
            output.innerHTML = `Late one summer afternoon there was a fox named ${ProperNoun.value} who 
            had a ${Obj.value}. That afternoon, ${ProperNoun.value} lost the ${Obj.value} and was 
            very ${Adjective.value}. ${ProperNoun.value} went on a quest 
            to find the ${Obj.value}. ${ProperNoun.value} ${Verb1.value} and ${Verb2.value} untill it 
            found the ${Obj.value} and wasn't ${Adjective.value} anymore.`;   
        }
    }       

} 

button.addEventListener("click", story);
