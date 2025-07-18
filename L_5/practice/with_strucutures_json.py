from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_theams": {
      "title": "Key Theams",
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key theams discussed in the review in a list"
    },
    "summary": {
      "title": "Summary",
      "type": "string",
      "description": "A Brief summary about the review"
    },
    "sentiment": {
      "title": "Sentiment",
      "type": "string",
      "description": "sentiment about the review Possitive, negative or nutral"
    },
    "pros": {
      "title": "Pros",
      "type": ["array","null"],
      "items": {
        "type": "string"
      },
      "description": "write show all the rows inside the list"
    },
    "cons": {
      "title": "Cons",
      "type": ["array","null"],
      "items": {
        "type": "string"
      },
      "description": "write show all the rows inside the list"
    },
    "name": {
      "title": "Name",
      "type": ["array","null"],
      "description": "write name of the reviewer"
    }
  },
  "required": [
    "key_theams",
    "summary",
    "sentiment"
  ]
}
 
    
structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""Overall Score: 7.8/10

The smartphone market is saturated, and finding a device that genuinely stands out without breaking the bank can be a challenge. Enter the Zenith X10, a new contender in the competitive mid-range segment that aims to offer a premium experience without the premium price tag. After a week of extensive use, I can confidently say the X10 mostly delivers on that promise, with a few caveats.

Design & Display (8/10):
Right out of the box, the Zenith X10 impresses with its sleek, minimalist design. The frosted glass back feels surprisingly premium, resisting fingerprints better than many glossy counterparts. The 6.7-inch OLED display is vibrant, with excellent contrast and decent brightness for outdoor visibility. Scrolling is smooth thanks to the 90Hz refresh rate, making everyday interactions feel fluid. Bezels are thin, though the teardrop notch for the front camera is a bit dated compared to punch-hole designs.

Performance (7.5/10):
Powered by the "OctaCore 5000" chipset (a custom-branded mid-range processor), the X10 handles daily tasks with ease. App launching is snappy, and multitasking rarely causes a hiccup. Gaming on titles like Asphalt 9 and Genshin Impact is surprisingly good, though you'll need to dial down graphics settings for the smoothest experience. There were occasional stutters during prolonged heavy use, but nothing that significantly impacted the overall experience. The 8GB of RAM helps keep things running smoothly.

Camera (7/10):
The triple-camera setup on the back features a 50MP main sensor, an 8MP ultrawide, and a 2MP macro lens. The main camera is the star of the show, capturing detailed and color-accurate photos in good lighting. Dynamic range is respectable, and the AI scene recognition does a decent job of optimizing shots. Low-light performance is acceptable for the price point, but don't expect flagship-level results; noise becomes noticeable. The ultrawide is a nice addition, though quality drops off, and the macro lens, as usual, is more of a gimmick. The 16MP front camera takes sharp selfies suitable for social media.

Battery Life & Charging (8.5/10):
This is where the Zenith X10 truly shines. The massive 5000mAh battery easily lasts a full day of heavy use, often stretching into a second day with moderate usage. Streaming videos, Browse social media, and making calls barely put a dent in its endurance. The included 33W fast charger is a welcome bonus, topping up the battery from 0 to 50% in under 30 minutes. Wireless charging is, predictably, absent at this price.

Software (7/10):
The X10 runs on Android 15 with Zenith's custom "ZenUI 5.0" overlay. The UI is clean and relatively bloatware-free, with some useful customization options. However, software updates are a bit of an unknown. Zenith promises two major Android updates and three years of security patches, which is decent but not industry-leading. There were a few minor pre-installed apps that couldn't be uninstalled, which was a slight annoyance.

Conclusion:
The Zenith X10 is a compelling option for anyone looking for a well-rounded smartphone without spending flagship money. Its strong battery life, vibrant display, and solid main camera make it a joy to use for everyday tasks and even some light gaming. While the processor isn't top-tier and the ultrawide camera could be better, these are minor compromises for the price. If you prioritize endurance and a good visual experience, the Zenith X10 is definitely worth considering.""")

print(result)