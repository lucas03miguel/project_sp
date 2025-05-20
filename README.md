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

### 2 — Gerar as chaves

```bash
python utils.py
```

### 3 — Encriptar o dataset e desencriptar os resultados

```bash
python data_holder.py
```

Inicialmente, vai dar erro por nao existir nenhum ficheiro `statistics`.
Terá que correr então o próximo ficheiro

```bash
python data_analyzer.py
```

E depois voltar a correr o `data_analyzer.py`

```bash
python data_holder.py
```

---

## Parâmetros CKKS adoptados

| Parâmetro             | Valor              |
| --------------------- | ------------------ |
| `poly_modulus_degree` | **16384**          |
| `coeff_mod_bit_sizes` | `[60, 30, 30, 30, 30, 30, 30, 60]` |
| `global_scale`        | `2**30`            |
| Galois & Relinear     | Gerados            |

---

## Descrição do *dataset*

| Coluna                 | Tipo                  |
| ---------------------- | --------------------- |
| `Gender`               | categórico (`F`, `M`) |
| `Base Salary/Year ($)` | float                 |
