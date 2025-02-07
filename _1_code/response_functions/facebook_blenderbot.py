device = 'cpu'


class Facebook_BlenderBot:
    
    def __init__(self):
        
        self.prepare_model()
        
        return
    
    
    def prepare_model(self):
        
        import torch
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

        self.tokenizer = AutoTokenizer.from_pretrained(
            "facebook/blenderbot-400M-distill", max_length=128
        )
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            "facebook/blenderbot-400M-distill", max_position_embeddings=128
        ).to(device)
        
        input_text = "Explain to me the difference between nuclear fission and fusion."
        input_ids = self.tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True).input_ids.to(device)

        outputs = self.model.generate(input_ids, max_new_tokens=500)
        print(self.tokenizer.decode(outputs[0]))
        
        self.model.resize_token_embeddings(len(self.tokenizer))
        
        return
    
    
    def bot_call(self, prompt):
        
        tokenized_input = self.tokenizer(
            prompt, return_tensors='pt', max_length=128, truncation=True
        ).input_ids.to(device)
        
        return_string =  self.tokenizer.decode(
            self.model.generate(tokenized_input, max_new_tokens=500)[0]
        )
        
        return return_string

