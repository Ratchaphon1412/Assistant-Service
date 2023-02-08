import axios from "axios";
// import FormData from "form-data";

// const axios = require("axios");


const instance = axios.create({
    baseURL: "http://localhost:8000/api/",
});
instance.defaults.headers.common['Accept'] = 'application/json;charset=UTF-8';
instance.defaults.headers.common['Content-Type'] = 'application/json;charset=UTF-8';


export const ai = {
    async getAiResponse(message) {
        try {
            // let data = new FormData();
            // console.log(message);
            // data.append('query', message);
            // let response = await instance.post("ai/", {
            //     data: data,
            //     headers: data.getHeaders()
            // });
            let data = JSON.stringify({ "query": message });

            let response = await instance.post("ai/", data);
            return response.data;

        }

        catch (e) {
            console.error(e);
        }
    },
    async getKnowledge(message) {
        let data = JSON.stringify({
            "question": message
        })
        try {
            let response = await instance.post("knowledge/", data);
            return response.data;
        }
        catch (e) {
            console.error(e);
        }


    },
    async getAudio(message) {
        let data = JSON.stringify({
            "text": message
        })
        try {
            let response = await instance.post("texttospeech/", data);
            return response.data;
        }
        catch (e) {
            console.error(e);
        }

    }


}







// module.exports = instance;

// export default instance;