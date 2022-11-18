create table empresa{
cnpj VARCHAR(20)
ie VARCHAR(20)
razao_social VARCHAR(300)
nome_fantasia VARCHAR(300)
end_logradouro VARCHAR(300)
end_numero INT 
end_bairro VARCHAR(300)
end_cidade VARCHAR(300)
end_estado VARCHAR(300)
end_cep VARCHAR(10)
};

create table funcionario{
cpf VARCHAR(20)
nome VARCHAR(300)
rg VARCHAR(20)
sexo VARCHAR(10)
data_nascimento DATE
end_logradouro VARCHAR (300)
end_numero INT
end_cidade VARCHAR(300) |
end_bairro VARCHAR(300)
end_estado VARCHAR(300)
end_cep VARCHAR(10)
data_admissão DATE
n_carteira_trabalho VARCHAR(45)
};
 

create table cupom_fiscal{
ccf INT
data DATE
hora TIME
valor_total FLOAT
empresa_cnpj VARCHAR(20)
funcionario_caixa_idfuncionario_caixa INT
};


create table item_cupom_fiscal{
cupom_fiscal_ccf INT
produto_idproduto INT
item INT
qtd VARCHAR(45)
valor_item VARCHAR(45)      
};


create  table produto{
idproduto INT
nome VARCHAR(200)
descricao VARCHAR(500)
unidade VARCHAR(45)
preco_unitario FLOAT
};
 

create table funcionario_caixa{
idfuncionario_caixa INT
funcionario_cpf VARCHAR(20)
caixa_idcaixa INT
data_abertura DATE
hora_abertura TIME
valor_abertura DOUBLE
data_fechamento DATE
hora_fechamento TIME
valor_fechamento FLOAT
diferenca DOUBLE
situacao VARCHAR(45)
};


create caixa{
idcaixa INT
descricao VARCHAR(500)
};