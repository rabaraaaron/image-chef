import { axiosClient } from "./axios_config";

export function generateImageFromCaption(data) {
  return axiosClient.post("/text-to-image/", data);
}

export function generateImageFromImage(formData) {
  return axiosClient.post("/text-guided-image-to-image/", formData);
}

export const ImageGenerateAPI = {
  textToImage: async function (data) {
    const response = await axiosClient.request({
      url: "/text-to-image/",
      method: "POST",
      headers: {
        Accept: "*/*",
        "Content-Type": "application/json",
      },
      data: data,
      responseType: "blob",
    });

    return response;
  },
};
