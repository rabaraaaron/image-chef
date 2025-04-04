import React, { useState } from "react";

import "./TextField.css";

function TextField({ selected, fetchData }) {
  const [text, setText] = useState("");
  const handleChange = (event) => {
    setText(event.target.value);
    console.log(selected);
  };

  function enterKeyPress(e) {
    if (e.key === "Enter") {
      console.log("Key pressed:", e.key);
      console.log("Text Area: ", text);
      console.log("Selected: ", selected);
      fetchData(text);
      return true;
    }
  }

  return (
    <div class="form__group field">
      <input
        type="input"
        class="form__field"
        placeholder="Name"
        name="name"
        id="name"
        required
        value={text}
        onChange={handleChange}
        onKeyDown={enterKeyPress}
      />
      <label for="name" class="form__label">
        Prompt
      </label>
    </div>
  );
}

export default TextField;
