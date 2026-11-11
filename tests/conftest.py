"""Fixtures compartidas por las pruebas del Lab 1."""

from pathlib import Path

import pytest

from frc_incidents.classifier import ProvidedNaiveBayesClassifier
from frc_incidents.repositories import TrainingCsvRepository


@pytest.fixture
def classifier() -> ProvidedNaiveBayesClassifier:
    """Entrega un clasificador entrenado y nuevo para cada prueba que lo pida."""
    training = Path(__file__).parents[1] / "data" / "training.csv"
    return ProvidedNaiveBayesClassifier().fit(TrainingCsvRepository().load(training))
