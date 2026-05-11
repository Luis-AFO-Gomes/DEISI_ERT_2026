USE biblioteca;

SELECT * FROM dbo.livro;

IF COL_LENGTH('dbo.livro', 'disponivel') IS NULL
BEGIN
    ALTER TABLE dbo.livro
    ADD disponivel varchar(20) NOT NULL CONSTRAINT DF_livro_disponivel DEFAULT('disponivel');
END


UPDATE dbo.livro
SET disponivel = CASE
    WHEN RTRIM(ISBN) IN ('978-9727229451', '978-9727228294', '978-9727229406') THEN 'emprestado'
    WHEN RTRIM(ISBN) IN ('978-9727224432') THEN 'retirado'
    ELSE 'disponivel'
END;
