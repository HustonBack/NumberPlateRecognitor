CREATE TABLE entries
(
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    customer_id MEDIUMINT NOT NULL,
    reg_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    in_out CHAR(5) NOT NULL,
    PRIMARY KEY(id)
);
GO