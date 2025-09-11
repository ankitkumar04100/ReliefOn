# 🌍 ReliefOn
**AI-Powered Platform for Instant Disaster Relief**


> 🚑 Turning scattered cries for help into actionable, real-time relief coordination.
> Because when disaster strikes, **Relief should always be ON.**

---

## Demo  
Check out our demo here: [ReliefOn Demo on Blackbox.ai](https://www.blackbox.ai/share/97dd597b-ad6a-4ed1-bc0c-1aaa9f13034a?fullScreen=true)  

## Table of Contents
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [Built With](#built-with)
- [Features](#features)
- [Accomplishments](#accomplishments)
- [What We Learned](#what-we-learned)
- [What's Next](#whats-next)
- [Contributing](#contributing)
- [License](#license)
- [Quote](#quote)
- [Architecture](#architecture)


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

## Features
- Multi-channel input (Mobile, SMS, WhatsApp)
- AI categorization & urgency scoring
- Real-time map clustering & heatmaps
- Volunteer dashboard with claim/resolution
- Notifications when requests are fulfilled
- Security: anonymized & auto-expiring data
- Accessibility: multi-language, offline, voice input

---

## Accomplishments
- AI-powered request categorization
- Real-time disaster map & clustering
- Volunteer dashboard with live updates
- Scalable backend tested with 100k+ requests
- NGO feedback integrated

---

## What We Learned
- Simplicity & speed save lives
- Multi-channel & offline support is crucial
- Hackathons are about impact, not just code

---

## What's Next
- Offline-first native apps
- Blockchain-based aid tracking
- NGO/government partnerships
- Predictive AI for disaster anticipation
- Satellite integration for live updates

---

## Contributing
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## License
This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.

---

## Quote
*"Disasters are inevitable. Chaos doesn’t have to be. ReliefOn brings order, speed, and hope."*

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



