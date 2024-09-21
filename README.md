
---

# Energy Consumption by Continent

Este projeto calcula a porcentagem de consumo de energia elétrica por continente com base em imagens em escala de cinza. As imagens representam diferentes continentes, onde os pixels brancos indicam o consumo de energia elétrica. O cálculo é feito normalizando a área de cada continente e comparando os pixels brancos em relação à área total.

Software feito para a disciplina TEC433 - Formação e Visualização de Imagens Digitais, no curso de Engenharia de Computação - UEFS (Universidade Estadual de Feira de Santana)

## O que o software faz

- Leitura de imagens de diferentes continentes em escala de cinza.
- Contagem de pixels brancos, que representam o consumo de energia elétrica.
- Normalização das áreas de continentes para comparação justa.
- Cálculo da porcentagem de energia consumida por continente.

## Tecnologias Utilizadas

- Python 3
- Pillow (PIL) para manipulação de imagens
- Plotly para visualização de gráficos

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Coloque as imagens dos continentes na pasta `img/`.

3. Execute o script principal para calcular e exibir os resultados:
   ```bash
   python main.py
   ```

## Saída

O programa gera um gráfico de pizza mostrando a porcentagem de consumo de energia elétrica de cada continente com base nos pixels brancos das imagens.

### Saída com os dados utilizados:

![Resultado](https://github.com/ValmirNogFilho/Energy-Consumption-by-Continent/blob/master/results/result.png)

---
