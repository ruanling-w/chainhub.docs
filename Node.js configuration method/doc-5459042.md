# Node.js Basic Dialogue

```bash
npm i openai
```

```js
const fs = require("fs");
const OpenAI = require("openai");

const openai = new OpenAI({
  apiKey: "sk-xxxxxxxx",
  baseURL: "https://api.wlai.vip/v1",
});

async function transcribeAudio() {
  try {
    const transcription = await openai.audio.transcriptions.create({
      file: fs.createReadStream("a-product-demo-167264.mp3"), //Replace with your audio file path
      model: "whisper-1",
    });

    console.log("Transcription result:", transcription.text);
  } catch (error) {
    console.error("Transcription error:", error);
  }
}

transcribeAudio();
```
