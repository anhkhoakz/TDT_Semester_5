const { path } = require("express/lib/application");
const https = require("https");

const getOptions = {
    hostname: "web-nodejs-502070-wiolshzi6q-uc.a.run.app",
    path: "/students",
    port: 443,
    method: "GET",
};

const postOptions = {
    hostname: "web-nodejs-502070-wiolshzi6q-uc.a.run.app",
    path: "/students",
    port: 443,
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
};

const request = () => {
    return new Promise((resolve, reject) => {
        const req = https.request(getOptions, async (res) => {
            try {
                const user = await parseBody(res);
                resolve(user);
            } catch (error) {
                reject(error);
            }
        });

        req.on("error", (err) => {
            console.error("Request error:", err);
            reject(err);
        });

        req.setTimeout(5000, () => {
            console.error("Request timed out");
            req.abort();
            reject(new Error("Request timed out"));
        });

        req.end();
    });
};

const postRequest = (data) => {
    return new Promise((resolve, reject) => {
        const req = https.request(postOptions, async (res) => {
            try {
                const response = await parseBody(res);

                resolve(response);
            } catch (error) {
                reject(error);
            }
        });

        req.on("error", (err) => {
            console.error("Request error:", err);
            reject(err);
        });

        req.setTimeout(5000, () => {
            console.error("Request timed out");
            req.abort();
            reject(new Error("Request timed out"));
        });

        req.write(JSON.stringify(data));
        req.end();
    });
};

const getUserById = (id) => {
    const getOptions = {
        hostname: "web-nodejs-502070-wiolshzi6q-uc.a.run.app",
        path: `/students/${id}`,
        port: 443,
        method: "GET",
    };

    return new Promise((resolve, reject) => {
        const req = https.request(getOptions, async (res) => {
            try {
                const response = await parseBody(res);
                resolve(response);
            } catch (error) {
                reject(error);
            }
        });

        req.on("error", (err) => {
            console.error("Request error:", err);
            reject(err);
        });

        req.setTimeout(5000, () => {
            console.error("Request timed out");
            reject(new Error("Request timed out"));
        });

        req.end();
    });
};

const deleteRequest = (id) => {
    const deleteOptions = {
        hostname: "web-nodejs-502070-wiolshzi6q-uc.a.run.app",
        path: `/students/${id}`,
        port: 443,
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    };

    return new Promise((resolve, reject) => {
        const req = https.request(deleteOptions, async (res) => {
            try {
                const response = await parseBody(res);
                resolve(response);
            } catch (error) {
                reject(error);
            }
        });

        req.on("error", (err) => {
            console.error("Request error:", err);
            reject(err);
        });

        req.setTimeout(5000, () => {
            console.error("Request timed out");
            reject(new Error("Request timed out"));
        });

        req.end();
    });
};

const putRequest = (id, data) => {
    const putOptions = {
        hostname: "web-nodejs-502070-wiolshzi6q-uc.a.run.app",
        path: `/students/${id}`,
        port: 443,
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
    };

    return new Promise((resolve, reject) => {
        const req = https.request(putOptions, async (res) => {
            try {
                const response = await parseBody(res);
                resolve(response);
            } catch (error) {
                reject(error);
            }
        });

        req.on("error", (err) => {
            console.error("Request error:", err);
            reject(err);
        });

        req.setTimeout(5000, () => {
            console.error("Request timed out");
            reject(new Error("Request timed out"));
        });

        req.write(JSON.stringify(data));
        req.end();
    });
};

const patchRequest = (id, data) => {
    const patchOptions = {
        hostname: "web-nodejs-502070-wiolshzi6q-uc.a.run.app",
        path: `/students/${id}`,
        port: 443,
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
        },
    };

    return new Promise((resolve, reject) => {
        const req = https.request(patchOptions, async (res) => {
            try {
                const response = await parseBody(res);
                resolve(response);
            } catch (error) {
                reject(error);
            }
        });

        req.on("error", (err) => {
            console.error("Request error:", err);
            reject(err);
        });

        req.setTimeout(5000, () => {
            console.error("Request timed out");
            reject(new Error("Request timed out"));
        });

        req.write(JSON.stringify(data));
        req.end();
    });
};

function parseBody(res) {
    return new Promise((resolve, reject) => {
        let data = "";

        res.on("data", (chunk) => {
            data += chunk;
        });

        res.on("end", () => {
            try {
                resolve(JSON.parse(data));
            } catch (error) {
                reject("Error parsing JSON: " + error);
            }
        });

        res.on("error", (err) => {
            reject("Response error: " + err);
        });
    });
}

module.exports = {
    request,
    postRequest,
    getUserById,
    deleteRequest,
    putRequest,
    patchRequest,
};
