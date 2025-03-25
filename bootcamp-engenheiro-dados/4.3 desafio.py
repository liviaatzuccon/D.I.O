
INSERT INTO Relatorio (nome_cliente, nome_vendedor, valor_venda)  
SELECT   
    c.nome_cliente AS nome_cliente,  
    v.nome AS nome_vendedor,  
    SUM(vd.valor_venda) AS valor_venda  
FROM   
    Vendas vd  
JOIN   
    Clientes c ON vd.cliente_id = c.cliente_id  
LEFT JOIN   
    Vendedores v ON c.vendedor_id = v.vendedor_id  
GROUP BY   
    c.nome_cliente, v.nome;  
    