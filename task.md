# AssemblyAI Universal-Streaming Integration Work Package

## 1. API Key Verification and Environment Variable
- [x] Ensure there is a valid AssemblyAI API key (`ASSEMBLYAI_API_KEY`) in the `.env` file.
- [x] Verify that the key is correct and has Universal-Streaming access.

## 2. Backend Settings and Restart
- [x] Check that the environment variable is correctly read in the backend code.
- [x] Restart the backend.

## 3. Token Endpoint Test
- [x] Test getting a token by making a request to the `POST /api/assemblyai-token` endpoint.
- [x] If you get an error, examine the backend logs and fix it.

## 4. Frontend Microphone Integration
- [x] Add the necessary JavaScript code for microphone access in the frontend.
- [x] Start audio recording when the microphone button is clicked.
- [x] Collect audio data in real-time and store it in a buffer.

## 5. WebSocket Connection Setup
- [x] Add necessary libraries for WebSocket connection in the frontend.
- [x] Get a token from the backend when the microphone is active.
- [x] Establish AssemblyAI WebSocket connection with the received token.
- [x] Check connection status and handle error situations.

## 6. Real-time Audio Transmission
- [ ] Send microphone data to AssemblyAI via WebSocket.
- [ ] Set the audio format correctly (16kHz, PCM, mono).
- [ ] Send audio data in chunks.

## 7. STT (Speech-to-Text) Processing
- [ ] Receive real-time transcript data from AssemblyAI.
- [ ] Display transcript data in the frontend.
- [ ] Get the final transcript when speech ends.

## 8. Qloo+LLM Integration
- [ ] Send the final transcript to the `/chat` endpoint in the backend.
- [ ] Get relevant data with the Qloo API.
- [ ] Process the transcript with LLM and generate a response.
- [ ] Send the response back to the frontend and display it.

## 9. User Experience (UX) Improvements
- [ ] Visually show microphone active/inactive states.
- [ ] Add a "listening" animation during speech.
- [ ] Update transcript in real-time while it's being written.
- [ ] Inform the user in error situations.

## 10. Error Handling and Log Tracking
- [ ] Catch and handle WebSocket connection errors.
- [ ] Check microphone access errors.
- [ ] Examine backend logs and add error messages to task.md.
- [ ] Update solution steps if necessary.

## 11. Testing and Optimization
- [ ] Test the entire flow end-to-end.
- [ ] Test in different browsers.
- [ ] Optimize audio quality and latency times.
- [ ] Track performance metrics.

## 12. Security and Performance
- [ ] Manage WebSocket connections securely.
- [ ] Check and renew token expiration.
- [ ] Optimize memory usage.
- [ ] Add rate limiting (if necessary).
