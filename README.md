# mental_health_app
# FastAPI Server for Mental Health Chatbot and Data Classification

This repository contains a FastAPI server with two endpoints: `/rag` and `/classification`. These endpoints serve as a mental health chatbot utilizing Retrieval-Augmented Generation (RAG) and a data classification model, respectively.

## Instructions for Setup and Execution

### Prerequisites
- Python 3.8+
- Docker (optional, for containerization)

### Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/mental-health-chatbot-classification.git
    cd mental-health-chatbot-classification
    ```

2. **Setup a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Train the classifier:**
    ```bash
    python app/models/classifier.py
    ```

4. **Run the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```

5. **Dockerization (Optional):**

    - **Build the Docker image:**
      ```bash
      docker build -t mental-health-app .
      ```

    - **Run the Docker container:**
      ```bash
      docker run -d -p 80:80 mental-health-app
      ```

6. **Deploy on Hugging Face (Optional):**

    Follow the Hugging Face Spaces [documentation](https://huggingface.co/docs/hub/spaces-overview) to deploy your app.

7. **Testing the Endpoints:**

    Use tools like Postman to test your endpoints.

## Endpoints

### /rag

- **Method**: POST
- **Request Body**: JSON object containing the prompt.
    ```json
    {
        "prompt": "I am feeling very anxious and stressed about my exams."
    }
    ```
- **Response**: JSON object containing relevant articles or blog posts.
    ```json
    {
        "response": "Here are some articles that might help you with your anxiety and stress: [Link1, Link2, Link3]"
    }
    ```

### /classification

- **Method**: POST
- **Request Body**: JSON object containing the data to be classified.
    ```json
    {
        "data": "Sample data to classify"
    }
    ```
- **Response**: JSON object containing the classification result.
    ```json
    {
        "category": "Category Name"
    }
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by opening issues or submitting pull requests. For any questions or suggestions, please contact [your-email@example.com](mailto:your-email@example.com).
 
