# Gender Pay Gap — Privacy Through Homomorphic Encryption

Este repositório contém a implementação do **Step 2** do projecto *“Privacy Through Homomorphic Encryption”* para a unidade curricular **Security and Privacy (MSI 2024/2025)**. O objectivo é cifrar um *dataset* salarial e gerar os artefactos necessários para que um *Data Analyzer* consiga calcular, **sobre os dados cifrados**, a diferença média e o desvio percentual de remuneração entre mulheres e homens, tal como exige a **Diretiva (EU) 2023/970**.

---

## Estrutura do repositório

| Caminho/Ficheiro         | Papel  |
| ------------------------ | ------------------------ |
| `dataset.xlsx`           | *Dataset* (10 398 linhas); colunas: `ID`, `Gender`, `Base Salary/Year ($)` |
| `data_analyzer.py`       | Realiza as operações estatísticas |
| `data_holder.py`         | Encripta o dataset e desencripta os resultados |
| `utils.py`               | Funções auxiliares |
| `README.md`              | Este documento |

---

## Como executar

### 1 — Clonar o repositório

```bash
# clone
https://github.com/lucas03miguel/project_sp.git
cd <repo>
```

### 2 — Gerar os ficheiros cifrados (Step 2)

```bash
python utils.py
```

* **Input** → `dataset.xlsx`
* **Output** → `artifacts/enc_male.tenseal`, `enc_female.tenseal`, `enc_counts.tenseal`, `public_context.tenseal`
* **Tempo de execução** (M1 Pro, 8‑cores): \~2,3 s • **Tamanho total** dos artefactos: 1,8 MB

### 3 — Descifrar um resultado (quando regressar do Step 3)

```bash
python decrypt.py --results artifacts/enc_results.tenseal \
                  --secret_ctx secret_context.tenseal
```

Exemplo de saída:

```
Homens – média: 99 661.3 $
Mulheres – média: 96 654.6 $
Diferença absoluta: 3 006.7 $
Desvio relativo: 3.11 %
```

---

## Parâmetros CKKS adoptados

| Parâmetro             | Valor              | Justificação                                                        |
| --------------------- | ------------------ | ------------------------------------------------------------------- |
| `poly_modulus_degree` | **8192**           | Segurança \~128‑bit e capacidade para vectores ≥ 4096.              |
| `coeff_mod_bit_sizes` | `[60, 40, 40, 60]` | Permite \~3 multiplicações de profundidade com *global scale* 2^40. |
| `global_scale`        | `2**40`            | Compromisso precisão × crescimento do ruído.                        |
| Galois & Relinear     | Gerados            | Necessários para somas rotativas e relinearização.                  |

---

## Descrição do *dataset*

| Coluna                 | Tipo                  |
| ---------------------- | --------------------- |
| `Gender`               | categórico (`F`, `M`) |
| `Base Salary/Year ($)` | float                 |


---

## Conformidade com a Diretiva (EU) 2023/970

* As únicas métricas exigidas são:

  1. **Diferença média absoluta** de remuneração (homens − mulheres).
  2. **Desvio %** relativo ao salário médio feminino.
* O limiar regulamentar é **5 %** → se ultrapassado, inicia‑se *joint pay assessment*.
* Como todos os cálculos são feitos sobre HE‑CKKS, **nenhum salário individual é exposto** em qualquer fase.
