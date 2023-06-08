-- Create the transactions table
CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  src_bank_account VARCHAR(255) NOT NULL,
  dst_bank_account VARCHAR(255) NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  direction VARCHAR(10) NOT NULL,
  status VARCHAR(10) NOT NULL
);
