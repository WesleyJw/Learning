# Machine Learning Validation Techniques

Como avaliar se um modelo estatístico ou de machine learning foi bem ajustado ou treinado para um problema de negócio proposto? 

Gosto de considerar estas duas abordagens de forma distinta, principalmente pelo fato de que para respondermos esta pergunta em comum, estas abordagens possuem formas diferentes. 

Alguns especialistas afirmão que é possível avaliar a qualidade do ajuste de um modelo de regressão sem recorrer aos pressupostos da análise de regressão, seja ela, linear ou não linear, simples ou múltipla, generalizado ou não. Lembrando que, este caso só é possível quando o modelador tem o interesse apenas em avalair a qualidade do valor predito, para uma análise inferencial a análise dos pressupostos sempre será recomandada. Apesar da possibilidade é sempre recomendado fazer a análise dos resíduos, isto trás confiança para a equação gerada, bem como a interpretabilidade.

Considerando a abordagem não paramétrica dos algoritmos de Machine Learning uma avaliação teórica da qualidade de ajuste não é possível. Pois não existem certas suposições (pressupostos) atreladas a uma distribuição teórica de probabilidade, o que garante a consistência dos testes estatísticos que avaliam essa qualidade. O que não permite uma anaĺise inferencial (apesar de já existirem alguns esforços nessa tentativa) como no caso da regressão. Se teoricamente (com base em pressuposições estatísticas) não é possível avaliar qualidade de ajsute de um algoritmo treinado, como é possivel garantir que um algoritmo de ML aprendeu de fato?

## Holdout

Em algoritmos de Machine Learning a melhor forma de estimar o erro 