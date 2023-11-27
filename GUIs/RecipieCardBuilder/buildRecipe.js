const recipeName = document.getElementById("recipeName");
const ingredientList = document.getElementById("ingredient-items");
const showList = document.createElement("div");
//instructions
const instructionList = document.getElementById("instruction-items");
const showInstructionList = document.createElement("div");
//ingredients
const ingredientInput = document.getElementById("ingredient")
const instructionInput = document.getElementById("instruction")
//buttons
const saveButton = document.getElementById("save");
const resetButton = document.getElementById("reset");
const addIngredientButton = document.getElementById("addIngredient");
const addInstructionButton = document.getElementById("addInstruction");

const DeleteMessage = document.getElementById("DeleteMessage");

//Ingredient placeholder
const placeholderIngredients = document.createElement("div");
placeholderIngredients.innerHTML = `
    <div class="placeholder">
      <label>Ingredients will Appear Here</label>
    </div>
  `;

let numIngredients = 0;
const mapIngredients = [];

//make html div for a new ingredient and create event listneners for deleting the elements
function createHTML(htmlString, text){
    const container = document.createElement("div");
    container.innerHTML = htmlString;

    // event listener to delete element on click
    container.addEventListener("click", (e) => {
        container.remove();
        numIngredients -= 1;
        //also delete element from array 
        let index = mapIngredients.findIndex(x => x === text); 
        mapIngredients.splice(index, 1);
        //put placeholder back if all elements are deleted
        if(numIngredients == 0){
            ingredientList.replaceChildren(placeholderIngredients);
        }
        //acessibility delete message
        DeleteMessage.textContent = `${text} has been removed from the list.`;
    });

    //add event listener to delete on enter key when element is in focus
    container.addEventListener("keydown", (e) => {
        if(e.code === "Enter"){
            container.remove();
            numIngredients -= 1;

            let index = mapIngredients.findIndex(x => x === text); 
            mapIngredients.splice(index, 1);
            
            if(numIngredients == 0){
                ingredientList.replaceChildren(placeholderIngredients);
            }

            DeleteMessage.textContent = `${text} has been removed from the list.`;
        }
    });

    return container;
}

//create the list of ingredients
function createIngredient() {
    // replace the placeholder div with the elements
    ingredientList.replaceChildren(showList);
    const text = ingredientInput.value;
    numIngredients += 1;
    const ingredient = createHTML(`
      <div class="ingredient-item">
        <label>${text}</label>
      </div>
    `, text);  
    // tab index so user can tab through the elements they create and delete them
    ingredient.tabIndex = 0; 

    showList.appendChild(ingredient);
    mapIngredients.push(ingredientInput.value);
    //reset input field to the default placeholder once element is created 
    ingredientInput.value = "";
  }

//make it so it creates an ingredient when you press enter
ingredientInput.addEventListener("keypress", (e) => {
    if (e.code === "Enter") {
        createIngredient();
    }
  });

  //instructions part*********************************************************************************

  let numInstructions = 0;
  const mapInstructions = [];

  const placeholderInstructions = document.createElement("div");
  placeholderInstructions.innerHTML = `
  <div class="placeholder">
    <label>Instructions will Appear Here</label>
  </div>
`;


  function createHTMLInstructions(htmlString, text){
    const container = document.createElement("div");
    container.innerHTML = htmlString;

    //add event listener to delete instruction element on a click
    container.addEventListener("click", (e) => {
        container.remove();
        DeleteMessage.textContent = `${text} has been removed from the list.`;

       //also delete from array of instructions
        let index = mapInstructions.findIndex(x => x === text); 
        mapInstructions.splice(index, 1);

        numInstructions -= 1;
        if(numInstructions == 0){
            instructionList.replaceChildren(placeholderInstructions);
        }
    });
    // another event listener so user can also delete on an enter keypress when element is in focus
    container.addEventListener("keydown", (e) => {
        if(e.code === "Enter"){
            container.remove();
            DeleteMessage.textContent = `${text} has been removed from the list.`;

            let index = mapInstructions.findIndex(x => x === text); 
            mapInstructions.splice(index, 1);
    
            numInstructions -= 1;
            if(numInstructions == 0){
                instructionList.replaceChildren(placeholderInstructions);
            }
        }
        
    });
    return container;
}

  //create list of instructions
  function createInstruction() {
    instructionList.replaceChildren(showInstructionList);
    const text = instructionInput.value;
    numInstructions += 1;
    const instruction = createHTMLInstructions(`
      <div class="instruction-item">
        <label>${text}</label>
      </div>
    `, text);
    instruction.tabIndex = 0;
    showInstructionList.appendChild(instruction);
    mapInstructions.push(instructionInput.value);
    instructionInput.value = "";
  }

// event listener to create an instruction element on enter keypress
instructionInput.addEventListener("keypress", (e) => {
    if (e.code === "Enter") {
        createInstruction();
    }
  });

//add event listener to update lists with the add button
addIngredientButton.addEventListener("click", createIngredient);
addInstructionButton.addEventListener("click", createInstruction);

//reset recipe page
function reset(){

    recipeName.value = "";

    ingredientList.replaceChildren(placeholderIngredients);
    showList.replaceChildren("");
    instructionList.replaceChildren(placeholderInstructions);
    showInstructionList.replaceChildren("");

    mapIngredients.splice(0, mapIngredients.length);
    mapInstructions.splice(0, mapInstructions.length);
}

//event listeners so user can reset page by either clicking the reset button or pressing enter when button is in focus
resetButton.addEventListener("click", reset);

resetButton.addEventListener("keypress", (e) => {
    if (e.code === "Enter") {
        reset();
    }
});

saveButton.addEventListener("click", () => writeRecipeToFile(
    recipe = {
        title: recipeName.value, 
        ingredients: mapIngredients, 
        instructions: mapInstructions}
) );
saveButton.addEventListener("keypress", (e) => {
    if (e.code === "Enter") {
        writeRecipeToFile(
            recipe = {
                title: recipeName.value, 
                ingredients: mapIngredients, 
                instructions: mapInstructions}
        );
    }
});