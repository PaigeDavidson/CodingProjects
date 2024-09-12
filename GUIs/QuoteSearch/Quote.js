const search = document.getElementById("searchBar");
const searchButton = document.getElementById("searchButton")
const message = document.getElementById("Message")
const pinned = document.getElementById("pinned")
let pinnedList = [];

//enter keypress event
search.addEventListener("keypress", (e) => {
    if(e.code === "Enter") {
        moveToTop();
        //if the user tries to hit enter without anything in the search bar...
        if(search.value === ""){
            displayErrorMessage("Make sure to search for an author!", "Nothing was entered in the search bar");
        }else{
            renderQuotes(search.value);
        }
    }
});

//search button event listeners for click and enter keypress event
searchButton.addEventListener("click", (e) => {
    moveToTop();
    if(search.value === ""){
        displayErrorMessage("Make sure to search for an author!", "Nothing was entered in the search bar");
    }else{
        renderQuotes(search.value);
    }
});

searchButton.addEventListener("keypress", (e) => {
    if(e.code === "Enter") {
        moveToTop();
        //if the user tries to hit enter without anything in the search bar...
        if(search.value === ""){
            displayErrorMessage("Make sure to search for an author!", "Nothing was entered in the search bar");
        }else{
            renderQuotes(search.value);
        }
    }
});

//render random quote to start with
getQuote();

//move everything to the top when a user first searches
function moveToTop(){
    const everything = document.getElementById("everything")
    everything.classList.remove("centered");
    everything.classList.add("top");
}

//get a singular random quote
async function getQuote() {
    const result = await fetch("https://usu-quotes-mimic.vercel.app/api/random");
    const data = await result.json();
    document.getElementById("quote-content").innerText = data.content;
    document.getElementById("quote-author").innerText = `-${data.author}`;
}

//display error message
function displayErrorMessage(message, ariaMessage) {
    const errorMessageContainer = document.createElement("div");
    errorMessageContainer.innerText = message;
    errorMessageContainer.classList.add("error");

    errorMessageContainer.setAttribute("aria-label", ariaMessage)

    // Append the error message container to an existing element in the DOM
    const parentContainer = document.getElementById("errorMessage"); 
    parentContainer.appendChild(errorMessageContainer);
}

//change the css class when a user pinns a quote
function changePinnedCss(){
    const pinned = document.getElementById("quote")
    pinned.classList.remove("quote");
    pinned.classList.add("pinned")
}


// display list of quotes based on search
async function renderQuotes(author) {
    const result = await fetch(`https://usu-quotes-mimic.vercel.app/api/search?query=${author}`);
    const data = await result.json();
    
    // Check if quotes are available in the response
    if (data.results && data.results.length > 0) {
        // Clear existing quotes before displaying new ones (except pinned ones)
        clearQuotes();

        // Render pinned quotes first
        pinnedList.forEach(pinnedQuote => {
            displayQuote(pinnedQuote);
        });

        // Iterate through the quotes and display each one
        data.results.forEach(quote => {
            displayQuote(quote);
        });
    } else {
        // Handle the case where no quotes are found
        displayErrorMessage('No quotes found for the given search', "There werent any quotes found!");
    }
}

//create quote elements and add classes
function displayQuote(quote) {
    const quoteContainer = document.createElement("div");
    quoteContainer.classList.add("quotes");

    const quoteElement = document.createElement("div");
    quoteElement.classList.add("quote");

    //tab index so users can tab through the quotes and pin them
    quoteElement.tabIndex = 0;

    const contentElement = document.createElement("p");
    contentElement.innerText = quote.content;
    contentElement.classList.add("quote-content");

    const authorElement = document.createElement("p");
    authorElement.innerText = `-${quote.author}`;
    authorElement.classList.add("quote-author")

    quoteElement.appendChild(contentElement);
    quoteElement.appendChild(authorElement);

    quoteContainer.appendChild(quoteElement);

    // event listener to pin/unpin element on click
    quoteElement.addEventListener("click", (e) => {
        const quoteData = { content: quote.content, author: quote.author };

        if (isQuotePinned(quoteData)) {
            unpinQuote(quoteData);
            message.textContent = `A quote has been unpinned`;
        } else {
            pinQuote(quoteData);
            message.textContent = `A quote has been pinned`;
        }

        renderQuotes(search.value);
    });

    //event listener to in/unpin element on keypress enter event when element is in focus
    quoteElement.addEventListener("keypress", (e) => {
        if(e.code === "Enter"){
            const quoteData = { content: quote.content, author: quote.author };

            if (isQuotePinned(quoteData)) {
                unpinQuote(quoteData);
                message.textContent = `A quote has been unpinned`;
            } else {
                pinQuote(quoteData);
                message.textContent = `A quote has been pinned`;
            }

            renderQuotes(search.value);
        }
    });

    // Append the new container to the document body or another container of your choice
    document.body.appendChild(quoteContainer);
}

// Helper function to clear existing quotes - except pinned ones
function clearQuotes() {
    // Remove all elements with the class "quote-container"
    const existingQuoteContainers = document.querySelectorAll(".quote");
    existingQuoteContainers.forEach(container => container.remove());
    //remove any error messages
    const existingErrors = document.querySelectorAll(".error");
    existingErrors.forEach(container => container.remove());
}
// Function to check if a quote is pinned
function isQuotePinned(quoteData) {
    return pinnedList.some((pinnedQuote) => pinnedQuote.content === quoteData.content && pinnedQuote.author === quoteData.author);
}

// Function to pin a quote
function pinQuote(quoteData) {
    pinnedList.push(quoteData);
}

// Function to unpin a quote
function unpinQuote(quoteData) {
    const index = pinnedList.findIndex((pinnedQuote) => pinnedQuote.content === quoteData.content && pinnedQuote.author === quoteData.author);

    if (index !== -1) {
        pinnedList.splice(index, 1);
    }
}


