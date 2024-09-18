const localStorageTbody = document.getElementById("LocalStorageTBody");
const sessionStorageTbody = document.getElementById("sessionStorageTBody");

const addToLocalStorage = () => {
    if (!checkInput()) return;
    const data = getDataInput();
    let localStorageData = JSON.parse(localStorage.getItem("students")) || [];
    localStorageData.push(data);
    localStorage.setItem("students", JSON.stringify(localStorageData));
    displayLocalStorageData();
    clearInputs();
};

const addToSessionStorage = () => {
    if (!checkInput()) return;
    const data = getDataInput();
    let sessionStorageData =
        JSON.parse(sessionStorage.getItem("students")) || [];
    sessionStorageData.push(data);
    sessionStorage.setItem("students", JSON.stringify(sessionStorageData));
    displaySessionStorageData();
    clearInputs();
};

const getDataInput = () => {
    const id = Math.floor(Math.random() * 1000);
    const nameInput = document.getElementById("name");
    const ageInput = document.getElementById("age");
    return {
        id,
        name: nameInput.value,
        age: ageInput.value,
    };
};

const displayLocalStorageData = () => {
    const localStorageData = JSON.parse(localStorage.getItem("students")) || [];
    localStorageTbody.innerHTML = "";
    localStorageData.forEach((student, index) => {
        const row = `<tr>
            <td>${index + 1}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
        </tr>`;
        localStorageTbody.innerHTML += row;
    });
};

const displaySessionStorageData = () => {
    const sessionStorageData =
        JSON.parse(sessionStorage.getItem("students")) || [];
    sessionStorageTbody.innerHTML = "";
    sessionStorageData.forEach((student, index) => {
        const row = `<tr>
            <td>${index + 1}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
        </tr>`;
        sessionStorageTbody.innerHTML += row;
    });
};

const checkInput = () => {
    const nameInput = document.getElementById("name");
    const ageInput = document.getElementById("age");
    if (nameInput.value === "" || ageInput.value === "") {
        alert("Please fill all fields");
        return false;
    }
    return true;
};

const clearInputs = () => {
    document.getElementById("name").value = "";
    document.getElementById("age").value = "";
};

displayLocalStorageData();
displaySessionStorageData();
