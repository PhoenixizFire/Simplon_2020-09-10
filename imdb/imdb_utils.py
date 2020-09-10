import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
nltk.download('stopwords')


def preprocess(content):
    """
    Nettoyage d'un texte
    Entrées:
        content: chaîne de caractères
    Sortie:
        content: chaîne de caractères nettoyée
    """

    return content


def tokenize(content):
    """
    Segmentation d'une chaîne de caractère
    Les mots les plus fréquents dans la langue (stopwords) sont retirés
    Racinisation des mots
    Entrées:
        content: chaîne de caractères
    Sortie:
        content : liste segmentée de mots
    """

    return content


def extract_vocabulary(documents):
    """
    Entrées:
        documents: liste de documents sous la forme de listes segmentées de mots
    Sortie:
        vocabulary : set de la totalité des mots du corpus
    """
    vocabulary = set()

    return vocabulary


def create_bow(document):
    """
    Crée un sac de mots à partir d'une liste de mots
    Entrées:
        document: liste segmentée de mots
    Sortie:
        bow: Counter (sous classe de dictionnaire) du type {mot:fréquence}
    """
    bow = Counter()
    
    return bow


def create_word2idx(vocabulary):
    """
    Fonction pour accélerer la création de la matrice vectorisée des documents
    Entrées:
        vocabulary : liste de la totalité des mots du corpus
    Sortie:
        dictionnaire qui a un mot associe son index dans vocabulary {word: index}
    """
    word2idx = {}

    return word2idx
