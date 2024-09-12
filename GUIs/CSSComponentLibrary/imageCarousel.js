document.getElementById("imageCarousel-html").innerText = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="yourJSFile.js" defer></script>
    <link rel="stylesheet" href="yourCSSFile.css">
    <title>Document</title>
</head>
<body>
    <div class="container" id="container">
        <div class="images">
            <img class="image" src="imgOne.jpeg" alt="img1">
            <img class="image" src="imgTwo.jpeg" alt="img2">
            <img class="image" src="imgThree.jpeg" alt="img3">
            <img class="image" src="imgFour.jpeg" alt="img4">
            <img class="image" src="imgFive.jpeg" alt="img5">
        </div>
    </div>
</body>
</html>
`;

const imagesContainer = document.querySelector('.images');
let images = document.querySelectorAll('.image');
let index = 0;

function showImage(index) {
    const translateValue = -index * 100 + '%';
    imagesContainer.style.transition = "transform 0.5s ease-in-out";
    imagesContainer.style.transform = `translateX(${translateValue})`;
}

function nextImage() {
    // Clone and append the images
    let clone = images[index].cloneNode(true);
    imagesContainer.appendChild(clone);

    // Update the images NodeList
    images = document.querySelectorAll('.image');

    // Update the index and show the next image
    index++;
    showImage(index);
}

// Set an interval to transition to the next image every 3 seconds
nextImage();
setInterval(nextImage, 3000);

