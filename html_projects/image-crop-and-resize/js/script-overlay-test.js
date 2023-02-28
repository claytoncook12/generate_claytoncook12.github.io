const workingImage = document.getElementById("working-image"),
overlay = document.querySelector(".overlay"),
cropX = document.getElementById("cropX"),
cropXLength = document.getElementById("cropXLength"),
cropY = document.getElementById("cropY"),
cropYLength = document.getElementById("cropYLength");

const workingImageHeight = workingImage.getBoundingClientRect().height,
workingImageWidth = workingImage.getBoundingClientRect().width;

const scaleOverlay = () => {
    // Set Overlay to Image Size
    overlay.style.height = `${workingImageHeight}px`;
    overlay.style.width = `${workingImageWidth}px`;
    overlay.removeAttribute("hidden");
}

const setImageCropParameters = () => {
    cropX.value = 0;
    cropXLength.value = Math.round(workingImageWidth);
    cropXLength.max = Math.round(workingImageWidth);
    
    cropY.value = 0;
    cropY.max = Math.round(workingImageHeight);
    cropYLength.value = Math.round(workingImageHeight);
    cropYLength.max = Math.round(workingImageHeight);
}

cropY.addEventListener("change", (event) => {
    // Update Overlay Height
    overlay.style.top = `${event.target.value}px`;
    const newOverlayHeight = workingImageHeight - event.target.value;
    overlay.style.height = `${newOverlayHeight}px`;
    // Update Crop Y Length
    cropYLength.value = Math.round(workingImageHeight - event.target.value);
})

cropX.addEventListener("change", (event) => {
    // Update Overlay Width
    overlay.style.left = `${event.target.value}px`;
    const newOverlayWidth = workingImageWidth - event.target.value;
    overlay.style.width = `${newOverlayWidth}px`;
    // Update Crop X Length
    cropXLength.value = Math.round(workingImageWidth - event.target.value);
})

cropXLength.addEventListener("change", (event) => {
    overlay.style.width = `${event.target.value}px`;
})

cropYLength.addEventListener("change", (event) => {
    overlay.style.height = `${event.target.value}px`;
})

window.onload = function() {
    scaleOverlay();
    setImageCropParameters();
}