IF OBJECT_ID('biblioteca', 's') IS NULL
BEGIN
    CREATE DATABASE biblioteca;
END

USE biblioteca;
-- biblioteca.dbo.autor definition

-- Drop table

-- DROP TABLE biblioteca.dbo.autor;
IF OBJECT_ID('biblioteca.dbo.autor', 'U') IS NULL
BEGIN
    CREATE TABLE autor (
        id_pessoa char(10) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
        nome nvarchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
        dtNasce date DEFAULT NULL NULL,
        contacto varchar(MAX) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT NULL NULL,
        CONSTRAINT pk_autor PRIMARY KEY (id_pessoa)
    );
    ALTER TABLE biblioteca.dbo.autor WITH NOCHECK ADD CONSTRAINT ch_dtNasc CHECK (([dtNasce]<getdate()));
END


-- biblioteca.dbo.editora definition

-- Drop table

-- DROP TABLE biblioteca.dbo.editora;
if OBJECT_ID('biblioteca.dbo.editora', 'U') IS NULL
BEGIN
    CREATE TABLE editora (
        NIPC char(9) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
        nome nvarchar(25) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
        contacto varchar(MAX) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT NULL NULL,
        morada varchar(50) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT NULL NULL,
        CONSTRAINT pk_editora PRIMARY KEY (NIPC)
    );
END



-- biblioteca.dbo.livro definition

-- Drop table

-- DROP TABLE biblioteca.dbo.livro;
if OBJECT_ID('biblioteca.dbo.livro', 'U') IS NULL
BEGIN    
    CREATE TABLE livro (
        ISBN char(14) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
        titulo nvarchar(40) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
        idioma varchar(5) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT NULL NULL,
        tema varchar(MAX) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT NULL NULL,
        tipo varchar(MAX) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT NULL NULL,
        editora char(9) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
        dtPub decimal(4,0) DEFAULT NULL NULL,
        original char(14) COLLATE SQL_Latin1_General_CP1_CI_AS DEFAULT NULL NULL,
        CONSTRAINT pk_livro PRIMARY KEY (ISBN),
        CONSTRAINT fk_editora_livro FOREIGN KEY (editora) REFERENCES editora(NIPC)
    );
    CREATE NONCLUSTERED INDEX idx_livro_titulo ON biblioteca.dbo.livro (  titulo ASC  )  
        WITH (  PAD_INDEX = OFF ,FILLFACTOR = 100  ,SORT_IN_TEMPDB = OFF , IGNORE_DUP_KEY = OFF , STATISTICS_NORECOMPUTE = OFF , ONLINE = OFF , ALLOW_ROW_LOCKS = ON , ALLOW_PAGE_LOCKS = ON  )
        ON [PRIMARY ] ;
END
-- biblioteca.dbo.escreve definition

-- Drop table

-- DROP TABLE biblioteca.dbo.escreve;
if OBJECT_ID('biblioteca.dbo.escreve', 'U') IS NULL
BEGIN
    CREATE TABLE escreve (
        autor char(10) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
        livro char(14) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
        CONSTRAINT pk_escreve PRIMARY KEY (autor,livro),
        CONSTRAINT fk_autor_escreve FOREIGN KEY (autor) REFERENCES autor(id_pessoa),
        CONSTRAINT fk_escreve_livro FOREIGN KEY (livro) REFERENCES livro(ISBN)
    );
END

BEGIN TRANSACTION
    BEGIN TRY
        -- Insert data into tables

        IF OBJECT_ID('biblioteca.dbo.editora', 'U') IS NOT NULL
        BEGIN
            INSERT INTO biblioteca.dbo.editora (NIPC,nome,contacto,morada) VALUES
                (N'500123456',N'FCA',NULL,NULL),
                (N'500654321',N'Campus',NULL,NULL),
                (N'500987654',N'Addison',NULL,NULL);
        END

        IF OBJECT_ID('biblioteca.dbo.livro', 'U') IS NOT NULL
        BEGIN
            INSERT INTO biblioteca.dbo.livro (ISBN,titulo,idioma,tema,tipo,editora,dtPub,original) VALUES
                (N'978-0201385908',N'An Introduction to Database Systems',N'EN',N'database systems',N'Hardcover',N'500987654',1989,NULL),
                (N'978-8535212730',N'Introdução a Sistemas de Bancos de Dados',N'PT',N'database systems',N'capa dura',N'500654321',2004,N'978-0201385908'),
                (N'978-9727224432',N'SQL, 6ª edição',N'PT',N'database systems',N'capa mole',N'500123456',2005,NULL),
                (N'978-9727228294',N'SQL, 14ª edição',N'PT',N'database systems',N'capa mole',N'500123456',2017,NULL),
                (N'978-9727229017',N'Bases de Dados, Fundamentos, 2ª edição',N'PT',N'database systems',N'capa mole',N'500123456',2021,NULL),
                (N'978-9727229215',N'Bases de Dados Relacionais',N'PT',N'database systems',N'capa mole',N'500123456',2021,NULL),
                (N'978-9727229406',N'Programação em Python, Fundamentos',N'PT',N'Programming',N'capa mole',N'500123456',2024,NULL),
                (N'978-9727229451',N'Linguagem C, 25ª edição',N'PT',N'Programming',N'capa mole',N'500123456',2025,NULL);
        END

        IF OBJECT_ID('biblioteca.dbo.autor', 'U') IS NOT NULL
        BEGIN
            INSERT INTO biblioteca.dbo.autor (id_pessoa,nome,dtNasce,contacto) VALUES
                (N'A001      ',N'José Silva','1980-05-12',N'912345678'),
                (N'A002      ',N'Maria Oliveira','1990-01-01',NULL),
                (N'A003      ',N'Ana Costa','1990-11-23',N'913456789'),
                (N'A004      ',N'Carlos Mendes',NULL,NULL),
                (N'A005      ',N'Luís Ferreira','1975-09-30',N'919876543'),
                (N'A006      ',N'Paula Ramos','1985-03-15',NULL),
                (N'A007      ',N'Rui Sousa',NULL,NULL),
                (N'A008      ',N'Sofia Pinto',NULL,N'915678901'),
                (N'A009      ',N'C.J.Date','1941-01-18',NULL),
                (N'A010      ',N'Luís Damas',NULL,NULL),
                (N'A011      ',N'Ernesto Costa',NULL,NULL),
                (N'A012      ',N'Feliz Gouveia',NULL,NULL),
                (N'A013      ',N'Orlando Belo',NULL,NULL),
                (N'A014      ',N'Daniel Vieira',NULL,NULL),
                (N'A015      ',N'Sergio Lifschitz',NULL,NULL);
        END

        IF OBJECT_ID('biblioteca.dbo.escreve', 'U') IS NOT NULL
        BEGIN
            INSERT INTO biblioteca.dbo.escreve (autor,livro) VALUES
                (N'A009      ',N'978-0201385908'),
                (N'A010      ',N'978-9727224432'),
                (N'A010      ',N'978-9727228294'),
            (N'A010      ',N'978-9727229451'),
            (N'A014      ',N'978-8535212730'),
            (N'A015      ',N'978-8535212730');
        END

    END TRY
    
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH
END