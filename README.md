# Medical RAG-using-Meditron-7B-LLM
Medical RAG QA App using Meditron 7B LLM, Qdrant Vector Database, and PubMedBERT Embedding Model.

# Steps:

1. Download the code zip, unzip it, in the same folder create the venv, using command `pyenv versions` then `pyenv local 3.10.0`. Make sure that `3.10.0` is installed before setting it to local. Then create venv, using command `python -m venv .venv`. Activate the .venv by command, `.\.venv\Scripts\activate`. Now (.venv) should be visible on your terminal.

2. Make sure that venv is activated properly, then run `pip install -r requirements.txt`. This will install all the dependencies.

3. Once this is done, now download the LLM file from this link [model](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q5_K_M.gguf?download=true). Once the model is downloaded, place it in same folder.

4. Download Docker, install it, it is very large and computationally intensive software, make sure to close all extra things, no background apps should be running while downloading and using docker. Restart after installing docker.

5. Once docker is installed, make sure to open it using administrative rights. How to do it? go to start, search docker, in the right you will see options, select run as administrative. Click once, then wait, do not click again. Very first time it may take upto 20 mins, after that time will be anywhere between 5 to 8 mins. Before any of the next steps it is crucial to start the docker engine.

6. Once docker desktop application is up and running, minimize it, and open the terminal with admin rights, run command `docker images`. Initially, it will be empty.

7. Then run `docker pull qdrant/qdrant` in the terminal that you opened in step 6. Once installed, run `docker images` again and make sure that you can see the Qdrant image there. This will be the Vector DB that we will be using.

8. Now let's start the image, from the same terminal run `docker run -p 6333:6333 qdrant/qdrant`. After running this, you will see QDRANT printed on your terminal.

9. Open your browser, and go to `localhost:6333/dashboard`

10. In your VS code terminal, run `python ingest.py`. It will take some time, in this process we are storing data from pdf to our vector db. Go back to browser and refresh, and you will see a new collection is created.

11. Then in the VS Code terminal, run `python retriever.py`. You will see the similar vectors to our Question which is hardcoded in the retriever.py file. Open the file to see the question, and in the terminal you will see the similar vectors from our pdf.

12. Then finally, run `uvicorn main:app`.


