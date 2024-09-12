document.getElementById("navbar-html").innerText = `
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
    <div class="mask" id="mask"></div>
    <nav class="navbar">
        <div class="nav-header">
            <button class="icon-button" id="nav-button">
                <span class="material-icons">menu</span>
            </button>
            <h2>Your Title Here</h2>
        </div>
        <div class="links">
            <a class="navLink" href="#">Link 1</a>
            <a class="navLink" href="#">Link 2</a>
            <a class="navLink" href="#">Link 3</a>
            <a class="navLink" href="#">Link 4</a>
        </div>
    </nav>
</body>
</html>
`;

const navIcon = document.getElementById("nav-button");

navIcon.addEventListener("click", () => {
    console.log("Navigation icon was clicked");
});
