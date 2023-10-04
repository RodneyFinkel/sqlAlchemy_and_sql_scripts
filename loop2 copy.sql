CREATE TABLE Test_Table (cola INT, colb CHAR(3));
GO
SET NOCOUNT ON;
GO

DECLARE @MyCounter INT;
SET @MyCounter = 1;
WHILE (@MyCounter < 26)
BEGIN;
	INSERT INTO Test_Table VALUES
		(@MyCounter, CHAR((@MyCounter + ASCII('a')))
		);
	SET @MyCounter = @MyCounter + 1;
END;
GO
SET NOCOUNT OFF;
GO

SELECT cola, colb
FROM Test_Table;
GO
DROP TABLE Test_Table
GO
