import json
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
)


def get_metadata(image_url):

    prompt = """
    Describe this clothing item.

    Return ONLY valid JSON.
    Do not include any explanations.

    Format:
    {
    "category": "",
    "subcategory": "",
    "color": "",
    "pattern": "",
    "material": "",
    "ocassion": "",
    "season": "",
    "aesthetic": ""
    }
    """

    try:
        response = client.chat.completions.create(
            model="google/gemma-4-26B-A4B-it:novita",
            messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )

    except Exception as e:
        print(f'Gemma error:{e}')
        return None
                
                    
    text = response.choices[0].message.content

    # remove invalid JSON
    if text.startswith("```json"):
        text = text[7:]

    if text.endswith("```"):
        text = text[:-3]

    text = text.strip()

    metadata = json.loads(text)

    return metadata