document.getElementById("button-html").innerText = `
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
    
    <button class="button" id="theButton">
        Button
    </button>

    <!-- The same button with an icon: -->
    <button class="button" id="theButton2">
        <a><span class="material-icons">favorite</span></a>
        Button
    </button>

</body>
</html>
`;

const button = document.getElementById("theButton");
const button2 = document.getElementById("theButton2");

button.addEventListener("click", () => {
    console.log("button was clicked");
    //add you button action here
});
button2.addEventListener("click", () => {
    console.log("button 2 was clicked");
    //add you button action here
});