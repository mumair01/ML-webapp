import React from "react";
import executeModel from "../components/ExecuteModel";

const OdqaPage = () => {
  const result = executeModel(
    "distilbert-base-cased-distilled-squad",
    "question-answering",

    {
      "input_data": {
        "question": "What is the name of the repository ?",
        "context":
          "Pipeline has been included in the huggingface/transformers repository",
      },
    }
  );
  console.log(result);

  return <p>HI!</p>;
};

export default OdqaPage;
