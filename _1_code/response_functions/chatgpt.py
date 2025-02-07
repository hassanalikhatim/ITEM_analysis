import openai
import backoff



class ChatGPT:
    
    def __init__(self):
        
        # OpenAI may update how to use this api key.
        # Updated instructions to generate and use api key at https://platform.openai.com/docs/api-reference/introduction
        api_key = '<your own api key>'
        
        self.client = openai.OpenAI(api_key=api_key)
        
        return
    
    
    @backoff.on_exception(backoff.expo, openai.RateLimitError)
    def chatgpt_call(self, prompt):
        
        messages = [ 
            {"role": "system", "content": "You are an intelligent assistant who solves task."},
            {"role": "user", "content": prompt}
        ]
        
        chat = self.client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages
        )
        
        reply = chat.choices[0].message.content
        # print(f"ChatGPT: {reply}")
        
        # We don't want to remember the answers to previous questions.
        # messages.append({"role": "assistant", "content": reply})
        
        return reply
    
    
    def test(self):

        while True:
        
            message = input("User : ")
        
            if message:
                self.messages.append(
                    {"role": "user", "content": message},
                )
                chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=messages
                )
        
            reply = chat.choices[0].message.content
            print(f"ChatGPT: {reply}")
        
            messages.append({"role": "assistant", "content": reply})
            
        return