"""Configuracion comun del experimento de clasificacion de pitting."""

SEED = 42
IMAGE_SIZE = 224
BATCH_SIZE = 32
LEARNING_RATE = 2e-5
EPOCHS = 2

DATASET_REPOSITORY = "2OBe/Ball_Screw_Drive_Classification"

MODEL_IDS = {
    "ResNet-50": "microsoft/resnet-50",
    "ConvNeXt-Tiny": "facebook/convnext-tiny-224",
    "ViT-Base": "google/vit-base-patch16-224",
}

ID_TO_LABEL = {0: "OK", 1: "Defecto"}
LABEL_TO_ID = {"OK": 0, "Defecto": 1}

