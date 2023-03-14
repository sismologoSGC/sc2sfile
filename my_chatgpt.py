#!/home/adagudelo/first_env/bin/python
import openai


#set api_key
openai.api_key = "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"

#create instance of openai
gpt = openai
#print(openai._dict_.keys)
#generate text
conv = []
previous_conversation = ""
for e in range(15):

    msg = input("pregunta: ")
    if len(conv) == 0:
        response = gpt.Completion.create(model="text-davinci-003", prompt=msg, max_tokens=3000, temperature=0)
        #response = gpt.Completion.create(model="text-davinci-003", prompt=msg, max_tokens=1000, temperature=0, top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n"])
        resp = str(response["choices"][0]["text"])
        print(response["choices"][0]["text"])

    else:
        response = gpt.Completion.create(model="text-davinci-003", prompt=f"{previous_conversation}{msg}", max_tokens=3000, temperature=0)
        #response = gpt.Completion.create(model="text-davinci-003", prompt=f"{previous_conversation}{msg}", max_tokens=1000, temperature=0, top_p=1, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n"])
        resp = str(response["choices"][0]["text"])
        print(response["choices"][0]["text"])

    previous_conversation += msg+"\n"+resp+"\n"
    conv.append(msg)
    conv.append(resp)
