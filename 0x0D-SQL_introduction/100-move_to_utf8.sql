-- convert database to utf8

ALTER DATABASE hbtn_0c_0
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE = utf8mb4_unicode_ci;

ALTER TABLE first_table
DEFAULT CHARACTER SET utf8mb4 
DEFAULT COLLATE utf8mb4_unicode_ci;
