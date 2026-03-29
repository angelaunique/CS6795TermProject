def compute_ras(predicted, ground_truth):
    pred_set = set(p["name"] for p in predicted)
    gt_set = set(ground_truth)

    if not gt_set:
        return 0

    overlap = len(pred_set & gt_set)
    return overlap / len(gt_set)
