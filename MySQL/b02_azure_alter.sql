create table empresa(
cnpj VARCHAR(20) NOT NULL PRIMARY KEY,
ie VARCHAR(20) NOT NULL,
razao_social VARCHAR(300) NOT NULL,
nome_fantasia VARCHAR(300) NOT NULL,
end_logradouro VARCHAR(300) NOT NULL,
end_numero INT NOT NULL,
end_bairro VARCHAR(300) NOT NULL,
end_cidade VARCHAR(300) NOT NULL,
end_estado VARCHAR(300) NOT NULL,
end_cep VARCHAR(10) NOT NULL
);

create table funcionario(
cpf VARCHAR(20) NOT NULL PRIMARY KEY,
nome VARCHAR(300) NOT NULL,
rg VARCHAR(20) NOT NULL,
sexo VARCHAR(10) NOT NULL,
data_nascimento DATE NOT NULL,
end_logradouro VARCHAR (300) NOT NULL,
end_numero INT NOT NULL,
end_cidade VARCHAR(300) NOT NULL,
end_bairro VARCHAR(300) NOT NULL,
end_estado VARCHAR(300) NOT NULL,
end_cep VARCHAR(10) NOT NULL,
data_admissão DATE NOT NULL,
n_carteira_trabalho VARCHAR(45) NOT NULL
);

create table cupom_fiscal(
ccf INT NOT NULL PRIMARY KEY,
data DATE NOT NULL,
hora TIME NOT NULL,
valor_total FLOAT NOT NULL,
fk_empresa_cnpj VARCHAR(20) NOT NULL,
FOREIGN KEY (fk_empresa_cnpj) REFERENCES empresa(cnpj),
fk_funcionario_caixa_idfuncionario_caixa INT,
FOREIGN KEY (fk_funcionario_caixa_idfuncionario_caixa) REFERENCES funcionario_caixa(idfuncionario_caixa)
);

create table item_cupom_fiscal(
fk_cupom_fiscal_ccf INT NOT NULL,
FOREIGN KEY (fk_cupom_fiscal_ccf) references cupom_fiscal(ccf),
fk_produto_idproduto INT NOT NULL,
FOREIGN KEY (fk_produto_idproduto) references produto(idproduto),
item INT  NOT NULL PRIMARY KEY,
qtd VARCHAR(45) NOT NULL,
valor_item VARCHAR(45) NOT NULL     
);

create  table produto(
idproduto INT NOT NULL PRIMARY KEY,
nome VARCHAR(200) NOT NULL,
descricao VARCHAR(500) NOT NULL,
unidade VARCHAR(45) NOT NULL,
preco_unitario FLOAT NOT NULL
);

create table funcionario_caixa(
idfuncionario_caixa INT NOT NULL PRIMARY KEY,
fk_funcionario_cpf VARCHAR(20) NOT NULL,
FOREIGN KEY (fk_funcionario_cpf) references funcionario(cpf),
fk_caixa_idcaixa INT NOT NULL,
FOREIGN KEY (fk_caixa_idcaixa) references caixa(idcaixa),
data_abertura DATE NOT NULL,
hora_abertura TIME NOT NULL,
valor_abertura FLOAT,
data_fechamento DATE NOT NULL,
hora_fechamento TIME NOT NULL,
valor_fechamento FLOAT NOT NULL,
diferenca FLOAT NOT NULL,
situacao VARCHAR(45) NOT NULL
);

create table caixa(
idcaixa INT NOT NULL PRIMARY KEY,
descricao VARCHAR(500) NOT NULL
);
