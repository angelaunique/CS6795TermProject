from pipeline.pipeline import run_pipeline
from utils.scorer import compute_ras

source = "Immune system protects body"
target = "Firewall protects network"

ground_truth = ["DETECTS", "BLOCKS", "CAUSES"]

result = run_pipeline(source, target)

ras = compute_ras(result["stage3"]["predicates"], ground_truth)

print("RAS:", ras)
print(result)
