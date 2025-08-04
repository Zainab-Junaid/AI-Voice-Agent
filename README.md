AI Voice Agent
This is a voice-based customer service agent for a small restaurant. It handles incoming phone calls using Twilio and responds to users with real-time voice using Deepgram and OpenAI. The agent can take orders, track existing orders, and answer questions about the menu.
Features
•	Receives calls through Twilio
•	Transcribes speech using Deepgram
•	Understands user intent using OpenAI
•	Responds in natural voice using Deepgram TTS
•	Handles menu questions, order placement, and order tracking
Tech Used
•	Twilio – for handling calls
•	Deepgram – for speech-to-text and text-to-speech
•	OpenAI GPT – for smart conversation logic
•	Python – main programming language
•	uv + pyproject.toml – for managing dependencies
Files
•	main.py: Core logic for handling calls
•	functions.py: Functions like get_menu, place_order, etc.
•	config.json: Prompt, function setup, and other config
•	.env: Stores API keys (not included in repo)
•	pyproject.toml: Project dependencies
•	uv.lock: Dependency lock file
How It Works
When a user calls the Twilio number, the agent listens, understands what the caller says, and responds naturally. It can place orders or look up existing ones, and everything runs in real time using Deepgram and OpenAI.

