import torch



device = 'cuda' if torch.cuda.is_available() else 'cpu'


class Dolly:
    
    def __init__(self):
        
        # self.model_name = 'databricks/dolly-v2-12b'
        self.model_name = 'databricks/dolly-v2-3b'
        self.prepare_model()
        
        return
    
    
    def prepare_model(self):

        # Load model directly
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name).to(device)
        
        print('Negativity: ', self.dolly_call('I hate you'))

        return
    
    
    def _dolly_call(self, prompt):
        return self.generate_text(prompt)[0]['generated_text']
    
    
    def dolly_call(self, prompt):
        
        tokenized = self.tokenizer(prompt, return_tensors='pt')
        tokens = self.model.generate(
            **tokenized.to(device),
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        return self.tokenizer.decode(tokens)


