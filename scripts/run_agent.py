#!/usr/bin/env python3
"""Runner real del agente SE.

Lee un caso de cliente desde un archivo de texto (prompts/casos/*.md), lo corre contra
prompts/system_prompt.md vía la API de Anthropic, y guarda la salida completa —tal como
salió— en corridas/raw/, junto con los tokens y el costo reales de esa corrida.

Es el conector/herramienta real del sistema: reemplaza el copy-paste manual entre chat y
archivos por lectura y escritura de archivos reales, y es la fuente de los datos de tokens
usados en ANALISIS_ECONOMICO.md.

Uso:
    python scripts/run_agent.py prompts/casos/solicitud_001_acme.md
    python scripts/run_agent.py prompts/casos/solicitud_002_synnex.md --model claude-haiku-4-5

Requiere la librería `anthropic` (ver scripts/requirements.txt) y la variable de entorno
ANTHROPIC_API_KEY (o credenciales equivalentes resueltas por el SDK).
"""
import argparse
import datetime
import pathlib

import anthropic

ROOT = pathlib.Path(__file__).resolve().parent.parent
SYSTEM_PROMPT_PATH = ROOT / "prompts" / "system_prompt.md"
RAW_DIR = ROOT / "corridas" / "raw"

# Precios oficiales de la API de Anthropic (USD por millón de tokens), primera parte.
PRICING_USD_PER_MTOK = {
    "claude-haiku-4-5": {"input": 1.00, "output": 5.00},
    "claude-sonnet-5": {"input": 2.00, "output": 10.00},
}


def run(input_file: pathlib.Path, model: str) -> pathlib.Path:
    system_prompt = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")
    user_input = input_file.read_text(encoding="utf-8")

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_input}],
    )

    output_text = "".join(
        block.text for block in response.content if block.type == "text"
    )

    price = PRICING_USD_PER_MTOK[model]
    cost_usd = (
        response.usage.input_tokens * price["input"]
        + response.usage.output_tokens * price["output"]
    ) / 1_000_000

    now = datetime.datetime.now()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / f"{input_file.stem}_{model}_{now:%Y%m%dT%H%M%S}.md"

    header = (
        "<!--\n"
        f"Caso: {input_file.name}\n"
        f"Modelo: {model}\n"
        f"Fecha: {now.isoformat(timespec='seconds')}\n"
        f"Tokens de entrada: {response.usage.input_tokens}\n"
        f"Tokens de salida: {response.usage.output_tokens}\n"
        f"Costo estimado de esta corrida (USD): {cost_usd:.4f}\n"
        "-->\n\n"
    )
    out_path.write_text(header + output_text, encoding="utf-8")

    print(f"Output guardado en {out_path}")
    print(
        f"Tokens in/out: {response.usage.input_tokens}/{response.usage.output_tokens} "
        f"— costo estimado: USD {cost_usd:.4f}"
    )
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Corre el agente SE contra un caso de cliente real y guarda el output crudo."
    )
    parser.add_argument(
        "input_file", type=pathlib.Path, help="Archivo de texto con la solicitud del cliente"
    )
    parser.add_argument(
        "--model", default="claude-sonnet-5", choices=sorted(PRICING_USD_PER_MTOK)
    )
    args = parser.parse_args()
    run(args.input_file, args.model)


if __name__ == "__main__":
    main()
