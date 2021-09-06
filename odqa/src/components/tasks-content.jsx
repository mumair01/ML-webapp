import OdqaPage from "../pages/OdqaPage";

const tasksPages = [
  {
    task: "question-answering",
    model: "distilbert-base-cased-distilled-squad",
    page: <OdqaPage />,
  },
];

export default tasksPages;
