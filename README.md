# Namo Turn Detector v1

<div align="center">

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![ONNX](https://img.shields.io/badge/ONNX-Optimized-brightgreen)](https://onnx.ai/)
[![Languages](https://img.shields.io/badge/Languages-23-orange)](https://huggingface.co/collections/videosdk-live/namo-turn-detector-v1-68d52c0564d2164e9d17ca97)
[![Model](https://img.shields.io/badge/Multilingual_Model-Hugging_Face-yellow)](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Multilingual)

**High-performance, semantic turn detection for conversational AI**

</div>

---

Namo-v1 is a collection of open-source turn detection models that solve one of the most challenging problems in conversational AI: **knowing when a user has finished speaking**. Namo uses advanced Natural Language Understanding to analyze semantic context, creating more natural conversations with reduced interruptions and latency.

**Namo's Solution:** Uses Natural Language Understanding to analyze the semantic meaning and context of speech, distinguishing between:
- ✅ **Complete utterances** (user is done speaking)
- 🔄 **Incomplete utterances** (user will continue speaking)

## 🚀 Key Features

- **Semantic Understanding**: Analyzes meaning and context, not just silence
- **Ultra-Fast Inference**: <19ms for specialized models, <29ms for multilingual
- **Lightweight**: ~135MB (specialized) / ~295MB (multilingual)
- **High Accuracy**: Up to 97.3% for specialized models, 90.25% average for multilingual
- **Production-Ready**: ONNX-optimized for real-time, enterprise-grade applications
- **Easy Integration**: Standalone usage or plug-and-play with VideoSDK Agents SDK


## Available Models

Namo offers both **specialized single-language models** and a **unified multilingual model**:

### Multilingual Model (Recommended)
- **Model**: [Namo-Turn-Detector-v1-Multilingual](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Multilingual)
- **Base**: mmBERT
- **Languages**: All 23 supported languages
- **Inference**: <29ms
- **Size**: ~295MB
- **Average Accuracy**: 90.25%


#### 📊 Performance Benchmarks for Multilingual Model

Evaluated on **25,000+ diverse utterances** across all supported languages.

| Language        | Accuracy | Precision | Recall | F1 Score | Samples |
| --------------- | -------- | --------- | ------ | -------- | ------- |
| 🇹🇷 Turkish    | 97.31%   | 0.9611    | 0.9853 | 0.9730   | 966     |
| 🇰🇷 Korean     | 96.85%   | 0.9541    | 0.9842 | 0.9690   | 890     |
| 🇯🇵 Japanese   | 94.36%   | 0.9099    | 0.9857 | 0.9463   | 834     |
| 🇩🇪 German     | 94.25%   | 0.9135    | 0.9772 | 0.9443   | 1,322   |
| 🇮🇳 Hindi      | 93.98%   | 0.9276    | 0.9603 | 0.9436   | 1,295   |
| 🇳🇱 Dutch      | 92.79%   | 0.8959    | 0.9738 | 0.9332   | 1,401   |
| 🇳🇴 Norwegian  | 91.65%   | 0.8717    | 0.9801 | 0.9227   | 1,976   |
| 🇨🇳 Chinese    | 91.64%   | 0.8859    | 0.9608 | 0.9219   | 945     |
| 🇫🇮 Finnish    | 91.58%   | 0.8746    | 0.9702 | 0.9199   | 1,010   |
| 🇬🇧 English    | 90.86%   | 0.8507    | 0.9801 | 0.9108   | 2,845   |
| 🇵🇱 Polish     | 90.68%   | 0.8619    | 0.9568 | 0.9069   | 976     |
| 🇮🇩 Indonesian | 90.22%   | 0.8514    | 0.9707 | 0.9071   | 971     |
| 🇮🇹 Italian    | 90.15%   | 0.8562    | 0.9640 | 0.9069   | 782     |
| 🇩🇰 Danish     | 89.73%   | 0.8517    | 0.9644 | 0.9045   | 779     |
| 🇵🇹 Portuguese | 89.56%   | 0.8410    | 0.9676 | 0.8999   | 1,398   |
| 🇪🇸 Spanish    | 88.88%   | 0.8304    | 0.9681 | 0.8940   | 1,295   |
| 🇮🇳 Marathi    | 88.50%   | 0.8762    | 0.9008 | 0.8883   | 774     |
| 🇺🇦 Ukrainian  | 87.94%   | 0.8164    | 0.9587 | 0.8819   | 929     |
| 🇷🇺 Russian    | 87.48%   | 0.8318    | 0.9547 | 0.8890   | 1,470   |
| 🇻🇳 Vietnamese | 86.45%   | 0.8135    | 0.9439 | 0.8738   | 1,004   |
| 🇸🇦 Arabic     | 84.90%   | 0.7965    | 0.9439 | 0.8639   | 947     |
| 🇧🇩 Bengali    | 79.40%   | 0.7874    | 0.7939 | 0.7907   | 1,000   |

**Average Accuracy: 90.25%** across all languages

> For detailed performance metrics of individual specialized models, visit their respective model pages.


### Specialized Single-Language Models

- **Architecture**: DistilBERT-based
- **Inference**: <19ms
- **Size**: ~135MB each

| Language        | Model Link                                                                                  | Accuracy |
| --------------- | ------------------------------------------------------------------------------------------- | -------- |
| 🇰🇷 Korean     | [Namo-v1-Korean](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Korean)         | 97.3%    |
| 🇹🇷 Turkish    | [Namo-v1-Turkish](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Turkish)       | 96.8%    |
| 🇯🇵 Japanese   | [Namo-v1-Japanese](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Japanese)     | 93.5%    |
| 🇮🇳 Hindi      | [Namo-v1-Hindi](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Hindi)           | 93.1%    |
| 🇩🇪 German     | [Namo-v1-German](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-German)         | 91.9%    |
| 🇬🇧 English    | [Namo-v1-English](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-English)       | 91.5%    |
| 🇳🇱 Dutch      | [Namo-v1-Dutch](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Dutch)           | 90.0%    |
| 🇮🇳 Marathi    | [Namo-v1-Marathi](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Marathi)       | 89.7%    |
| 🇨🇳 Chinese    | [Namo-v1-Chinese](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Chinese)       | 88.8%    |
| 🇵🇱 Polish     | [Namo-v1-Polish](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Polish)         | 87.8%    |
| 🇳🇴 Norwegian  | [Namo-v1-Norwegian](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Norwegian)   | 87.3%    |
| 🇮🇩 Indonesian | [Namo-v1-Indonesian](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Indonesian) | 87.1%    |
| 🇵🇹 Portuguese | [Namo-v1-Portuguese](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Portuguese) | 86.9%    |
| 🇮🇹 Italian    | [Namo-v1-Italian](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Italian)       | 86.8%    |
| 🇪🇸 Spanish    | [Namo-v1-Spanish](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Spanish)       | 86.7%    |
| 🇩🇰 Danish     | [Namo-v1-Danish](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Danish)         | 86.5%    |
| 🇻🇳 Vietnamese | [Namo-v1-Vietnamese](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Vietnamese) | 86.2%    |
| 🇫🇷 French     | [Namo-v1-French](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-French)         | 85.0%    |
| 🇫🇮 Finnish    | [Namo-v1-Finnish](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Finnish)       | 84.8%    |
| 🇷🇺 Russian    | [Namo-v1-Russian](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Russian)       | 84.1%    |
| 🇺🇦 Ukrainian  | [Namo-v1-Ukrainian](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Ukrainian)   | 82.4%    |
| 🇸🇦 Arabic     | [Namo-v1-Arabic](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Arabic)         | 79.7%    |
| 🇧🇩 Bengali    | [Namo-v1-Bengali](https://huggingface.co/videosdk-live/Namo-Turn-Detector-v1-Bengali)       | 79.2%    |


> 📊 **View Full Collection**: [All Namo Models on HuggingFace](https://huggingface.co/collections/videosdk-live/namo-turn-detector-v1-68d52c0564d2164e9d17ca97)


### ONNX Quantization Benefits

All Namo models are optimized using ONNX quantization, which reduces model complexity while maintaining high accuracy:

- **2.19x relative speedup** compared to unquantized models
- **Inference time**: Reduced from 61.3ms → 28.0ms
- **Throughput**: More than doubled
- **Accuracy Impact**: Negligible
- **Latency**: Virtually zero perceptible delay in conversations

### 🚀 Try It Yourself!

We’ve provided an [inference script](inference.py) to help you quickly test these models. Just plug it in and start experimenting!

### Integration with VideoSDK Agents

For seamless integration into your voice agent pipeline:

```python
from videosdk_agents import NamoTurnDetectorV1, pre_download_namo_turn_v1_model

# Download model files (one-time setup)
# For multilingual (default):
pre_download_namo_turn_v1_model()

# For specific language:
# pre_download_namo_turn_v1_model(language="en")

# Initialize turn detector
turn_detector = NamoTurnDetectorV1()  # Multilingual
# turn_detector = NamoTurnDetectorV1(language="en")  # English-specific

# Add to your agent pipeline
from videosdk_agents import CascadingPipeline

pipeline = CascadingPipeline(
    stt=your_stt_service,
    llm=your_llm_service,
    tts=your_tts_service,
    turn_detector=turn_detector  # Namo integration
)
```

> 📚 **Complete Integration Guide**: [VideoSDK Agents Documentation](https://docs.videosdk.live/ai_agents/plugins/namo-turn-detector)


## 🔧 Training & Testing

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

<div align="center">

**Made with ❤️ by the VideoSDK Team**

[![VideoSDK](https://img.shields.io/badge/VideoSDK-Live-blue)](https://videosdk.live)

</div>