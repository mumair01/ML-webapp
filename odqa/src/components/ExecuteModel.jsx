import React from "react";

const executeModel = (modelName, task, executeKwargs) => {
  const execute = async () => {
    const result = await fetch("/api/execute", {
      method: "post",
      body: JSON.stringify({
        modelName: modelName,
        task: task,
        executeKwargs: executeKwargs,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    const body = await result.json();
    console.log(body);
    return body;
  };
  return execute();
};

export default executeModel;
