const { request, postRequest } = require("../utils/http.config");

const getUsers = async () => {
    try {
        const users = await request();
        return users;
    } catch (error) {
        console.error("Error fetching users:", error);
        throw error;
    }
}

const getUserById = (userId) => {
    console.log('getUserById', userId);
}

const addUser = async (user) => {
    try {

        user.id = Math.floor(Math.random() * 10000);
        console.log('addUser', user);


        const response = await postRequest(user);
        console.log('addUser', response);

        return response;
    } catch (error) {
        console.error("Error adding user:", error);
        throw error;
    }
}

module.exports = { getUsers, getUserById, addUser };
