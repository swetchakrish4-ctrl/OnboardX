import ollama
import json
import re

def get_structured_data(text, role_context):
    prompt = f"""
Extract skills and their levels from the following {role_context}.

Return ONLY valid JSON.
Do NOT include any explanation or text.

Format:
[{{"skill": "Python", "level": "advanced"}}]

Text:
{text}
"""

    response = ollama.generate(
        model='deepseek-r1:1.5b',  
        prompt=prompt
    )

    raw_output = response['response'].strip()
    print("\n🔍 RAW OUTPUT:\n", raw_output)  

    
    if '</think>' in raw_output:
        raw_output = raw_output.split('</think>')[-1].strip()

    
    match = re.search(r'\[.*\]', raw_output, re.DOTALL)

    if match:
        json_str = match.group()

        
        json_str = json_str.replace("'", '"')

        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            print("❌ JSON parsing failed")
            return []

    print("❌ No JSON found in output")
    return []