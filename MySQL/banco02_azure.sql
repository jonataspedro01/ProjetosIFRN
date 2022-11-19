CREATE DATABASE IF NOT EXISTS banco02_azure;

USE banco02_azure;

create table empresa(
cnpj VARCHAR(20) NOT NULL PRIMARY KEY,
ie VARCHAR(20),
razao_social VARCHAR(300),
nome_fantasia VARCHAR(300),
end_logradouro VARCHAR(300),
end_numero INT,
end_bairro VARCHAR(300),
end_cidade VARCHAR(300),
end_estado VARCHAR(300),
end_cep VARCHAR(10)
);

create table funcionario(
cpf VARCHAR(20) NOT NULL PRIMARY KEY,
nome VARCHAR(300),
rg VARCHAR(20),
sexo VARCHAR(10),
data_nascimento DATE,
end_logradouro VARCHAR (300),
end_numero INT,
end_cidade VARCHAR(300),
end_bairro VARCHAR(300),
end_estado VARCHAR(300),
end_cep VARCHAR(10),
data_admissão DATE,
n_carteira_trabalho VARCHAR(45)
);
 

create table cupom_fiscal(
ccf INT NOT NULL PRIMARY KEY,
data DATE,
hora TIME,
valor_total FLOAT,
empresa_cnpj VARCHAR(20),
FOREIGN KEY (empresa_cnpj) references empresa(cnpj),
funcionario_caixa_idfuncionario_caixa INT,
FOREIGN KEY (funcionario_caixa_idfuncionario_caixa) references funcionario_caixa(idfuncionario_caixa)
);


create table item_cupom_fiscal(
cupom_fiscal_ccf INT,
FOREIGN KEY (cupom_fiscal_ccf) references cupom_fiscal(ccf),
produto_idproduto INT,
FOREIGN KEY (produto_idproduto) references produto(idproduto),
item INT  NOT NULL PRIMARY KEY,
qtd VARCHAR(45),
valor_item VARCHAR(45)      
);


create  table produto(
idproduto INT NOT NULL PRIMARY KEY,
nome VARCHAR(200),
descricao VARCHAR(500),
unidade VARCHAR(45),
preco_unitario FLOAT
);
 

create table funcionario_caixa(
idfuncionario_caixa INT NOT NULL PRIMARY KEY,
funcionario_cpf VARCHAR(20),
FOREIGN KEY (funcionario_cpf) references funcionario(cpf),
caixa_idcaixa INT,
FOREIGN KEY (caixa_idcaixa) references caixa(idcaixa),
data_abertura DATE,
hora_abertura TIME,
valor_abertura DOUBLE,
data_fechamento DATE,
hora_fechamento TIME,
valor_fechamento FLOAT,
diferenca DOUBLE,
situacao VARCHAR(45)
);


create table caixa(
idcaixa INT NOT NULL PRIMARY KEY,
descricao VARCHAR(500)
);

