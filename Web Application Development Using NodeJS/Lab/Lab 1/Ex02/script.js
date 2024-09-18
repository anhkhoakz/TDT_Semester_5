const studentListTBody = document.getElementById("studentListTBody");
const studentListDataUrl = "./students.json";

const downloadByFetch = async () => {
    try {
        const response = await fetch(studentListDataUrl);

        response.json().then((response) => {
            displayTable(response);
        });
    } catch (error) {
        console.error("Error:", error);
    }
};

const downloadByAjax = () => {
    const xhr = new XMLHttpRequest();
    xhr.onload = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            displayTable(response);
        } else {
            console.log("Not ok");
        }
    };
    xhr.open("GET", studentListDataUrl, true);
    xhr.send();
};

const displayTable = (response) => {
    studentListTBody.innerHTML = "";
    const peopleData = response.data;
    peopleData.forEach((personData) => {
        const { id, name, age } = personData;
        studentListTBody.innerHTML += `
            <tr>
                <td>${id}</td>
                <td>${name}</td>
                <td>${age}</td>
            </tr>
        `;
    });
};

const reset = () => {
    studentListTBody.innerHTML = "";
};
