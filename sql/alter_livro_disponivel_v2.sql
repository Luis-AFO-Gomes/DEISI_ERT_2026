USE biblioteca;

IF COL_LENGTH('dbo.livro', 'disponivel') IS NULL
BEGIN
    ALTER TABLE dbo.livro
    ADD disponivel varchar(20) NOT NULL CONSTRAINT DF_livro_disponivel DEFAULT('disponivel');
END
ELSE
BEGIN
    IF EXISTS (
        SELECT 1
        FROM sys.columns c
        JOIN sys.types t ON c.user_type_id = t.user_type_id
        WHERE c.object_id = OBJECT_ID('dbo.livro') AND c.name = 'disponivel' AND t.name = 'bit'
    )
    BEGIN
        ALTER TABLE dbo.livro ADD disponivel_tmp varchar(20) NOT NULL CONSTRAINT DF_livro_disponivel_tmp DEFAULT('disponivel');
        UPDATE dbo.livro SET disponivel_tmp = CASE WHEN disponivel = 1 THEN 'disponivel' ELSE 'emprestado' END;
        ALTER TABLE dbo.livro DROP COLUMN disponivel;
        EXEC sp_rename 'dbo.livro.disponivel_tmp', 'disponivel', 'COLUMN';
    END
END

UPDATE dbo.livro
SET disponivel = CASE
    WHEN RTRIM(ISBN) IN ('978-9727229451', '978-9727228294') THEN 'emprestado'
    WHEN RTRIM(ISBN) IN ('978-9727224432') THEN 'retirado'
    ELSE 'disponivel'
END;
