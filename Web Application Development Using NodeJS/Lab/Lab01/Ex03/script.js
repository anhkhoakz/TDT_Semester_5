const imageLink = document.getElementById("imageLink");
const imageDisplay = document.getElementById("image");

const loadImage = async () => {
    const imageURLInput = document.getElementById("imageUrl").value;

    if (!imageURLInput) {
        alert("Provide URL");
        return;
    }

    try {
        const response = await fetch(imageURLInput);
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);

        imageDisplay.src = url;
        imageLink.href = url;
    } catch (error) {
        console.error("Error:", error);
    }
};
