import axios from "axios";

const url = import.meta.env.VITE_API_URL;

export const axiosClient = axios.create({
  baseURL: url,
});

axiosClient.interceptors.response.use(
  function (response) {
    return response;
  },
  function (error) {
    let res = error.response;
    if (res.status == 401) {
      console.error(
        "Looks like there was a problem. Status Code:" + res.status
      );
    }
    console.error("Looks like there was a problem. Status Code:" + res.status);
    return Promise.reject(error);
  }
);
