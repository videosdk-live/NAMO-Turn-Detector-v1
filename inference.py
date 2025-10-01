import numpy as np
import onnxruntime as ort
from transformers import AutoTokenizer
from huggingface_hub import hf_hub_download

# --- Configuration Section ---
sentences = [
        "They're often made with oil or sugar.",      # Expected: End of Turn
        "I think the next logical step is to", # Expected: Not End of Turn
        "What are you doing tonight?",          # Expected: End of Turn
        "The Revenue Act of 1862 adopted rates that increased with",         # Expected: Not End of Turn

]
language = None # Set to None for multilingual, or use ISO 639-1 language code (e.g., "en", "pt", "es", etc.)

def get_repo_id(language):
    """
    Returns the appropriate repository ID based on the language code.
    """
    if language is None:
        return "videosdk-live/Namo-Turn-Detector-v1-Multilingual"
    else:
        language_map = dict(ar="Arabic", bn="Bengali", zh="Chinese", da="Danish", nl="Dutch", de="German", en="English", fi="Finnish", fr="French", hi="Hindi", id="Indonesian", it="Italian", ja="Japanese", ko="Korean", mr="Marathi", no="Norwegian", pl="Polish", pt="Portuguese", ru="Russian", es="Spanish", tr="Turkish", uk="Ukrainian", vi="Vietnamese")
        lang_name = language_map.get(language.lower(), language.capitalize())
        return f"videosdk-live/Namo-Turn-Detector-v1-{lang_name}"

class TurnDetector:
    def __init__(self, language=None):
        """
        Initializes the detector by downloading the model and tokenizer
        from the Hugging Face Hub based on the specified language.
        """
        repo_id = get_repo_id(language)
        print(f"Loading model from repo: {repo_id}")
        
        # Download the model and tokenizer from the Hub
        # Authentication is handled automatically if you are logged in
        model_path = hf_hub_download(repo_id=repo_id, filename="model_quant.onnx")
        self.tokenizer = AutoTokenizer.from_pretrained(repo_id)
        
        # Set up the ONNX Runtime inference session
        self.session = ort.InferenceSession(model_path)
        
        # Set max_length based on whether it's multilingual or not
        self.max_length = 8192 if language is None else 512
        print("✅ Model and tokenizer loaded successfully.")

    def predict(self, text: str) -> tuple:
        """
        Predicts if a given text utterance is the end of a turn.
        Returns (predicted_label, confidence) where:
        - predicted_label: 0 for "Not End of Turn", 1 for "End of Turn"
        - confidence: confidence score between 0 and 1
        """
        # Tokenize the input text
        inputs = self.tokenizer(
            text,
            truncation=True,
            max_length=self.max_length,
            return_tensors="np"
        )
        
        # Prepare the feed dictionary for the ONNX model
        feed_dict = {
            "input_ids": inputs["input_ids"],
            "attention_mask": inputs["attention_mask"]
        }
        
        # Run inference
        outputs = self.session.run(None, feed_dict)
        logits = outputs[0]

        probabilities = self._softmax(logits[0])
        predicted_label = np.argmax(probabilities)
        confidence = float(np.max(probabilities))

        return predicted_label, confidence

    def _softmax(self, x, axis=None):
        if axis is None:
            axis = -1
        exp_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
        return exp_x / np.sum(exp_x, axis=axis, keepdims=True)

# --- Example Usage ---
if __name__ == "__main__":
    detector = TurnDetector(language=language)
    
    for sentence in sentences:
        predicted_label, confidence = detector.predict(sentence)
        result = "End of Turn" if predicted_label == 1 else "Not End of Turn"
        print(f"'{sentence}' -> {result} (confidence: {confidence:.3f})")
        print("-" * 50)
