# 🗣️ Talking Photo Generator

Turn a still photo into a talking video by typing text.  
The system generates speech from text, syncs it to lip movements, and outputs a video of the photo “speaking.”

---

## 🚀 Features

* Upload a **photo** + enter **text** in the web UI
* Text is converted into **speech** (using gTTS)
* Speech + photo are processed by **Wav2Lip** (AI model for lip-sync)
* A **talking video** is generated and auto-downloaded
* **Dockerized** → no setup headache (just `docker compose up`)
* Works on **CPU** (runs anywhere), auto-uses **GPU if available** (much faster)

---

## 🛠️ Tech Stack

* **[FastAPI](https://fastapi.tiangolo.com/)** → backend API (upload handling, orchestration)
* **[Uvicorn](https://www.uvicorn.org/)** + **Gunicorn** → ASGI server for FastAPI
* **[Docker](https://www.docker.com/)** + **docker-compose** → containerized deployment
* **[PyTorch](https://pytorch.org/)** → AI deep learning library powering Wav2Lip
* **[Wav2Lip](https://github.com/Rudrabha/Wav2Lip)** → lip-sync model that animates the photo
* **[gTTS](https://pypi.org/project/gTTS/)** → converts text into speech
* **[MoviePy](https://zulko.github.io/moviepy/)** → merges final audio + video into mp4
* **Frontend**: simple **HTML + JS** page with progress bar + auto-download

---

## ⚙️ How It Works (Pipeline)

1. User uploads a **face photo** + enters text.
2. The **backend** (FastAPI) saves the photo + text.
3. Text → **speech** using Google Text-to-Speech (gTTS).
4. Photo + audio → fed into **Wav2Lip model**.
5. Wav2Lip animates the lips of the still image.
6. Output is a **realistic video** of the photo speaking the text.
7. The frontend shows a preview and provides auto-download.

---

## 📦 Setup (Client Instructions)

### 1. Install Docker

* [Download Docker Desktop](https://www.docker.com/products/docker-desktop) (Windows/Mac)
* [Docker Engine](https://docs.docker.com/engine/install/) (Linux)
* Make sure Docker is running.

---

### 2. Download Model Weights

The app needs pretrained model files:

- `wav2lip.pth`
- `s3fd.pth`

👉 Download from the official [Wav2Lip repo](https://github.com/Rudrabha/Wav2Lip) and place them into:

