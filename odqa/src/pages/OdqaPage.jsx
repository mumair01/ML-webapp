import React, { useState } from "react";
import { Form, Button, Card } from "react-bootstrap";

const OdqaPage = () => {
  const [context, setContext] = useState("");
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState("");

  const executeModel = async () => {
    const result = await fetch("/api/execute", {
      method: "post",
      body: JSON.stringify({
        modelName: "distilbert-base-cased-distilled-squad",
        task: "question-answering",
        executeKwargs: {
          "input_data": {
            "question": question,
            "context": context,
          },
        },
      }),
      headers: {
        "Content-Type": "application/json",
      },
    }).catch((error) => console.log(error));
    const body = await result.json();
    setResult(JSON.stringify(body));
  };

  return (
    <>
      <Form>
        <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
          <Form.Label>Context</Form.Label>
          <Form.Control
            as="textarea"
            rows={3}
            onChange={(event) => setContext(event.target.value)}
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
          <Form.Label>Question</Form.Label>
          <Form.Control
            as="textarea"
            rows={3}
            onChange={(event) => setQuestion(event.target.value)}
          />
        </Form.Group>
        <Button
          variant="primary"
          type="submit"
          onClick={(event) => {
            event.preventDefault();
            executeModel();
          }}
        >
          Submit
        </Button>
      </Form>
      <h2>Result</h2>
      <Card>
        <Card.Body>{result}</Card.Body>
      </Card>
    </>
  );
};

export default OdqaPage;
