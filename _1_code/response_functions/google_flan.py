class Google_Flan_T5:
    
    def __init__(self):
        
        self.prepare_model()
        
        return
    
    
    def _prepare_model(self):
        
        from transformers import T5Tokenizer, T5ForConditionalGeneration

        self.tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xxl")
        self.model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xxl", device_map="auto")

        input_text = "translate English to German: How old are you?"
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

        outputs = self.model.generate(input_ids)
        print(self.tokenizer.decode(outputs[0]))

        return
    
    
    def prepare_model(self):
        
        import torch
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-xxl")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-xxl")

        input_text = "Explain to me the difference between nuclear fission and fusion."
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids#.to("cuda")

        outputs = self.model.generate(input_ids, max_new_tokens=100)
        print(self.tokenizer.decode(outputs[0]))

        return
    
    
    def flan_call(self, prompt):
        
        return_string =  self.tokenizer.decode(
            self.model.generate(
                self.tokenizer(prompt, return_tensors='pt').input_ids,
                max_new_tokens=100
            )[0]
        )
        
        return return_string

