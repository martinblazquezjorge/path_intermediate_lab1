"""Interfaz de consola que conecta todos los componentes del Lab 1."""

import argparse

from .classifier import ProvidedNaiveBayesClassifier
from .repositories import IncidentCsvRepository, TrainingCsvRepository
from .service import IncidentClassificationService, JsonPredictionWriter, PriorityPolicy


def build_parser() -> argparse.ArgumentParser:
    """Define argumentos reproducibles y sus rutas predeterminadas."""
    parser = argparse.ArgumentParser(description="Clasifica incidencias FRC sintéticas")
    parser.add_argument("--training", default="data/training.csv")
    parser.add_argument("--input", default="data/incidents.csv")
    parser.add_argument("--output", default="output/predictions.json")
    return parser


def main() -> None:
    """Carga datos, entrena, clasifica y escribe el resultado final."""
    args = build_parser().parse_args()
    # La composición ocurre en el borde de la aplicación: cada clase conserva
    # una responsabilidad y el CLI decide cómo conectarlas.
    classifier = ProvidedNaiveBayesClassifier().fit(TrainingCsvRepository().load(args.training))
    service = IncidentClassificationService(classifier, PriorityPolicy())
    predictions = service.classify_all(IncidentCsvRepository().load(args.input))
    JsonPredictionWriter().write(predictions, args.output)
    print(f"Procesadas {len(predictions)} incidencias sintéticas -> {args.output}")


if __name__ == "__main__":
    main()
