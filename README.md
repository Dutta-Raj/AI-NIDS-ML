%%writefile README.md
# 🚨 AI-Powered Network Intrusion Detection System (NIDS)

This Streamlit app predicts whether a network connection is normal or an attack using a trained ML model on the NSL-KDD dataset.

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

---

### 🔹 4. Push to GitHub

> ✅ You can do this either locally (with Git) or via the [GitHub Web UI](https://github.com/new) for simplicity.

#### ✅ Option 1: Upload via GitHub Web

1. Go to: [https://github.com/new](https://github.com/new)
2. Create a new repo (e.g., `nids-streamlit-app`)
3. Click **“Upload files”**
4. Upload:
   - `app.py`
   - `model.pkl`
   - `requirements.txt`
   - `README.md`
5. Click **“Commit changes”**

---

#### ✅ Option 2: Use Git Locally (if you're on your PC)

If working from your PC:

```bash
git init
git remote add origin https://github.com/YOUR_USERNAME/nids-streamlit-app.git
git add .
git commit -m "Initial commit"
git push -u origin master
