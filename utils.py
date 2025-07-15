# utils.py
import os, re, requests, pandas as pd
from datetime import datetime

ANO         = 2025
LEGISLATURA = 57
CSV_URL = (
    "https://www.camara.leg.br/transparencia/api/download/"
    f"tabelaComparativa.csv?ano={ANO}&legislatura={LEGISLATURA}"
    "&por=deputado"
)
TMP_CSV = "dados_atual.csv"

def fetch_csv() -> str:
    """Baixa CSV para disco (se ainda não existe hoje) e devolve o caminho."""
    if os.path.exists(TMP_CSV):
        mod = datetime.fromtimestamp(os.path.getmtime(TMP_CSV)).date()
        if mod == datetime.today().date():
            return TMP_CSV  # já temos versão de hoje
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.camara.leg.br/transparencia/gastos-parlamentares",
    }
    r = requests.get(CSV_URL, headers=headers, timeout=60)
    r.raise_for_status()
    with open(TMP_CSV, "wb") as f:
        f.write(r.content)
    return TMP_CSV

def _parse_money(v: str) -> float:
    v = str(v).replace("R$", "").replace(" ", "").replace(" ", "")
    if "," in v:
        v = v.replace(".", "").replace(",", ".")
    v = re.sub(r"[^\d.]", "", v)
    return float(v or 0)

def resumo_dataframe() -> pd.DataFrame:
    """Produz DataFrame ordenado de gastos (maior → menor)."""
    path = fetch_csv()
    df = pd.read_csv(path, sep=";", encoding="utf-8", engine="python")
    df.columns = [c.strip().title() for c in df.columns]
    nome_c    = next(c for c in df.columns if "Nome"    in c)
    partido_c = next(c for c in df.columns if "Partido" in c)
    uf_c      = next(c for c in df.columns if c.lower() == "uf")
    valor_c   = next(c for c in df.columns if "Valor"   in c)
    df[valor_c] = df[valor_c].apply(_parse_money)
    df = df.sort_values(valor_c, ascending=False)
    df = df[[nome_c, partido_c, uf_c, valor_c]]
    df.columns = ["nome", "partido", "uf", "valor"]
    return df
