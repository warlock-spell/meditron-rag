# Steps:

0. Activate env using `.\.venv\Scripts\activate`
1. Run your docker and run ingest.py
2. Make sure env is activated. Install deepeval: `pip install deepeval`
3. `pip install --upgrade huggingface_hub`. Then run `huggingface-cli login`. Then go to: https://huggingface.co/settings/tokens and then create account, verify email, and then create tokens (write access) and paste it in terminal.
4. Once logged in, go to https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2  and request access.
5. Run `python eval_llm.py` and wait for around 20 mins.