import numpy as np
import torch



class Dialog_GPT:
    
    def __init__(self):
        
        self.prepare_model()
        
        return
    
    
    def prepare_model(self):
        
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium").to('cuda')
        
        input_text = "Explain to me the difference between nuclear fission and fusion."
        
        print('\nDialogpt: {}'.format(self.dialogpt_call(input_text)))

        return
    
    
    def _deprecated_dialogpt_call_left(self, prompt):
        
        tokenized_input = self.tokenizer.encode(
            self.tokenizer.eos_token + prompt, return_tensors='pt', max_length=1024, truncation=True
        ).to('cuda')
        
        model_output = self.model.generate(
            tokenized_input, max_length=1024, pad_token_id=self.tokenizer.eos_token_id
        )
        
        return_string = self.tokenizer.decode(model_output[:, tokenized_input.shape[-1]:][0], skip_special_tokens=True)
        
        return return_string
    
    
    def dialogpt_call(self, prompt):
        
        tokenized = self.tokenizer(prompt, return_tensors='pt')
        tokens = self.model.generate(
            **tokenized.to('cuda'),
            pad_token_id=self.tokenizer.eos_token_id
        )[0, tokenized.input_ids.shape[-1]:]
        
        return self.tokenizer.decode(tokens)

