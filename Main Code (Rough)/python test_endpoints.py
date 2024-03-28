import requests

# Define the base URL for your FastAPI server
BASE_URL = "http://localhost:5000"  # Update with your actual server address

# Example usage for finetune endpoint


# def test_finetune():
#     endpoint = "/finetune/"
#     directory_path = r"D:\RAG-based-Personal-AI-Assistant\Main Code\Data\empty"
#     response = requests.post(
#         BASE_URL + endpoint, json={"directory_path": directory_path})
#     if response.status_code == 200:
#         print(response.json())
#     else:
#         print("Error:", response.status_code)
#         print("Response:", response.text)

# Example usage for chat endpoint


def test_chat():
    endpoint = "/chat/"
    prompt = "what is AI?"
    response = requests.post(BASE_URL + endpoint, json={"prompt": prompt})
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error:", response.status_code)
        print("Response:", response.text)


# Test the endpoints
if __name__ == "__main__":
    # test_finetune()
    test_chat()
