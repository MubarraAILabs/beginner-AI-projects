# Gemini Chatbot with Gradio

A small Python chatbot with a Gradio web interface. It sends your message to Google Gemini and displays the response. The prompt is written to make Gemini respond as a data science instructor.

## What you need

- Python 3.10 or newer
- A Google Gemini API key
- Internet access

## 1. Get the project

Clone the repository, or download it from GitHub and extract it. Open a terminal in the `gradioUI` project folder, where `gradio_app.py` is located.

```bash
git clone <repository-url>
cd <repository-folder>/gradioUI
```

If you downloaded a ZIP, open a terminal in the extracted `gradioUI` folder instead.

## 2. Create and activate a virtual environment

A virtual environment keeps this app's Python packages separate from other projects.

**Windows PowerShell:**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

**macOS or Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

With the virtual environment activated, run:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 4. Configure your Gemini API key

1. Create or copy an API key in [Google AI Studio](https://aistudio.google.com/apikey).
2. In the project folder, create a file named `.env` (without a second file extension).
3. Add this line, replacing the example value with your key:

   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

Keep your API key private. Do not commit `.env` or paste the key into source code. This project's `.gitignore` excludes `.env`.

## 5. Start the Gradio app

From the project folder, with the virtual environment active, run:

```bash
python gradio_app.py
```

Open the local URL printed in the terminal (usually `http://127.0.0.1:7860`) in your browser. Enter a message and submit it to see Gemini's response. Stop the app with `Ctrl+C` in the terminal.

## Optional: run the terminal chatbot

The project also includes a text-only version that runs in the terminal:

```bash
python simple_chat.py
```

Type `exit` to end the conversation.

## Notes and troubleshooting

- The app currently requests the Gemini model `gemini-3.6-flash`. If the API reports that the model is unavailable, check the model name supported by your Google AI account and update it in `simple_chat.py`.
- If you see an API-key error, make sure `.env` is in the same project folder, the variable is spelled `GOOGLE_API_KEY`, and the key is valid.
- If Python or pip is not recognized, install Python and ensure it is available on your system PATH. On Windows, `py` can be used to create the environment.
- `gradio_app.py` launches with `share=True`. Gradio will create a temporary public URL in addition to the local URL. Anyone with that public link may be able to use the chatbot while it is running, and requests can consume your API quota. Do not share it unless that is intended; remove `share=True` from `iface.launch(...)` to disable the public link.
- Gemini usage may be subject to Google account limits, quotas, or billing settings.
