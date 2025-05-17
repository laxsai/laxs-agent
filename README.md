
# 🤖 LAXS Agent

LAXS Agent is a simple, open-source AI tool powered by $LAXS on Solana. It helps users interact with AI through a lightweight Flask API. No hype — just clean and useful code backed by the community.

---

## 🔧 Features

- OpenAI-powered AI assistant  
- One endpoint: `/ask`  
- Lightweight Flask app  
- Easy to run locally or on a VPS  
- Built to support the $LAXS ecosystem  

---

## 💰 What’s $LAXS?

$LAXS is a meme token on Solana that stands for real utility — not fluff. We build open tools like this to give our token purpose, visibility, and real world use.

---

## 🌍 Links

- Linktr: [https://linktr.ee/laxs_ai](https://linktr.ee/laxs_ai)  
  

---

## 🚀 Getting Started


## 🛠️ Installation

Follow these instructions to get LAXS Agent up and running on your local machine.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/laxsai/laxs-agent.git
   cd laxs-agent
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Copy the example environment variables file:
     ```bash
     cp .env.example .env
     ```
   - Open the `.env` file and add your OpenAI API key:
     ```bash
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Run the Flask app:**
   ```bash
   python web.py
   ```

Once the app is running, it will listen on `http://localhost:5000`.

---

## 💬 Example Usage

After running the agent, send a request like this to the `/ask` endpoint:

```bash
curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"message": "Tell me about Solana"}'
```

**Response:**

```json
{
  "reply": "Solana is a high-performance blockchain built for speed and low fees."
}
```

## 🧰 Requirements

- **Python 3.x** – The programming language used to build the agent.
- **Flask** – Lightweight web framework for handling API requests.
- **OpenAI GPT API** – Powers the AI responses.
- **Solana Public API** – For blockchain interactions.
- **Requests** – Makes HTTP requests to APIs.
- **dotenv** – Manages environment variables securely.

## 🔓 License

MIT License — free to use, modify, distribute, fork, and contribute.

---

Built by the $LAXS community. No fluff. Just code.
