const {
    request,
    postRequest,
    getUserById,
    deleteRequest,
    putRequest,
    patchRequest,
} = require("../utils/http.config");

const getUsers = async () => {
    try {
        const users = await request();
        return users;
    } catch (error) {
        console.error("Error fetching users:", error);
        throw error;
    }
};

const getUser = (userId) => {
    try {
        const user = getUserById(userId);
        return user;
    } catch (error) {
        console.error("Error fetching user:", error);
        throw error;
    }
};

const addUser = async (user) => {
    try {
        const users = await getUsers();

        user.id = users.length + 1;

        const response = await postRequest(user);
        // console.log(response);

        return response;
    } catch (error) {
        console.error("Error adding user:", error);
        throw error;
    }
};

const deleteUser = (userId) => {
    try {
        const response = deleteRequest(userId);
        return response;
    } catch (error) {
        console.error("Error deleting user:", error);
        throw error;
    }
};

const updateUser = async (userId, user) => {
    try {
        const response = await putRequest(userId, user);
        return response;
    } catch (error) {
        console.error("Error updating user:", error);
        throw error;
    }
};

const patchUser = async (userId, user) => {
    try {
        const response = await patchRequest(userId, user);
        return response;
    } catch (error) {
        console.error("Error patching user:", error);
        throw error;
    }
};

module.exports = {
    getUsers,
    getUserById,
    addUser,
    deleteUser,
    updateUser,
    patchUser,
};
