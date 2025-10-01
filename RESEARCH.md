# Namo-Turn-Detection-v1  
**Semantic End-of-Utterance Prediction for Real-Time Voice Agents**

## Abstract
Turn-taking — deciding exactly when a speaker has finished — underpins natural conversation. Current voice agents mostly rely on **Voice Activity Detection (VAD)** or fixed silence thresholds, causing premature cut-offs or latency.  
We present **NAMO Turn Detector v1 (NAMO-v1)**, an **open-source**, **ONNX-optimized** model that predicts **End-of-Utterance (EOU)** using semantics rather than silence alone. NAMO achieves **<19 ms inference (specialized)**, **<29 ms (multilingual)** and **up to 97.3 % accuracy**, making it the first practical semantic replacement for VAD in real-time systems.

---

## 1. Problem Statement

In interactive speech, the system must estimate the **EOU boundary** — the point where the user’s current thought is complete.

Let an utterance be a token sequence:

$$
U = (w_1, w_2, \dots, w_T)
$$

EOU detection is a binary classification task:

$$
f_\theta(U_{1:t}) =
\begin{cases}
1 & \text{if the sequence up to $t$ forms a complete thought (EOU)}\\
0 & \text{otherwise}
\end{cases}
$$

Traditional methods approximate $f_\theta$ with acoustic silence or punctuation cues.

### Limitations
- **Silence-based VAD** — fast but brittle: hesitations or noise cause false positives.  
- **ASR endpointing** — better than raw energy but language-dependent; enumerations and fillers (“uh”, “and…”) confuse pause-based rules.

This creates a **latency vs. interruption trade-off**:

$$
\text{Response Latency} \uparrow \quad \Longleftrightarrow \quad \text{False Cut-offs} \downarrow
$$

---

## 2. NAMO Approach

### Semantic End-of-Utterance Classifier
NAMO replaces silence heuristics with **contextual embeddings**.  
Given ASR text stream $X_{1:t}$:

$$
h_t = \mathrm{Encoder}_\theta(X_{1:t})
$$

$$
p_t = \sigma(W h_t + b)
$$

where $p_t = \Pr(\mathrm{EOU}\mid X_{1:t})$.  
If $p_t > \tau$ (threshold), the system triggers turn transfer.

- **Encoder:** mmBERT (multilingual) or DistilBERT (single-language)  
- **Optimization:** ONNX + INT8 quantization for sub-30 ms inference

---

## 3. Model Characteristics

| Feature       | Description                                             |
|---------------|---------------------------------------------------------|
| **Latency**   | <19 ms (single-language), <29 ms (multilingual)          |
| **Accuracy**  | Up to 97.3 % (Turkish/Korean), ~90 % avg multilingual    |
| **Size**      | 135 MB (specialized), 295 MB (multilingual)              |
| **Coverage**  | 23+ languages with one multilingual model                |
| **Integration** | Plug-and-play with STT → NAMO → LLM → TTS pipeline    |

---

## 4. Performance Evaluation

### Latency & Throughput
Quantization improves inference:

$$
\mathrm{Latency}_{\text{multi}}: 61\,\mathrm{ms} \rightarrow 28\,\mathrm{ms}
$$

$$
\mathrm{Latency}_{\text{single}}: 38\,\mathrm{ms} \rightarrow 14.9\,\mathrm{ms}
$$

Throughput:  
$$35.6 \rightarrow 66.8\ \text{tokens/sec (≈2× increase)}$$

Accuracy drop: **<0.2 %** after quantization.

### Multilingual Accuracy (selected)

| Lang | Accuracy |
|------|----------|
| Turkish | 97.3 % |
| Korean | 96.8 % |
| Japanese | 94.3 % |
| Hindi | 93.9 % |
| German | 94.2 % |
*(Average multilingual: 90.25 % across 23 languages)*

---

## 5. Integration Example

```python
from videosdk_agents import NamoTurnDetectorV1, pre_download_namo_turn_v1_model

# Download model (one-time)
pre_download_namo_turn_v1_model()              # multilingual
# pre_download_namo_turn_v1_model(language="en") # single language

turn_detector = NamoTurnDetectorV1()

from videosdk_agents import CascadingPipeline
pipeline = CascadingPipeline(
    stt=your_stt_service,
    llm=your_llm_service,
    tts=your_tts_service,
    turn_detector=turn_detector
)

```
## 6. Training & Testing

Each model includes Colab notebooks for training and testing:

- **Training Notebooks**: Fine-tune models on your own datasets
- **Testing Notebooks**: Evaluate model performance on custom data

Visit individual model pages for notebook links:
- [Multilingual Training Notebook](https://colab.research.google.com/drive/1WEVVAzu1WHiucPRabnyPiWWc-OYvBMNj)
- [Specialised Model Training Notebook](https://colab.research.google.com/drive/1DqSUYfcya0r2iAEZB9fS4mfrennubduV)
- [Testing Notebook](https://colab.research.google.com/drive/19ZOlNoHS2WLX2V4r5r492tsCUnYLXnQR)

## License

This project is licensed under the **Apache License 2.0**.
## Citation

If you use Namo-v1 in your research or project, please cite:

```bibtex
@software{namo2025,
  title = {Namo Turn Detector v1: Semantic Turn Detection for Conversational AI},
  author = {VideoSDK Team},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/collections/videosdk-live/namo-turn-detector-v1-68d52c0564d2164e9d17ca97}
}
```
---



