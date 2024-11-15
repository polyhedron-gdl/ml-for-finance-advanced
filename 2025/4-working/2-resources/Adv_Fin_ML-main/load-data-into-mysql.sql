# how find the secure folder 
# mysql> SHOW VARIABLES LIKE "secure_file_priv";
# 
#+------------------+------------------------------------------------+
#| Variable_name    | Value                                          |
#+------------------+------------------------------------------------+
#| secure_file_priv | C:\ProgramData\MySQL\MySQL Server 5.7\Uploads\ |
#+------------------+------------------------------------------------+
#
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/SP.csv' INTO TABLE raw_data_sp FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;

