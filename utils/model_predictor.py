<<<<<<< HEAD
import tensorflow as tf
import pickle
import numpy as np

class PhishingPredictor:
    def __init__(self, model_path, tokenizer_paths, max_lengths):
        self.model = tf.keras.models.load_model(model_path)
        self.subject_tokenizer = self._load_tokenizer(tokenizer_paths['subject'])
        self.body_tokenizer = self._load_tokenizer(tokenizer_paths['body'])
        self.max_subject_len = max_lengths['subject']
        self.max_body_len = max_lengths['body']
    
    def _load_tokenizer(self, path):
        with open(path, 'rb') as f:
            return pickle.load(f)
    
    def _preprocess_text(self, text, tokenizer, max_len):
        seq = tokenizer.texts_to_sequences([text])
        return tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=max_len)
    
    def predict(self, subject, body):
        subject_padded = self._preprocess_text(subject, self.subject_tokenizer, self.max_subject_len)
        body_padded = self._preprocess_text(body, self.body_tokenizer, self.max_body_len)
=======
import tensorflow as tf
import pickle
import numpy as np

class PhishingPredictor:
    def __init__(self, model_path, tokenizer_paths, max_lengths):
        self.model = tf.keras.models.load_model(model_path)
        self.subject_tokenizer = self._load_tokenizer(tokenizer_paths['subject'])
        self.body_tokenizer = self._load_tokenizer(tokenizer_paths['body'])
        self.max_subject_len = max_lengths['subject']
        self.max_body_len = max_lengths['body']
    
    def _load_tokenizer(self, path):
        with open(path, 'rb') as f:
            return pickle.load(f)
    
    def _preprocess_text(self, text, tokenizer, max_len):
        seq = tokenizer.texts_to_sequences([text])
        return tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=max_len)
    
    def predict(self, subject, body):
        subject_padded = self._preprocess_text(subject, self.subject_tokenizer, self.max_subject_len)
        body_padded = self._preprocess_text(body, self.body_tokenizer, self.max_body_len)
>>>>>>> e61dca5c (Update app.py)
        return self.model.predict([subject_padded, body_padded])[0][0]