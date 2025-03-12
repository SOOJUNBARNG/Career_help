import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

DEFAULT_SYSTEM_PROMPT = "あなたは誠実で優秀なITエンジニアです。プログラミングを追加・訂正して回答してください。"
text = """
looker studio data to google bucket automatically? how do I do that?

1. Create a Google Cloud Storage bucket where you want to store your data.

2. Create a new Google Cloud Function or Google App Engine application.

3. In your function or application, you need to use the Google Cloud Storage and Google Analytics APIs to fetch data from Looker Studio and upload it to your bucket.

4. Schedule your function or application to run at regular intervals using Cloud Scheduler.

tell me more about google analytics api that fetch data from looker studio?

https://lookerstudio.google.com/u/0/reporting/62467673-1ec2-4b90-9fe8-105ca378eabb/page/p_an45grm7nd

i want to download data fromt this automatically 


"""

model_name = "SakanaAI/Llama-3-8B-Instruct-Coding-Expert"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
)
model.eval()

messages = [
    {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
    {"role": "user", "content": text},
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
token_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_new_tokens=1200,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )
output = tokenizer.decode(output_ids.tolist()[0][token_ids.size(1) :], skip_special_tokens=True)
print(output)
