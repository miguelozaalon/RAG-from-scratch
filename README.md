# RAG from scratch

This project implements an insurance assistant using a Retrieval-Augmented Generation (RAG) model to answer insurance-related questions.
It can be used to answer questions on any topic that is passed to it.

## Features

- Uses the OpenAI API to generate responses.
- Implements Jaccard similarity to select the most relevant documents.
- Preprocesses documents to improve comparison.
- Selects the k most relevant documents for each query.

## Requirements

- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/miguelozaalon/RAG-from-scratch.git
   cd RAG-from-scratch
   ```

2. Install dependencies:
   ```
   pip install python-dotenv openai
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

Run the main script:

```
python rag.py
```

Enter your query when prompted, and the assistant will generate a response based on the provided insurance information.

## Code Structure

- `rag.py`: Contains all the assistant logic, including:
  - Document loading
  - Jaccard similarity calculation
  - Document preprocessing
  - Relevant document selection
  - Response generation using the OpenAI API

## How it works

1. The user enters a query.
2. The system calculates the similarity between the query and the available documents.
3. The k most relevant documents are selected.
4. A prompt is generated for the OpenAI API including the selected documents.
5. The OpenAI API generates a response based on the prompt and the user's query.
6. The response is displayed to the user.

## License

[MIT](https://choosealicense.com/licenses/mit/)