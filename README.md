# AI Cyber Toolkit

> Machine Learning applique a la cybersecurite — detection d anomalies, automatisation SOC.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python)
![ML](https://img.shields.io/badge/ML-scikit--learn-F7931E?style=flat-square)
![Author](https://img.shields.io/badge/Author-ibramoha2-CC0000?style=flat-square)

## Modules

| Module | Description |
|--------|-------------|
| `anomaly_detector.py` | Detection d anomalies reseau avec Isolation Forest |
| `log_classifier.py` | Classification de logs (normal / suspect / critique) |
| `alert_correlator.py` | Correlation d alertes SIEM pour reduire les faux positifs |

## Installation
```bash
git clone https://github.com/ibramoha2/ai-cyber-toolkit
cd ai-cyber-toolkit
pip install -r requirements.txt
```

## Usage
```bash
python anomaly_detector.py --input logs.csv
python log_classifier.py --file /var/log/syslog
```

**Auteur :** [@ibramoha2](https://github.com/ibramoha2) | Niger