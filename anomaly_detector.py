#!/usr/bin/env python3
# Anomaly Detector - ibramoha2/ai-cyber-toolkit
# Detection d anomalies reseau avec Isolation Forest
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import argparse, sys

def detect_anomalies(filepath, contamination=0.05):
    print(f'[*] Chargement: {filepath}')
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print('[-] Fichier introuvable'); sys.exit(1)
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    X = df[numeric_cols].fillna(0)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = IsolationForest(contamination=contamination, random_state=42)
    preds = model.fit_predict(X_scaled)
    df['anomaly'] = (preds == -1)
    df['score'] = model.score_samples(X_scaled)
    anomalies = df[df['anomaly']]
    print(f'[+] {len(anomalies)}/{len(df)} anomalies detectees ({len(anomalies)/len(df)*100:.1f}%)')
    out = filepath.replace('.csv', '_anomalies.csv')
    anomalies.to_csv(out, index=False)
    print(f'[+] Resultats: {out}')
    return anomalies

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--contamination', type=float, default=0.05)
    args = ap.parse_args()
    detect_anomalies(args.input, args.contamination)
