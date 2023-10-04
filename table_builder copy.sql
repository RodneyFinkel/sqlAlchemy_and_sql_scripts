USE [B22]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[BURSA_2022_ALCHEMY7777](
	[מס גיליון] [nvarchar](max) NULL,
	[ת.סליקה] [nvarchar](max) NULL,
	[סוג פעולה] [nvarchar](max) NULL,
	[שם סוג פעולה] [nvarchar](max) NULL,
	[קבוצה] [nvarchar](max) NULL,
	[שם קבוצה] [nvarchar](max) NULL,
	[מס נייר] [nvarchar](max) NULL,
	[שם נייר] [nvarchar](max) NULL,
	[סוג נייר] [nvarchar](max) NULL,
	[תת סוג נייר] [nvarchar](max) NULL,
	[כמות] [nvarchar](max) NULL,
	[שער] [nvarchar](max) NULL,
	[תמורה כספית] [nvarchar](max) NULL,
	[חשבון] [nvarchar](max) NULL,
	[אסמכתה] [nvarchar](max) NULL,
	[עמלה] [varchar](53) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
