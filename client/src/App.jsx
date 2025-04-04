import { useState } from "react";
import "./App.css";
import TextField from "./components/TextField";
import {
  ImageGenerateAPI,
  generateImageFromCaption,
} from "./controller/image_handler";

function App() {
  const [selected, setSelected] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  function fetchData(prompt) {
    setLoading(true);
    setError(null);

    ImageGenerateAPI.textToImage({ prompt: prompt })
      // generateImageFromCaption({ prompt: prompt })
      .then(async function (response) {
        console.log(response);
        const imageUrl = URL.createObjectURL(response.data);

        setData(imageUrl);
        setLoading(false);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  return (
    <>
      <h1>Image Chef</h1>
      <TextField selected={selected} fetchData={fetchData} />
      <div className="card-top">
        <button
          className={`card-button ${
            selected == "TextToImage" ? "selected-button" : ""
          }`}
          onClick={() => setSelected("TextToImage")}
        >
          Text To Image
        </button>
        <button
          className={`card-button ${
            selected == "TGImageToImage" ? "selected-button" : ""
          }`}
          onClick={() => setSelected("TGImageToImage")}
        >
          Text Guided Image to Image
        </button>
      </div>
      {loading ? (
        "loading..."
      ) : (
        <img className="generated-image" src={data} alt="Generated Image" />
      )}
    </>
  );
}

export default App;
