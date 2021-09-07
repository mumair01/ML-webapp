import React, { useState, useEffect } from "react";
import { Form, Button } from "react-bootstrap";

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

  return (
    <Form>
      <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
        <Form.Label>Context</Form.Label>
        <Form.Control as="textarea" rows={3} />
      </Form.Group>
      <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
        <Form.Label>Question</Form.Label>
        <Form.Control as="textarea" rows={3} />
      </Form.Group>

      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
};

export default OdqaPage;
