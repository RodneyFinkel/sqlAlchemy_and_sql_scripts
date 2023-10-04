CREATE FUNCTION dbo.udf_GetNumeric(@strAlphaNumeric VARCHAR(256))
RETURNS VARCHAR(256)
AS
BEGIN
  DECLARE @intAlpha INT
  SET @intAlpha = PATINDEX('%[^0-9]%', @strAlphaNumeric)
  BEGIN
    WHILE @intAlpha > 0 
    BEGIN
      SET @strAlphaNumeric = STUFF(@strAlphaNumeric, @intAlpha, 1, '' )
      SET @intAlpha = PATINDEX('%[^0-9]%', @strAlphaNumeric )
    END
  END
  RETURN ISNULL(@strAlphaNumeric,0)
END
GO


CREATE FUNCTION dbo.udf_GetNonNumeric2(@strAlphaNumeric VARCHAR(256))
RETURNS VARCHAR(256)
AS
BEGIN
  DECLARE @intAlpha INT
  SET @intAlpha = PATINDEX('%[^a-z]%', @strAlphaNumeric)
  BEGIN
    WHILE @intAlpha > 0
    BEGIN
      SET @strAlphaNumeric = STUFF(@strAlphaNumeric, @intAlpha, 1, '' )
      SET @intAlpha = PATINDEX('%[0-9]%', @strAlphaNumeric )
    END
  END
  RETURN ISNULL(@strAlphaNumeric,0)
END
GO


CREATE FUNCTION dbo.udf_Getalpha_alt4(@strAlphaNumeric VARCHAR(256))
RETURNS VARCHAR(256)
AS
BEGIN
  DECLARE @intAlpha INT
  SET @intAlpha = PATINDEX('%[^a-z]%', @strAlphaNumeric)
  BEGIN
    WHILE @intAlpha > 0
    BEGIN
      SET @strAlphaNumeric = STUFF(@strAlphaNumeric, @intAlpha, 1, ' ' )
      SET @intAlpha = PATINDEX('%[^a-z]%', @strAlphaNumeric )
    END
  END
  RETURN ISNULL(@strAlphaNumeric,0)
END
GO


CREATE FUNCTION [dbo].[StripNonNumerics]
(
  @Temp varchar(255)
)
RETURNS varchar(255)
AS
Begin

    Declare @KeepValues as varchar(50)
    Set @KeepValues = '%[^0-9]%'
    While PatIndex(@KeepValues, @Temp) > 0
        Set @Temp = Stuff(@Temp, PatIndex(@KeepValues, @Temp), 1, '')

    Return @Temp
End


-- CREATE FUNCTION dbo.udf_BURSA(@strAlphaNumeric NVARCHAR(256))
-- RETURNS FLOAT(53)
-- AS
-- BEGIN
--   DECLARE @float FLOAT(53)
--   SET @float = PATINDEX('[^+]%', @strAlphaNumeric)
--   BEGIN
--     WHILE @float > 0 
--     BEGIN
--       SET @strAlphaNumeric = STUFF(@strAlphaNumeric, @float, 1, '' )
--       SET @float = PATINDEX('[^+]%', @strAlphaNumeric )
--     END
--   END
--   RETURN ISNULL(@strAlphaNumeric,0)
-- END
-- GO



---RUNNING THE FUNCTION

/*SELECT dbo.udf_GetNumeric(Column_Name) 
from Table_Name


---WILDCARD DETAILS %[^0-9]%   %% anything inside the brackets, [] represents any single character within the brackets, ^ NOT, - represents any character within the range

STUFF() replaces stuff inside a string...
PATINDEX() finds the index of the first character within a predefined patterns using for example wildcards


BURSA_2022_FUNCTION---


