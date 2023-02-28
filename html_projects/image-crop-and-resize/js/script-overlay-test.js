const workingImage = document.getElementById("working-image"),
overlay = document.querySelector(".overlay"),
cropXLength = document.getElementById("cropXLength"),
cropYLength = document.getElementById("cropYLength");


const workingImageHeight = workingImage.getBoundingClientRect().height,
workingImageHeightStr = workingImageHeight.toString(),
workingImageWidth = workingImage.getBoundingClientRect().width,
workingImageWidthStr = workingImageWidth.toString();

const scaleOverlay = () => {
    // Set Overlay to Image Size
    overlay.style.height = workingImageHeightStr+"px";
    overlay.style.width = workingImageWidthStr+"px";
    overlay.removeAttribute("hidden");
}

const setImageCropParameters = () => {
    cropXLength.max = workingImageWidth;
    cropYLength.max = workingImageHeight;
}

window.onload = function() {
    scaleOverlay();
    setImageCropParameters();
}
