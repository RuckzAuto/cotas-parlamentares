# app.py
from flask import Flask, render_template, jsonify, send_file
from fpdf import FPDF
from utils import resumo_dataframe
import io

app = Flask(__name__)

def safe(txt):  # garante latin‑1
    return str(txt).encode("latin-1", "replace").decode("latin-1")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/gastos")
def api_gastos():
    df = resumo_dataframe()
    return jsonify(df.to_dict(orient="records"))

@app.route("/download")
def download_pdf():
    df = resumo_dataframe()

    pdf = FPDF("L", "mm", "A4")
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 12, safe("Resumo de Gasto de Cota Parlamentar - 2025"),
             ln=1, align="C")
    pdf.ln(4)

    # cabeçalho
    pdf.set_font("Arial", "B", 12)
    headers = [("Nome", 90), ("Partido", 35), ("UF", 22), ("Valor (R$)", 45)]
    for text, w in headers:
        pdf.cell(w, 10, safe(text), border=1, align="C"); pdf.cell(3, 10)
    pdf.ln()

    # linhas
    pdf.set_font("Arial", "", 11)
    for _, r in df.iterrows():
        pdf.cell(90, 12, safe(r["nome"][:40]), border=1); pdf.cell(3, 12)
        pdf.cell(35, 12, safe(r["partido"]),    border=1, align="C"); pdf.cell(3, 12)
        pdf.cell(22, 12, safe(r["uf"]),         border=1, align="C"); pdf.cell(3, 12)
        pdf.cell(45, 12, safe(f"{r['valor']:,.2f}"), border=1, align="R")
        pdf.ln()

    # ------- CORREÇÃO AQUI -------
    pdf_bytes = pdf.output(dest="S").encode("latin-1")   # gera bytes
    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype="application/pdf",
        download_name="resumo_gastos_2025.pdf",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
