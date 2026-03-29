from pipeline.stage1_extractor import extract_relations
from pipeline.stage2_verifier import verify
from pipeline.stage3_mapper import map_to_target


def run_pipeline(source, target, max_retry=3):
    for attempt in range(max_retry):
        stage1 = extract_relations(source)

        valid, msg = verify(stage1["predicates"])
        if valid:
            break
        else:
            print(f"Retry {attempt}: {msg}")

    stage3 = map_to_target(stage1["predicates"], target)

    return {
        "stage1": stage1,
        "stage3": stage3
    }
