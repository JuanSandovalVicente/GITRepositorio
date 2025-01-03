import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')  # Descargar recursos necesarios para la tokenización

texto = "Este es un ejemplo. ¡Hola mundo! ¿Cómo estás?"

# Tokenización de palabras
tokens_palabras = word_tokenize(texto)
print("Tokens de palabras:", tokens_palabras)

# Tokenización de oraciones
tokens_oraciones = sent_tokenize(texto)
print("Tokens de oraciones:", tokens_oraciones)