# **GPT Genie 🧞‍♂️**  
*A Python package for free interaction with ChatGPT using an access token, featuring tools and methods to simplify ChatGPT usage.*

## **🚀 Features**  
✅ Interact with ChatGPT for free using an access token  
✅ Easy-to-use API for sending and receiving messages  
✅ Session management for persistent conversations  
✅ Configurable logging and history settings  

---

## **📦 Installation**  

```bash
pip install -e .
```
Or, if you prefer a **requirements file**, add this to `requirements.txt` and install:  

```bash
requests
```
```bash
pip install -r requirements.txt
```

---

## **🛠️ Usage**  

### **1️⃣ Import and Initialize ChatGPT**  
```python
from gpt_genie import initialize_chatgpt

chat = initialize_chatgpt(access_token="your_access_token")
```

### **2️⃣ Send a Message**
```python
response = chat.send_prompt("Hello, how are you?")
print("ChatGPT Response:", response)
```

---

## **⚙️ Configuration**  
You can configure logging and conversation history while initializing:

```python
chat = initialize_chatgpt(
    access_token="your_access_token",
    history_and_training_enabled=True,
    logging=True
)
```

---

## **🔗 How to Get an Access Token?**  
1. Go to [ChatGPT](https://chat.openai.com) and log in  
2. Open DevTools (`F12` or `Right-click → Inspect`)  
3. Navigate to **Application > Cookies**  
4. Copy the value of `__Secure-next-auth.session-token`  

⚠️ **Warning:** Do not share your access token publicly.

---

## **📜 License**  
This project is licensed under the **MIT License**.  

---

## **💡 Contributing**  
Contributions are welcome! Feel free to:  
- Submit issues  
- Open pull requests  
- Suggest new features  

---

## **📞 Support**  
For any issues or questions, reach out via GitHub issues or discussions.