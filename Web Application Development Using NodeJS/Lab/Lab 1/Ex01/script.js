const imageLink = document.getElementById("imageLink");
const imageDisplay = document.getElementById("image");

const loadImage = () => {
    const imageURLInput = document.getElementById("imageUrl").value;

    if (!imageURLInput) {
        alert("Provide URL");
        return;
    }

    const xhr = new XMLHttpRequest();

    xhr.onload = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const { response } = xhr;
            const url = URL.createObjectURL(response);

            imageDisplay.setAttribute("src", url);
            imageLink.href = url;
        } else {
            console.log("Not ok");
        }
    };

    xhr.open("GET", imageURLInput, true);
    xhr.responseType = "blob";

    xhr.send();
};
