const parseBody = (res) => {
    return new Promise((resolve, reject) => {
        try {
            let body = "";
            res.on('data', (data) => {
                body += data.toString();
            })
            res.on("end", () => {
                body = JSON.parse(body);
            })
            return resolve(body);
        } catch (error) {
            return reject(error);
        }
    })
}
