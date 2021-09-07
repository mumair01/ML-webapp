import React, { useState, useEffect } from "react";

const OdqaPage = () => {
  const [result, setResult] = useState({});
  useEffect(() => {
    const execute = async () => {
      const result = await fetch("/api/execute", {
        method: "post",
        body: JSON.stringify({
          modelName: "distilbert-base-cased-distilled-squad",
          task: "question-answering",
          executeKwargs: {
            "input_data": {
              "question": "What is the name of the repository ?",
              "context":
                "Pipeline has been included in the huggingface/transformers repository",
            },
          },
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      const body = await result.json();
      setResult(body);
    };
    execute();
  }, []);

  return <p>{JSON.stringify(result)}</p>;
};

export default OdqaPage;
