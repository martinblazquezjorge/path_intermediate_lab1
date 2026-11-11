"""Clasificador didáctico proporcionado: el alumno solo lo integra.

El objetivo del Lab no es implementar Naive Bayes. Los comentarios permiten
entender su contrato y el flujo general sin exigir la derivación matemática.
"""

import math
import re
from collections import Counter, defaultdict
from typing import Iterable


def tokenize(text: str) -> list[str]:
    """Normaliza texto y conserva tokens alfanuméricos de dos o más caracteres."""
    # Pasar a minúsculas hace equivalentes "Transferencia" y "transferencia".
    return re.findall(r"[a-záéíóúñ0-9]{2,}", text.lower())


class ProvidedNaiveBayesClassifier:
    """Naive Bayes multinomial mínimo, completo y listo para integrar."""

    def __init__(self) -> None:
        # Los contadores resumen documentos y palabras por categoría. El
        # vocabulario global se usa para suavizar palabras no observadas.
        self._documents: Counter[str] = Counter()
        self._tokens: dict[str, Counter[str]] = defaultdict(Counter)
        self._totals: Counter[str] = Counter()
        self._vocabulary: set[str] = set()

    def fit(self, examples: Iterable[tuple[str, str]]) -> "ProvidedNaiveBayesClassifier":
        """Aprende frecuencias de una secuencia de ``(texto, categoría)``."""
        for text, category in examples:
            tokens = tokenize(text)
            self._documents[category] += 1
            self._tokens[category].update(tokens)
            self._totals[category] += len(tokens)
            self._vocabulary.update(tokens)
        if not self._documents:
            raise ValueError("Se necesita al menos un ejemplo de entrenamiento")
        # Devolver ``self`` permite componer ``Provided...().fit(datos)``.
        return self

    def predict(self, text: str) -> tuple[str, float]:
        """Devuelve la categoría con mayor puntuación y una confianza normalizada."""
        if not self._documents:
            raise RuntimeError("El clasificador debe entrenarse antes de predecir")
        token_list = tokenize(text)
        total_docs = sum(self._documents.values())
        vocab_size = max(1, len(self._vocabulary))
        scores: dict[str, float] = {}
        for category, document_count in self._documents.items():
            # Se usan logaritmos para sumar valores pequeños sin perder
            # precisión numérica. ``+1`` aplica suavizado de Laplace.
            score = math.log(document_count / total_docs)
            denominator = self._totals[category] + vocab_size
            for token in token_list:
                score += math.log((self._tokens[category][token] + 1) / denominator)
            scores[category] = score
        best = max(scores, key=scores.get)
        # Restar el máximo antes de ``exp`` evita desbordamientos y permite
        # transformar puntuaciones relativas en una confianza entre 0 y 1.
        maximum = max(scores.values())
        probabilities = {key: math.exp(value - maximum) for key, value in scores.items()}
        confidence = probabilities[best] / sum(probabilities.values())
        return best, round(confidence, 4)
