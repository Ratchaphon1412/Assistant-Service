import axios from "axios";

const instance = axios.create({
    baseURL: "https://localhost:8000/api/",
    headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",

    },
});

export default instance;