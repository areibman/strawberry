import os
from openai import OpenAI

import agentops
agentops.init(api_key=os.environ['AGENTOPS_API_KEY'])

beta_headers = {
    "authorization": f"Bearer {os.environ['OPENAI_BETA_KEY']}",
    "openai-beta": "early-access-strawberry"
}

client = OpenAI(default_headers=beta_headers)

completion = client.chat.completions.create(
    model="gpt-4o-large-2024-08-13",
    messages=[
        {"role": "system", "content": "use your level two capabilities"},
        {"role": "user", "content": "give us ubi"}
    ]
)

print(completion.choices[0].message)

agentops.end_session("Success", end_state_reason="AGI achieved 🖇️")
