# ML Webapp

## About

THis project was developed as a personal project to showcase full-stack development using Express.js, React, and Flask as well as an ability to interact with ML frameworks including [transformers](https://huggingface.co/docs/transformers/index).

## Overview

This project contains three components: a React website for user interaction, an Express.js server to serve requests from the website, and a flask backend running ML models for different use cases. The landing page displays a list of models for multiple use cases including [Open Domain Question Answering](https://arxiv.org/abs/2101.00774).

## Supported Models

### Open Domain Question Answering

[Open Domain Question Answering](https://arxiv.org/abs/2101.00774) is the task of answering a question given a context. For example, the context could be a research paper that can be queried.

## Usage

Install dependencies using: `pip install -r requirements.txt`

To use, start the three components:

- Start the flask server using: `python ./model_server/flaskr/server.py`
- Start Express.js server using `cd node_server` and running `npm start `
- Start website using `cd odqa` and running `npm start`
