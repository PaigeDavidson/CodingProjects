document.getElementById("FAB-html").innerText = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
    <script src="yourJSFile.js" defer></script>
    <link rel="stylesheet" href="yourCSSFile.css">
    <title>Document</title>
</head>
<body>
    
    <button class="FAB" id="FAB">
        <!-- add your icon here -->
        <a><span class="material-icons">add</span></a>
    </button>

</body>
</html>
`;

const button = document.getElementById("FAB");

button.addEventListener("click", () => {
    console.log("button was clicked");
    //add you button action here
});