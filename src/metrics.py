"""Funciones de evaluacion utilizadas en la comparacion de modelos."""

from sklearn.metrics import accuracy_score, precision_recall_fscore_support


def calculate_binary_metrics(y_true, y_pred):
    """Calcula accuracy, precision, recall y F1 para la clase con pitting."""
    precision, recall, f1_score, _ = precision_recall_fscore_support(
        y_true,
        y_pred,
        average="binary",
        pos_label=1,
        zero_division=0,
    )

    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score,
    }
