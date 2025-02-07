device = 'cpu'


class Facebook_BlenderBot_3B:
    
    def __init__(self):
        
        self.prepare_model()
        
        return
    
    
    def prepare_model(self):
        
        import torch
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

        self.tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-3B", max_length=1024)
        self.model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-3B", max_position_embeddings=1024).to(device)
        
        input_text = "Explain to me the difference between nuclear fission and fusion."
        input_ids = self.tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True).input_ids.to(device)

        outputs = self.model.generate(input_ids, max_new_tokens=500)
        print(self.tokenizer.decode(outputs[0]))
        
        self.model.resize_token_embeddings(len(self.tokenizer))
        
        return
    
    
    def bot_3b_call(self, prompt):
        
        print(self.model.config.max_position_embeddings)
        
        tokenized_input = self.tokenizer(
            prompt, return_tensors='pt', max_length=1024, truncation=True
        ).input_ids.to(device)
        
        return_string =  self.tokenizer.decode(
            self.model.generate(tokenized_input, max_new_tokens=500)[0]
        )
        
        return return_string

