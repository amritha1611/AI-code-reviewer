# AI Code Reviewer using gpt-4o-mini and Streamlit

AI Code Reviewer is a simple web application built using Streamlit and OpenAI's API. It allows users to input Python code and receive a detailed review that includes identified bugs, issues, and suggestions for improvement, along with a corrected version of the code.

## Features

- **Code Analysis**: Identifies bugs, issues, and areas for improvement in Python code.
- **Code Fixing**: Provides an improved version of the input code.
- **User-Friendly Interface**: Easy-to-use Streamlit-based interface.

## Requirements

To run this project locally, you'll need:

- Python 3.7 or later
- Streamlit
- OpenAI Python SDK

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-code-reviewer.git
   cd ai-code-reviewer
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key:
   - Save your API key in a file located at `keys/.openai_api_key.txt`.
   - The file should contain only the API key.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Paste your Python code in the text area and click **Generate** to receive the review.

## File Structure

```
.
├── app.py                  # Main application file
├── keys/
│   └── .openai_api_key.txt # File containing the OpenAI API key
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Example

### Input:
```python
x = input("Enter a number")
print(x*2)
```

### Output:
**Bug Report**:
- The `input` function returns a string, and multiplying it by 2 will result in string concatenation instead of numerical multiplication.

**Fixed Code**:
```python
x = int(input("Enter a number: "))
print(x * 2)
```

## Contributing

Contributions are welcome! If you have suggestions for improving this project, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy using AI Code Reviewer!
