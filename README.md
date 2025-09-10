# 🌍 ReliefOn
**AI-Powered Platform for Instant Disaster Relief**


> 🚑 Turning scattered cries for help into actionable, real-time relief coordination.
> Because when disaster strikes, **Relief should always be ON.**

---

## Table of Contents
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [Built With](#built-with)
- [Architecture](#architecture)
- [Installation & Setup](#installation--setup)
- [Features](#features)
- [Accomplishments](#accomplishments)
- [What We Learned](#what-we-learned)
- [What's Next](#whats-next)
- [Contributing](#contributing)
- [License](#license)
- [Quote](#quote)
- [Badges](#badges)

---

## Inspiration
Millions are affected by floods, earthquakes, wildfires, and other disasters every year. Victims send desperate messages across social media, SMS, and word-of-mouth, but lack of coordination delays aid. ReliefOn was created to **bridge the gap** between victims, volunteers, NGOs, and governments using AI, real-time mapping, and multi-channel communication.

---

## What It Does
- 📲 Victims submit requests via mobile app, SMS, or WhatsApp
- 🤖 AI engine categorizes needs (food, water, shelter, medicine) and assigns urgency scores
- 🗺️ Requests appear on a real-time interactive disaster map, clustered to prevent duplication
- 👩‍🚒 Volunteers and NGOs use a dashboard to claim and resolve tasks
- 🔔 Victims are notified when their requests are fulfilled
- 🌍 Supports low-connectivity areas, offline mode, multi-language, and voice input

---

## Built With
**React.js, TailwindCSS, Node.js, Express.js, MongoDB Atlas, Redis, GCP, Docker, Kubernetes, Leaflet.js, Mapbox API, Twilio API, HuggingFace Transformers, spaCy, Python, TensorFlow Lite, REST APIs, WebSockets, GitHub, Figma**

---

## Architecture

```mermaid
graph TD
  A[Victim: Mobile/SMS/WhatsApp] -->|Request| B[API Gateway: Node.js/Express]
  B --> C[AI Engine: Python + HuggingFace + spaCy]
  C --> D[Database: MongoDB Atlas + Redis]
  D --> E[Relief Map: React.js + Leaflet.js + Mapbox]
  D --> F[Volunteer Dashboard]
  E --> G[NGOs & Volunteers]
  F --> G
  G -->|Task Updates| D

## Installation & Setup

# Clone repository
git clone https://github.com/ankitkumar04100/reliefon.git
cd reliefon

# Backend
cd backend
npm install
npm run dev

# Frontend
cd frontend
npm install
npm start

# AI Engine
cd ai-engine
pip install -r requirements.txt

