import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from scipy.signal import butter, lfilter, welch
import time



# ========= FUNÇÕES AUXILIARES =========

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut=8, highcut=28, fs=250):
    """Filtro passa-banda entre 8–28 Hz (mu e beta)"""
    b, a = butter_bandpass(lowcut, highcut, fs)
    return lfilter(b, a, data, axis=0)

def selecionar_canais(df):
    """
    Seleciona canais motores: C3 (10), CZ (14) e C4 (15)
    Compatível com colunas numéricas ou texto.
    """
    df.columns = df.columns.map(str)
    canais_desejados = []

    for canal in ['10', '14', '15']:
        if canal in df.columns:
            canais_desejados.append(canal)

    if len(canais_desejados) == 0:
        raise ValueError(f"Canais C3, CZ e C4 não encontrados! Colunas disponíveis: {list(df.columns)}")

    return df[canais_desejados]

def calcular_bandpower(x, fs=250, fmin=8, fmax=28):
    """Estima potência espectral (média de potência entre 8–28 Hz)"""
    f, Pxx = welch(x, fs=fs, nperseg=min(len(x), 256))
    mask = (f >= fmin) & (f <= fmax)
    from scipy.integrate import trapezoid
    return trapezoid(Pxx[mask], f[mask])  # integração melhora robustez

def extrair_features_janelas(df, janela=250, sobreposicao=0.5, scaler=None):
    """
    Retorna features por janela: energia média, desvio padrão e bandpower por canal.
    Adiciona sobreposição de janelas e reuso do scaler.
    """
    df = selecionar_canais(df)
    dados = df.values

    imputer = SimpleImputer(strategy='mean')
    dados = imputer.fit_transform(dados)

    if scaler is None:
        scaler = StandardScaler()
        dados = scaler.fit_transform(dados)
    else:
        dados = scaler.transform(dados)

    dados_filtrados = bandpass_filter(dados)

    passo = int(janela * (1 - sobreposicao))
    janelas = [dados_filtrados[i:i+janela] for i in range(0, max(1, len(dados_filtrados) - janela + 1), passo)]

    features = []
    for j in janelas:
        feat_j = []
        for c in range(j.shape[1]):
            canal = j[:, c]
            feat_j.append(np.mean(canal**2))          # energia média
            feat_j.append(np.std(canal))              # desvio padrão
            feat_j.append(calcular_bandpower(canal))  # bandpower
        features.append(feat_j)

    return np.array(features), scaler

# ========= ARQUIVOS =========
arquivo_esquerda = "C:\\Users\\carlo\\OneDrive\\Área de Trabalho\\recordAlphaBeta-[2025.10.14-17.27.17]Esquerda.csv"
arquivo_direita = "C:\\Users\\carlo\\OneDrive\\Área de Trabalho\\recordAlphaBeta-[2025.10.14-17.24.46]Direita.csv"
arquivo_teste = "C:\\Users\\carlo\\OneDrive\\Área de Trabalho\\recordAlphaBeta-[2025.10.14-17.30.18]DireitaEsquerda.csv"

# ========= LEITURA =========
df_esq = pd.read_csv(arquivo_esquerda)
df_dir = pd.read_csv(arquivo_direita)
df_test = pd.read_csv(arquivo_teste)

# ========= EXTRAÇÃO DE FEATURES =========
feat_esq, scaler = extrair_features_janelas(df_esq)
feat_dir, _ = extrair_features_janelas(df_dir, scaler=scaler)

# ========= BALANCEAMENTO DE CLASSES =========
min_len = min(len(feat_esq), len(feat_dir))
X_train = np.vstack([feat_esq[:min_len], feat_dir[:min_len]])
y_train = np.hstack([np.zeros(min_len), np.ones(min_len)])

# ========= TREINAMENTO =========
clf = LDA()
clf.fit(X_train, y_train)
print("✅ Classificador LDA treinado com sucesso!")

# ========= PREDIÇÃO EM TEMPO REAL =========
janela = 250  # 1 segundo
n_amostras = df_test.shape[0]
passo = int(janela * 0.5)  # 50% de sobreposição

print("\n⏱ Iniciando predição em tempo real...\n")
for i in range(0, n_amostras - janela + 1, passo):
    df_janela = df_test.iloc[i:i+janela]
    feat_janela, _ = extrair_features_janelas(df_janela, janela=janela, scaler=scaler)
    if feat_janela.size == 0:
        continue
    pred = clf.predict(feat_janela)[0]

    if pred == 0:
        print(f"ESQUERDA")
    else:
        print(f"DIREITA")

    time.sleep(0.5)  # simula predição em tempo real
