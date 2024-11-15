INSERT INTO ts_data_sp (date, time, price, volume)
SELECT STR_TO_DATE(date, '%m/%d/%Y') as date, time, price, volume
FROM raw_data_sp;

select * from ts_data_sp where year(date) = 2019;