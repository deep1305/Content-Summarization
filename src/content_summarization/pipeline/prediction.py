from content_summarization.config.configuration import ConfigurationManager
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(self.device)


    
    def predict(self,text):
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        print("Dialogue:")
        print(text)

        inputs = self.tokenizer(
            text,
            max_length=1024,
            truncation=True,
            return_tensors="pt",
        )
        inputs = {key: value.to(self.device) for key, value in inputs.items()}
        summary_ids = self.model.generate(**inputs, **gen_kwargs)
        output = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        print("\nModel Summary:")
        print(output)

        return output