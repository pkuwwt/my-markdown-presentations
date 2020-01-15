
# Concepts in Neural Network

---

## Validation

### mean Average Precision (mAP)

  * AP is a popular metric in measuring the accuracy of object detectors lke Faster R-CNN, SSD.
  * AP computes the average precision value for recall value over 0 to 1
  * AP is the integration over Precision-Recall curve

$$
AP = \int_0^1 p(r) dr
$$

  * mAP is the average of AP over all categories.

---

#### mAP --- Precision and Recall

  * Precision (`\(P\)`): the percentage of your predictions are correct
  * Recall (`\(R\)`): how good you find all the positives

$$
P = \frac{TP}{TP + FP},\quad
R = \frac{T}{TP + FN},\quad
F1 = 2\cdot\frac{P\cdot R}{P + R}
$$

  * TP = True positive, TN = True negative, FP = False positive, FN = False negative
  * For example, in the testing for cancer

$$
P = \frac{TP}{\text{total positive results}},\quad R = \frac{TP}{\text{total cancer cases}}
$$

---

#### mAP --- IoU

  * IoU (Intersection over Union): the overlap between 2 boundaries
  * We use IoU to measure how much our predicted boundary overlaps with the ground truth (the real object boundary)
  * In some datasets, the IoU threashold is 0.5, to distinguish the true positive and false positive

$$
IoU = \frac{\text{area of overlap}}{\text{area of union}}
$$

---

## References

  * [mAP (mean Average Precision) for Object Detection](https://medium.com/@jonathan_hui/map-mean-average-precision-for-object-detection-45c121a31173)
